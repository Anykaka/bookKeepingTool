import sys
from PyQt6.QtWidgets import QApplication
from win.main_window import MainWindow
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())
