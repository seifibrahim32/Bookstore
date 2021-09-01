import sys

import pytest
from PyQt5 import QtWidgets

from main import Ui_bookstore

def test_func1():
    """
    Test case if the label text is found
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    bookstore = QtWidgets.QMainWindow()
    ui = Ui_bookstore()
    ui.setupUi(bookstore,"Add a book")
    assert ui.check_Labels("Add a book") == True, "Passed"
    bookstore.show()
    app.exit()
def test_func2():
    """
    Test case if the label text is found
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    bookstore = QtWidgets.QMainWindow()
    ui = Ui_bookstore()
    ui.setupUi(bookstore,"Delete a book")
    assert ui.check_Labels("Delete a book") == True, "Passed"
    bookstore.show()
    app.exit()
def test_fun3():
    """
    Test case if the label text isn't found
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    bookstore = QtWidgets.QMainWindow()
    ui = Ui_bookstore()
    ui.setupUi(bookstore, "Addk")
    bookstore.show()
    assert ui.check_Labels("Addk") == False, "Passed"
    app.exit()


def test_fun4():
    """
    Test case if the label text is found
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    bookstore = QtWidgets.QMainWindow()
    ui = Ui_bookstore()
    ui.setupUi(bookstore,"Delete a book")
    bookstore.show()
    assert ui.check_Labels("Delete a book") == True, "Passed"
    app.exit()

def test_fun5():
    """
    Test case if we encapsulated the setter to a wrong jpeg file
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    bookstore = QtWidgets.QMainWindow()
    ui = Ui_bookstore()
    ui.file = 'C:/Users/Eng-Seif/Desktop/SVProjectPython/ui file/bookstorve.jpg'
    bookstore.show()
    assert ui.setupUi(bookstore,"") is None, "Passed"
    app.exit()

def test_fun6():
    app = QtWidgets.QApplication(sys.argv)
    bookstore = QtWidgets.QMainWindow()
    ui = Ui_bookstore()
    ui.file = 'C:/Users/Eng-Seif/Desktop/SVProjectPython/ui file/bookstore.jpg'
    bookstore.show()
    assert ui.setupUi(bookstore, "") == 1, "Passed"
    app.exit()


if __name__ == '__main__':
    pytest.main()
