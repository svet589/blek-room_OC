import zipfile
import os

def unpack_archive(args):
    if not args:
        print("Использование: unpack <архив> [папка]")
        return
    archive = args[0]
    if not os.path.exists(archive):
        print("Архив не найден.")
        return
    extract_dir = args[1] if len(args) > 1 else archive.replace('.zip', '').replace('.rar', '')
    try:
        with zipfile.ZipFile(archive, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            print(f"Распаковано в {extract_dir}")
    except Exception as e:
        print(f"Ошибка распаковки: {e}")