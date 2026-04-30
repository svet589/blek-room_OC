import subprocess
import os

def run_script(args):
    if not args:
        print("Использование: run <script.py>")
        return
    script = args[0]
    if not os.path.exists(script) or not script.endswith('.py'):
        print("Файл не найден или не является Python-скриптом.")
        return
    print(f"Запуск {script}...")
    subprocess.run(['python', script])
