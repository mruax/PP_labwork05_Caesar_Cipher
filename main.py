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

        self.ui.lang1.toggled.connect(self.set_values)
        self.ui.lang2.toggled.connect(self.set_values)
        self.ui.action1.toggled.connect(self.set_values)
        self.ui.action2.toggled.connect(self.set_values)

        self.alphabet = russian_alphabet  # default
        self.action = 0  # default 0 (зашифровать)

    def translate(self):
        data = self.ui.inputData.text()
        n = int(self.ui.spinBox.text())
        self.set_values()
        if self.action:
            n *= -1
        processed_data = translatation(self.alphabet, data, n)
        self.ui.outputLabel.setText(processed_data)

    def set_values(self):
        if self.ui.lang1.isChecked():
            self.alphabet = russian_alphabet
        else:
            self.alphabet = english_alphabet
        if self.ui.action1.isChecked():
            self.action = 0
        else:
            self.action = 1


if __name__ == '__main__':
    english_alphabet = string.ascii_lowercase
    russian_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    russian_alphabet.insert(6, 'ё')

    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
