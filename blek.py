#!/usr/bin/env python3
import os
import sys
import time
from colorama import Fore, Style, init
import getpass
import hashlib
import sqlite3
import json
from commands import edit, unpack, run, sandbox, env, history as hist, theme, scan
from assets.banner import full_banner   # ← импорт анимированной заставки

init(autoreset=True)

# ---------- CONSTANTS ----------
PASSWORD_FILE = "data/password.hash"
HISTORY_DB = "data/history.db"
CONFIG_FILE = "data/config.json"

C_ERROR = Fore.RED
C_SUCCESS = Fore.GREEN
C_WARNING = Fore.YELLOW
C_INFO = Fore.LIGHTCYAN_EX
C_PROMPT = Fore.LIGHTRED_EX
C_DIM = Fore.LIGHTBLACK_EX
C_BRIGHT = Fore.LIGHTWHITE_EX
C_RESET = Style.RESET_ALL

# ---------- PASSWORD ----------
def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def is_first_launch():
    return not os.path.exists(PASSWORD_FILE)

def set_password():
    print(f"\n{C_WARNING}[FIRST LAUNCH DETECTED]{C_RESET}")
    print("Установите пароль для доступа к BLEK-ROOM.\n")
    while True:
        pwd1 = getpass.getpass("Придумайте пароль: ")
        pwd2 = getpass.getpass("Повторите пароль: ")
        if pwd1 == pwd2:
            if len(pwd1) < 4:
                print(f"{C_ERROR}Пароль должен быть не короче 4 символов.{C_RESET}\n")
                continue
            with open(PASSWORD_FILE, "w") as f:
                f.write(hash_password(pwd1))
            print(f"\n{C_WARNING}[!] Пароль сохранён. НЕ ЗАБУДЬТЕ ЕГО!{C_RESET}")
            input("\nНажмите Enter, чтобы продолжить...")
            return True
        else:
            print(f"{C_ERROR}Пароли не совпадают.{C_RESET}\n")

def check_password():
    print(f"\n{C_INFO}[SYSTEM] Доступ к BLEK-ROOM требует авторизации.{C_RESET}\n")
    for attempt in range(3):
        pwd = getpass.getpass("Введите пароль: ")
        hashed_input = hash_password(pwd)
        with open(PASSWORD_FILE, "r") as f:
            stored_hash = f.read().strip()
        if hashed_input == stored_hash:
            print(f"{C_SUCCESS}[ACCESS GRANTED]{C_RESET}\n")
            return True
        else:
            left = 2 - attempt
            print(f"{C_ERROR}[ACCESS DENIED] Осталось попыток: {left}{C_RESET}\n")
    print(f"{C_ERROR}[SYSTEM] Превышено количество попыток. Выход.{C_RESET}")
    return False

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect(HISTORY_DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  command TEXT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def add_to_history(cmd):
    conn = sqlite3.connect(HISTORY_DB)
    c = conn.cursor()
    c.execute("INSERT INTO history (command) VALUES (?)", (cmd,))
    conn.commit()
    conn.close()

# ---------- CONFIG ----------
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    else:
        default = {"theme": "red"}
        with open(CONFIG_FILE, "w") as f:
            json.dump(default, f)
        return default

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

# ---------- COMMAND HANDLER ----------
def execute_command(cmd):
    parts = cmd.split()
    if not parts:
        return
    command = parts[0]
    args = parts[1:]

    if command == "help":
        show_help()
    elif command == "clear":
        clear_screen()
    elif command == "exit":
        sys.exit(0)
    elif command == "edit":
        edit.edit_file(args)
    elif command == "unpack":
        unpack.unpack_archive(args)
    elif command == "run":
        run.run_script(args)
    elif command == "sandbox":
        sandbox.sandbox_exec(args)
    elif command == "env":
        env.show_env()
    elif command == "history":
        hist.show_history()
    elif command == "theme":
        theme.change_theme(args)
    elif command == "scan":
        scan.scan_ports(args)
    else:
        print(f"{C_ERROR}[!] Неизвестная команда: {command}. Введите 'help' для списка.{C_RESET}")

def show_help():
    help_text = f"""
{C_INFO}Доступные команды:{C_RESET}
  {C_BRIGHT}help{C_RESET}      - показать эту справку
  {C_BRIGHT}clear{C_RESET}     - очистить экран и показать баннер
  {C_BRIGHT}exit{C_RESET}      - выйти из BLEK-ROOM
  {C_BRIGHT}edit{C_RESET}      - редактировать файл (nano)
  {C_BRIGHT}unpack{C_RESET}    - распаковать архив (.zip, .rar)
  {C_BRIGHT}run{C_RESET}       - запустить Python-скрипт
  {C_BRIGHT}sandbox{C_RESET}   - выполнить команду в изолированной папке
  {C_BRIGHT}env{C_RESET}       - показать информацию о системе
  {C_BRIGHT}history{C_RESET}   - показать историю команд
  {C_BRIGHT}theme{C_RESET}     - сменить цветовую схему (red/green)
  {C_BRIGHT}scan{C_RESET}      - сканировать порты (локальный хост)
"""
    print(help_text)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
    full_banner()   # ← анимированная заставка

# ---------- MAIN ----------
def main():
    if is_first_launch():
        set_password()
    if not check_password():
        sys.exit(1)
    init_db()
    load_config()
    clear_screen()   # ЗАСТАВКА + ДЕМОН
    while True:
        try:
            cmd = input(f"{C_PROMPT}blek> {C_RESET}").strip()
            if cmd:
                add_to_history(cmd)
            execute_command(cmd)
        except KeyboardInterrupt:
            print(f"\n{C_WARNING}[SYSTEM] Прерывание. Выход...{C_RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()
