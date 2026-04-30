import time
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

def beep():
    """Звук в Termux (работает через print)"""
    sys.stdout.write('\a')
    sys.stdout.flush()

def slow_print(text, delay=0.03, sound=False):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if sound:
            beep()
        time.sleep(delay)
    print()

def drop_letters(word, target_color=Fore.RED):
    """Падающие буквы"""
    screen_width = 80
    padding = (screen_width - len(word)) // 2
    print("\n" * 8)
    for i, letter in enumerate(word):
        for drop in range(10):
            sys.stdout.write("\033[1;1H")
            print(" " * (padding + i) + " " * drop + letter)
            time.sleep(0.02)
        sys.stdout.write("\033[1;1H")
        print(" " * (padding + i) + letter)
        beep()
        time.sleep(0.05)

def melt_letters(word, target_color=Fore.RED):
    """Стекание букв"""
    screen_width = 80
    padding = (screen_width - len(word)) // 2
    for i, letter in enumerate(word):
        for step in range(6):
            sys.stdout.write("\033[1;1H")
            melted = " " * step + letter
            print(" " * (padding + i) + melted)
            time.sleep(0.03)

def progress_bar():
    """Прогресс-бар с рывками"""
    steps = [5, 12, 27, 45, 68, 84, 95, 100]
    bar_length = 50
    for percent in steps:
        filled = int(bar_length * percent // 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        sys.stdout.write(f"\r{Fore.RED}Загрузка: [{bar}] {percent}%{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.15 if percent < 95 else 0.4)
        if percent >= 95:
            beep()
    print("\n")

def show_demon():
    """ASCII-демон / палач"""
    demon = f"""
{Fore.RED}
    ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
   ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
   ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
   ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌
   ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
    ▀▀▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌
             ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌
    ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
{Style.RESET_ALL}
"""
    for line in demon.split('\n'):
        slow_print(line, delay=0.005, sound=False)
        time.sleep(0.02)

def welcome_to_hell():
    """Добро пожаловать в ад"""
    text = f"{Fore.RED}ДОБРО ПОЖАЛОВАТЬ В АД{Style.RESET_ALL}"
    slow_print(text, delay=0.05, sound=True)
    time.sleep(0.8)

def full_banner():
    """Полная анимация запуска"""
    os.system('clear')
    drop_letters("BLEK-ROOM")
    time.sleep(0.3)
    melt_letters("BLEK-ROOM")
    time.sleep(0.3)
    progress_bar()
    show_demon()
    welcome_to_hell()
    time.sleep(1)

# Для совместимости со старым импортом
BANNER = ""
