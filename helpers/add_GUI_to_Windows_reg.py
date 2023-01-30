import argparse


from utils import Utilities

python_path = r"C:\Program Files\Python39\python.exe"
script_exe_path = r"C:\Users\hadarean\PycharmProjects\tazz_GUI\main.py"


def main(script_exe_path: str) -> None:
    start_toolkit_command = script_exe_path

    Utilities.add_to_windows_context_menu(
        filetype="Directory",
        registry_title="TazzGUI",
        command=start_toolkit_command,
        title="TazzGUI",
    )
    # Utilities.remove_windows_context_menu("Directory", "TazzGUI")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("script_exe_path")

    args = parser.parse_args()
    main(args.script_exe_path)
