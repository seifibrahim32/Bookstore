import sqlite3
import sys

import pytest
from PyQt5 import QtWidgets

from Addfunction import Ui_bk1


def test_func():
    """
    Test Case if ISBN is more than 2018
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    connection = sqlite3.connect("bookstore.db")
    bk1 = QtWidgets.QMainWindow()
    ui = Ui_bk1()
    ui.strID = "201732"
    ui.strName = "sfsdfsdff"
    ui.strAuthor = "sfsdssdfsdff"
    ui.setupUi(bk1)
    bk1.show()
    assert ui.Check() == True, "Passed"
    connection.close()
    app.exit()

def test_func1():
    """
    Test Case if ISBN is less than 2018
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    connection = sqlite3.connect("bookstore.db")
    bk1 = QtWidgets.QMainWindow()
    ui = Ui_bk1()
    ui.strID = "2017"
    ui.strName = "sfsdfsdff"
    ui.strAuthor = "sfsdssdfsdff"
    ui.setupUi(bk1)
    bk1.show()
    assert ui.Check() == 'Less', "Passed"
    connection.close()
    app.exit()

def test_func2():

    """
    Test Case if ISBN is more than 2018 and ISBN is alphanumeric
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    connection = sqlite3.connect("bookstore.db")
    bk1 = QtWidgets.QMainWindow()
    ui = Ui_bk1()
    ui.strID = "2013323-3237"
    ui.strName = "sfsdfsdff"
    ui.strAuthor = "sfsdssdfsdff"
    ui.setupUi(bk1)
    bk1.show()
    assert ui.Check() == True, "Passed"
    connection.close()
    app.exit()
if __name__ == '__main__':
    """
    Main Program
    """
    pytest.main()
