import os


from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiArea, QVBoxLayout, QWidget

from models.mainmodel import MainModel


class MainView(object):
    def __init__(self, main_model: MainModel):
        print('Current Working Directory: ', os.getcwd())
        self.main_model = main_model

        self._app = QApplication([])
        self._file_path = os.path.dirname(__file__)
        self._app_dir = os.path.abspath(os.path.join(self._file_path, os.pardir))

        self._mainwindow = QMainWindow()
        self._mainwindow.mdi = QMdiArea()

        self._mainwindow.setWindowTitle('Tazz Extractor')
        self._mainwindow.setWindowIcon(QIcon("style/app.ico"))

        self._mainwindow.setGeometry(100, 100, 640, 627)
        self._mainwindow.move(30, 0)

        self._main_layout = QVBoxLayout()
        self._main_widget = QWidget()
        self._main_widget.setProperty("class", "main-window-widget")
        self._main_widget.setLayout(self._main_layout)

    def show_gui(self):
        self._mainwindow.show()

    def run(self):
        return self._app.exec()
