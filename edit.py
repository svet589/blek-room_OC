import subprocess
import os

def edit_file(args):
    if not args:
        print("Использование: edit <файл>")
        return
    filename = args[0]
    if not os.path.exists(filename):
        open(filename, 'w').close()
        print(f"Создан новый файл: {filename}")
    subprocess.call(['nano', '-w', filename])
    print("Редактор закрыт.")