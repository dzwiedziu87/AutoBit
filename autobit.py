import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 400)
        self.setWindowTitle("AutoBit")
        self.setWindowIcon(QIcon('icon.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    autobit = AppWindow()
    autobit.show()

    sys.exit(app.exec())