import sys
import string

from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup

from caesar_cipher import translatation
from generated_ui import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Шифр цезаря")

        self.ui.group1 = QButtonGroup()
        self.ui.group1.addButton(self.ui.lang1)
        self.ui.group1.addButton(self.ui.lang2)

        self.ui.group2 = QButtonGroup()
        self.ui.group2.addButton(self.ui.action1)
        self.ui.group2.addButton(self.ui.action2)

        self.ui.lang1.setChecked(True)
        self.ui.action1.setChecked(True)

        self.ui.translateBtn.clicked.connect(self.translate)

    def translate(self):
        data = self.ui.inputData.text()
        n = self.ui.spinBox.text()
        print(data, n)
        # processed_data = translatation(self.alphabet, data, n)
        self.ui.outputLabel.setText("кто")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    english_alphabet = string.ascii_lowercase
    russian_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]

    window.show()
    sys.exit(app.exec())
