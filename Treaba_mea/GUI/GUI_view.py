import sys
import time

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiArea, QVBoxLayout, QWidget, QPushButton, QTextEdit, \
    QGridLayout, QTableWidgetItem, QTableWidget, QHBoxLayout
import threading
from Treaba_mea.Data_extraction import extract_restaurants, data_extraction_from_tazz
from Treaba_mea.Data_extraction import sort_data


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
        self.setWindowTitle('Cities')
        layout = QGridLayout()
        self.setLayout(layout)
        x = data_extraction_from_tazz.get_Cities()
        for ct, i in enumerate(x):
            self.make_buttons(i, layout, ct)

    def make_buttons(self, url, layout, ct):
        city = url.split('/')[3]
        button = QPushButton(f'{city}')
        # Buttons_dict['timisoara'].clicked.connect(lambda: self.show_restaurants(f'https://tazz.ro/timisoara/oras'))
        button.clicked.connect(lambda: self.show_restaurants(f'https://tazz.ro/{city}/oras'))
        layout.addWidget(button, ct / 2, ct % 2)

    def show_restaurants(self, url):
        self.w = City_Window(url)
        self.w.show()


class City_Window(QWidget):
    def __init__(self, url):
        super().__init__()
        self.x = extract_restaurants.get_Restaurants_Per_city(url)
        self.initial = self.x
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.x))
        self.tableWidget.setColumnCount(3)
        self.url = url
        self.tableWidget.setHorizontalHeaderLabels(['Restaurant', 'Stele', 'Livrare'])
        self.resize(600, 500)
        self.city = url.split('/')[3]
        self.setWindowIcon(QIcon("../style/app.ico"))
        self.setWindowTitle(f'Restaurants {self.city}')
        self.layout = QVBoxLayout()
        self.set_data(self.x)
        button1 = QPushButton('Sort ASC by Name')
        button2 = QPushButton('Sort DESC by Name')

        button2.clicked.connect(self.sort_DESC)
        button1.clicked.connect(self.sort_INC)
        button3 = QPushButton('Filter Stars')
        button3.clicked.connect(self.filter_stars)
        reset = QPushButton('Reset')
        reset.clicked.connect(self.reset)
        self.stars = QTextEdit(self)
        self.stars.setMaximumHeight(30)
        self.layout.addWidget(button1)
        self.layout.addWidget(button2)
        self.layout.addWidget(button3)
        self.layout.addWidget(self.stars)
        self.layout.addWidget(reset)

        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def reset(self):
        self.x = self.initial
        self.update_table()
    def filter_stars(self):
        try:
            a = float(self.stars.toPlainText())
            if a < 0 or a > 5:
                self.stars.setPlainText("Wrong value")
            else:
                self.x = sort_data.filter_by_stars(self.url, a)
                self.update_table()
        except:
            self.stars.setPlainText("That was not a float")

    def sort_INC(self):
        self.x = sort_data.sortINC_Name(self.x)
        self.update_table()

    def sort_DESC(self):
        self.x = sort_data.sortDESC_Name(self.x)
        self.update_table()

    def update_table(self):
        self.tableWidget.clearContents()
        self.set_data(self.x)

    def set_data(self, x):
        self.tableWidget.setRowCount(len(x))

        for ct, i in enumerate(x):
            self.tableWidget.setItem(ct, 0, QTableWidgetItem(i))
            self.tableWidget.setItem(ct, 1, QTableWidgetItem(x[i][0]))
            self.tableWidget.setItem(ct, 2, QTableWidgetItem(x[i][1]))
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
