import platform
import sys

def show_env():
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version}")
    try:
        import psutil
        mem = psutil.virtual_memory()
        print(f"RAM: {mem.total // (1024**3)} GB total, {mem.percent}% used")
    except ImportError:
        print("Для подробной RAM-информации установите 'pip install psutil'")
