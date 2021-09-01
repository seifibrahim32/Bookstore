# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Displayby.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QPushButton


class Ui_MainWindowDisplay(object):
    def setupUi(self, MainWindow):
        """
        A setup for Ui.At opening the funciton it appears all books
        :param MainWindow:
        :return:
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(535, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 10, 231, 22))
        self.comboBox.setObjectName("comboBox")

        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 360, 75, 23))
        self.pushButton.clicked.connect(self.Refresh)

        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(60, 40, 431, 311))
        self.treeView.setObjectName("treeView")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(30, 40, 481, 311))
        self.treeWidget.setObjectName("treeWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        connection = sqlite3.connect("bookstore.db")
        cursor = connection.cursor()
        row = cursor.execute("SELECT * from bookstore")
        r = row.fetchall()
        print(r)
        #r = (row.fetchone())[0]
        # print(row.fetchall())
        """
        If exists so, Re-add Widgets due to how many columns
        """
        x = (cursor.execute("SELECT COUNT(id) from bookstore").fetchone())[0]
        a = 1
        while a <= x:
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            a = a + 1
        #print(r)
        """
        Inflator for books
        """
        if self.comboBox.currentText() == "Display all books":
            k = 0
            for i in r:
                col = 0
                self.treeWidget.topLevelItem(k).setText(col,QtCore.QCoreApplication.translate("MainWindow", str(i[0])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col,QtCore.QCoreApplication.translate("MainWindow", str(i[1])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col,QtCore.QCoreApplication.translate("MainWindow", str(i[4])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col,QtCore.QCoreApplication.translate("MainWindow", str(i[3])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col,QtCore.QCoreApplication.translate("MainWindow", str(i[2])))
                k = k+1
        connection.close()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Display all"))
        self.comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Display all books"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Display by authors"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Display by price"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Book ISBN"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Book Name"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Author"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Price"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Pages"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
    def Refresh(self):

        """
        Inflator for books
        """
        if self.comboBox.currentText() == "Display all books":
            k = 0
            connection = sqlite3.connect("bookstore.db")
            cursor = connection.cursor()
            row = cursor.execute("SELECT * from bookstore")
            r = row.fetchall()
            for i in r:
                col = 0
                self.treeWidget.topLevelItem(k).setText(col,QtCore.QCoreApplication.translate("MainWindow", str(i[0])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col,QtCore.QCoreApplication.translate("MainWindow", str(i[1])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col,QtCore.QCoreApplication.translate("MainWindow", str(i[4])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col,QtCore.QCoreApplication.translate("MainWindow", str(i[3])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col,QtCore.QCoreApplication.translate("MainWindow", str(i[2])))
                k = k+1

        elif self.comboBox.currentText() == "Display by authors":

            """
            Inflator for books ordered by authors
            """
            k = 0
            connection = sqlite3.connect("bookstore.db")
            cursor = connection.cursor()
            row = cursor.execute("SELECT * from bookstore ORDER BY AUTHOR_NAME ASC")
            r = row.fetchall()
            for i in r:
                col = 0
                self.treeWidget.topLevelItem(k).setText(col, QtCore.QCoreApplication.translate("MainWindow", str(i[0])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col, QtCore.QCoreApplication.translate("MainWindow", str(i[1])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col, QtCore.QCoreApplication.translate("MainWindow", str(i[4])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col, QtCore.QCoreApplication.translate("MainWindow", str(i[3])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col, QtCore.QCoreApplication.translate("MainWindow", str(i[2])))
                k = k + 1
        else:
            """
            Inflator for books ordered by ascendingly by Price
            """
            k = 0
            connection = sqlite3.connect("bookstore.db")
            cursor = connection.cursor()
            row = cursor.execute("SELECT * from bookstore ORDER BY PRICE ,id ASC")
            r = row.fetchall()
            for i in r:
                col = 0
                self.treeWidget.topLevelItem(k).setText(col, QtCore.QCoreApplication.translate("MainWindow", str(i[0])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col, QtCore.QCoreApplication.translate("MainWindow", str(i[1])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col, QtCore.QCoreApplication.translate("MainWindow", str(i[4])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col, QtCore.QCoreApplication.translate("MainWindow", str(i[3])))
                col = col + 1
                self.treeWidget.topLevelItem(k).setText(col, QtCore.QCoreApplication.translate("MainWindow", str(i[2])))
                k = k + 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowDisplay()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())