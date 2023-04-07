import sys
import time

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiArea, QVBoxLayout, QWidget, QPushButton, QTextEdit, \
    QGridLayout
import threading
from Treaba_mea.Data_extraction import extract_restaurants, data_extraction_from_tazz


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        # self.mainwindow = QMainWindow()
        self.setWindowIcon(QIcon("../style/app.ico"))
        self.setWindowTitle('Tazz Extractor')

        # self.mainwindow.setGeometry(100, 100, 640, 627)
        # self.mainwindow.move(30, 0)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.output = QTextEdit()

        button = QPushButton('Extract data')
        button.clicked.connect(self.extract)
        button2 = QPushButton('View Data')
        button2.clicked.connect(self.new_window)
        main_layout.addWidget(button)
        main_layout.addWidget(button2)
        main_layout.addWidget(self.output)

    def extract(self):
        x = data_extraction_from_tazz.get_Cities()
        for i in x:
            city = i.split('/')[3]
            self.output.append(f'Extracting from {city}')
            a = threading.Thread(target=extract_restaurants.get_html, args=(i,))
            a.start()
            self.output.append(f'Done with {city}\n')

    def new_window(self):
        self.w = View_Restaurants()
        self.w.show()


class View_Restaurants(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("../style/app.ico"))
        self.setWindowTitle('Restaurant info')
        layout = QGridLayout()
        self.setLayout(layout)

        x = data_extraction_from_tazz.get_Cities()
        for ct, i in enumerate(x):
            city = i.split('/')[3]
            layout.addWidget(QPushButton(f'{city}'), ct / 2, ct % 2)
