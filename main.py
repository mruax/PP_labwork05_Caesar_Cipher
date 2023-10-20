import sys
from pathlib import Path

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from caesar_cipher import translatation
from generated_ui import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Шифр цезаря")
        # icon = QIcon(str(Path("src/*.ico")))
        # self.setWindowIcon(icon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())