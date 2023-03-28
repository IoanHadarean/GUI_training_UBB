import os
import time

from PyQt6.QtCore import QThreadPool, QThread, QObject, pyqtBoundSignal, pyqtSignal
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
        task = ExtractDataTask([1, 2, 3, 4])
        self.task = task
        self.extractor = QThread()
        task.moveToThread(self.extractor)
        self.extractor.started.connect(task.start_extraction)
        task.extractDataFinishedSignal.connect(self.extractor.quit)
        task.extractDataFinishedSignal.connect(task.deleteLater)
        task.extractDataFinishedSignal.connect(self.show_success_message)
        self.extractor.finished.connect(self.thread_done)
        self.extractor.finished.connect(self.extractor.deleteLater)
        self.extractor.start()

    def thread_done(self):
        print('Done')

    def extract_data(self):
        for i in range(10):
            print("Started")

    def show_gui(self):
        self._mainwindow.show()

    def run(self):
        return self._app.exec()

    def show_success_message(self, message):
        print(message)
        print()


class ExtractRestaurantsByCity(QThread):

    def __init__(self, function):
        super(ExtractRestaurantsByCity, self).__init__()
        self.function = function

    def run(self):
        self.function()


class ExtractDataTask(QObject):

    extractDataFinishedSignal: pyqtBoundSignal = pyqtSignal(str)

    def __init__(self, list_of_numbers):
        super().__init__()
        self.nums = list_of_numbers
        self.powers_of_nums = []

    def start_extraction(self):
        self.powers_of_nums = [num ** 2 for num in self.nums]
        self.extractDataFinishedSignal.emit("Extraction finished")


