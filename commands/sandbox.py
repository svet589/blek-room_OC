import subprocess
import os
import tempfile

def sandbox_exec(args):
    if not args:
        print("Использование: sandbox <команда>")
        return
    command = ' '.join(args)
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Выполнение в песочнице: {tmpdir}")
        try:
            result = subprocess.run(command, shell=True, cwd=tmpdir,
                                    capture_output=True, text=True, timeout=5)
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
        except subprocess.TimeoutExpired:
            print("Команда превысила лимит времени (5 с).")
        except Exception as e:
            print(f"Ошибка: {e}")
