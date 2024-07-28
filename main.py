import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
import unit_price, ui
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(640, 480)
        self.table_ = ui.xlsx_ui(self)
        self.initUI()
        self.show()

    def initUI(self):
        self.setCentralWidget(self.table_)

    def resizeEvent(self, event):
        self.table_.setGeometry(0, 0, self.width(), self.height())

    def closeEvent(self, a0):
        self.table_.running = False
        self.table_.close()


if __name__ == '__main__':
    print(unit_price.price_dict)
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())
