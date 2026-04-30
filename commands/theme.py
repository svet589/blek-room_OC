from blek import load_config, save_config, C_ERROR, C_SUCCESS

def change_theme(args):
    if not args:
        print("Использование: theme [red|green]")
        return
    new_theme = args[0]
    if new_theme not in ["red", "green"]:
        print("Доступные темы: red, green")
        return
    config = load_config()
    config["theme"] = new_theme
    save_config(config)
    # TODO: динамически менять цветовые константы (сложно без restart)
    print(f"Тема изменена на {new_theme}. Перезапустите BLEK-ROOM для применения.")
