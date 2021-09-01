from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Addfunction import Ui_bk1
from DeleteABook import Ui_MainWindowDelete
from Displayby import Ui_MainWindowDisplay
from Modifyprice import Ui_MainWindowModify


class Ui_bookstore(object):
    def __init__(self):
        """
        Regular Constructor USED MORE IN TESTING
        """
        self.file = "C:/Users/Eng-Seif/Desktop/SVProjectPython/ui file/bookstore.jpg"
    def Addfunction(self):
        """
        Function of adding books
        :return:
        """
        self.add = QtWidgets.QMainWindow()
        self.ui = Ui_bk1()
        self.ui.setupUi(self.add)
        self.add.show()

    def Deletefunction(self):
        """
        Delete books from database
        :return:
        """
        self.delete = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowDelete()
        self.ui.setupUi(self.delete)
        self.delete.show()

    def Modifyfunction(self):
        """
        Modify price for a book
        :return:
        """
        self.modify = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowModify()
        self.ui.setupUi(self.modify)
        self.modify.show()

    def Displayallfunction(self):
        """
        Display all books either by all or authors or by price ascendingly
        :return:  None
        """
        self.displayall = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowDisplay()
        self.ui.setupUi(self.displayall)
        self.displayall.show()

    def Exit(self):
        """
        Exit Function
        :return: None
        """
        sys.exit()

    def setupUi(self, bookstore,str):
        """
        setUp the Ui
        :param bookstore: returns object
        :param str: string
        :return: None
        """
        bookstore.setObjectName("bookstore")
        bookstore.setFixedSize(616, 399)
        self.centralwidget = QtWidgets.QWidget(bookstore)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 150, 151, 21))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.Addfunction)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 190, 151, 21))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.Modifyfunction)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 170, 151, 21))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(self.Deletefunction)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 210, 151, 21))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_5.clicked.connect(self.Displayallfunction)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -10, 791, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWhatsThis("")
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        if self.file != 'C:/Users/Eng-Seif/Desktop/SVProjectPython/ui file/bookstore.jpg':
            return
        else:
            self.label.setPixmap(QtGui.QPixmap("C:/Users/Eng-Seif/Desktop/SVProjectPython/ui file/bookstore.jpg"))
            #For testing purposes
            #return 1
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 60, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.pushButton_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        bookstore.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(bookstore)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        bookstore.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(bookstore)
        self.statusbar.setObjectName("statusbar")
        bookstore.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(bookstore)

        self.actionExit.setObjectName("actionExit")

        self.actionExit.triggered.connect(self.Exit)

        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(bookstore,str)
        QtCore.QMetaObject.connectSlotsByName(bookstore)

    def retranslateUi(self, bookstore,str):
        """

        :param bookstore: object
        :param str: string
        :return: None
        SetText for all images
        """
        _translate = QtCore.QCoreApplication.translate
        bookstore.setWindowTitle(_translate("bookstore", "Bookstore"))
        bookstore.setToolTip(
            _translate("bookstore", "<html><head/><body><p><img src=\":/image/m.qrc\"/></p></body></html>"))
        self.pushButton.setText(_translate("bookstore", "Add a book"))

        self.pushButton_2.setText(_translate("bookstore", "Modify a price"))
        self.pushButton_4.setText(_translate("bookstore", "Delete a book"))

        self.pushButton_5.setText(_translate("bookstore", "Display all books"))

        self.label_2.setText(_translate("bookstore",
                                        "<html><head/><body><p><span style=\" color:#ffff7f;\">Bookstore</span></p></body></html>"))
        self.menuFile.setTitle(_translate("bookstore", "File"))
        self.actionExit.setText(_translate("bookstore", "Exit"))
        self.check_Labels(str)

    def check_Labels(self, str):
        """
        For testing purposes
        :param str: string
        :return:
        Checks if strings are set on GUI true or not
        """
        if str == self.pushButton.text() or str == self.pushButton_4.text() or str == self.pushButton_2.text() or\
                str == self.pushButton_5.text():
            return True
        else:
            return False


def main():
    """
    :return: None
    Main Program
    We connect sqlite either to delete a row or columns as a programmer in case i have a database and i need to uncomment
    those lines , OTHERWISE, i comment them.
    connection.commit() is a method to save the result of querying into the Database.

    Then the Ui_bookstore class makes an object of ui then setup the bookstore and show it

    """
    #connection = sqlite3.connect("bookstore.db")
    #cursor = connection.cursor()
    #cursor.execute("CREATE TABLE bookstore (id nvarchar(255) PRIMARY KEY,Book_Name nvarchar(225), pages int,PRICE int ,AUTHOR_NAME varchar(25))")
    #cursor.execute("DELETE FROM bookstore ")
    # cursor.execute("INSERT INTO bookstore VALUES (20184310,\"Harry Potter\",20,191.5,\"J.K. Rowling\")")
    # cursor.execute("DELETE FROM bookstore WHERE Book_Name = \'Harry Potter\'").fetchall()
    # print(connection.total_changes)
    # rows = cursor.execute("SELECT * FROM bookstore").fetchall()
    # print((cursor.execute("SELECT COUNT(id) from bookstore").fetchone())[0])
    #connection.commit()
    app = QtWidgets.QApplication(sys.argv)
    bookstore = QtWidgets.QMainWindow()
    ui = Ui_bookstore()
    ui.setupUi(bookstore,"")
    bookstore.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
