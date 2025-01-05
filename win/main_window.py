from PyQt6.QtWidgets import QApplication, QMainWindow
from win.ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self._update_connect()
        self.show()

    def _update_connect(self):
        print(f"创建各种信号槽相关连接")
