import sys

from views.mainview import MainView
from models.mainmodel import MainModel


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
