# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(0)
        self.Table.setRowCount(0)
        self.gridLayout.addWidget(self.Table, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.Files = QtWidgets.QMenu(parent=self.menubar)
        self.Files.setObjectName("Files")
        self.Import = QtWidgets.QMenu(parent=self.Files)
        self.Import.setObjectName("Import")
        self.Export = QtWidgets.QMenu(parent=self.Files)
        self.Export.setObjectName("Export")
        self.DataBase = QtWidgets.QMenu(parent=self.menubar)
        self.DataBase.setObjectName("DataBase")
        self.About = QtWidgets.QMenu(parent=self.menubar)
        self.About.setObjectName("About")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.New = QtGui.QAction(parent=MainWindow)
        self.New.setObjectName("New")
        self.export_xml = QtGui.QAction(parent=MainWindow)
        self.export_xml.setObjectName("export_xml")
        self.import_xml = QtGui.QAction(parent=MainWindow)
        self.import_xml.setObjectName("import_xml")
        self.Connect = QtGui.QAction(parent=MainWindow)
        self.Connect.setObjectName("Connect")
        self.DisConnect = QtGui.QAction(parent=MainWindow)
        self.DisConnect.setObjectName("DisConnect")
        self.ChangeConnect = QtGui.QAction(parent=MainWindow)
        self.ChangeConnect.setObjectName("ChangeConnect")
        self.Save = QtGui.QAction(parent=MainWindow)
        self.Save.setObjectName("Save")
        self.Close = QtGui.QAction(parent=MainWindow)
        self.Close.setObjectName("Close")
        self.Exit = QtGui.QAction(parent=MainWindow)
        self.Exit.setObjectName("Exit")
        self.Import.addAction(self.import_xml)
        self.Export.addAction(self.export_xml)
        self.Files.addAction(self.New)
        self.Files.addAction(self.Save)
        self.Files.addAction(self.Close)
        self.Files.addAction(self.Import.menuAction())
        self.Files.addAction(self.Export.menuAction())
        self.Files.addAction(self.Exit)
        self.DataBase.addAction(self.Connect)
        self.DataBase.addAction(self.DisConnect)
        self.DataBase.addAction(self.ChangeConnect)
        self.menubar.addAction(self.Files.menuAction())
        self.menubar.addAction(self.DataBase.menuAction())
        self.menubar.addAction(self.About.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "项目物料清单管理系统"))
        self.Files.setTitle(_translate("MainWindow", "文件"))
        self.Import.setTitle(_translate("MainWindow", "导入文件"))
        self.Export.setTitle(_translate("MainWindow", "导出文件"))
        self.DataBase.setTitle(_translate("MainWindow", "数据库"))
        self.About.setTitle(_translate("MainWindow", "说明"))
        self.New.setText(_translate("MainWindow", "新建文件"))
        self.export_xml.setText(_translate("MainWindow", "xml"))
        self.import_xml.setText(_translate("MainWindow", "xml"))
        self.Connect.setText(_translate("MainWindow", "连接"))
        self.DisConnect.setText(_translate("MainWindow", "断开连接"))
        self.ChangeConnect.setText(_translate("MainWindow", "修改连接"))
        self.Save.setText(_translate("MainWindow", "保存文件"))
        self.Close.setText(_translate("MainWindow", "关闭文件"))
        self.Exit.setText(_translate("MainWindow", "关闭"))
