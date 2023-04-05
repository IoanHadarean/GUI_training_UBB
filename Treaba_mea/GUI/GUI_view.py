from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiArea, QVBoxLayout, QWidget, QPushButton, QTextEdit


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.mainwindow = QMainWindow()
        self.setWindowIcon(QIcon("../style/app.ico"))
        self.setWindowTitle('Tazz Extractor')

        self.mainwindow.setGeometry(100, 100, 640, 627)
        self.mainwindow.move(30, 0)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        button = QPushButton()
        self.output = QTextEdit()

        main_layout.addWidget(button)
        main_layout.addWidget(self.output)


