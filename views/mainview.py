import os
import time

from PyQt6.QtCore import QThreadPool, QThread
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

        self._mainwindow.setGeometry(100, 100, 640, 627)
        self._mainwindow.move(30, 0)

        self._main_layout = QVBoxLayout()
        self._main_widget = QWidget()
        self._main_widget.setProperty("class", "main-window-widget")
        self._main_widget.setLayout(self._main_layout)
        self.pool = QThreadPool()
        self.extractor = ExtractRestaurantsByCity(self.extract_data)
        self.extractor.start()
        self.extractor.finished.connect(self.thread_finished)

    def extract_data(self):
        for i in range(10):
            print("Started")

    def show_gui(self):
        self._mainwindow.show()

    def run(self):
        return self._app.exec()


class ExtractRestaurantsByCity(QThread):

    def __init__(self, function):
        super(ExtractRestaurantsByCity, self).__init__()
        self.function = function

    def run(self):
        self.function()