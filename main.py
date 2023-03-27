import os
import sys


import ctypes

if sys.platform.startswith("win"):
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Tazz-GUI")

from views.mainview import MainView
from models.mainmodel import MainModel

os.chdir(r"C:\Users\hadarean\PycharmProjects\GUI_training_UBB")


def main():
    main_model = MainModel()
    main_view = MainView(main_model)
    main_view.show_gui()

    exitcode = main_view.run()

    return exitcode


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(e)
