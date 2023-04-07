import sys

from PyQt6.QtWidgets import QApplication

from Treaba_mea.GUI.GUI_view import MainPage


def call_GUI():
    app = QApplication(sys.argv)
    app.setStyleSheet('''
    QWidget{
        font-size: 15px;
    }
    QPushButton{
        font-size: 18px;
    }
    ''')
    window = MainPage()
    window.show()

    app.exec()


if __name__ == '__main__':
    call_GUI()
