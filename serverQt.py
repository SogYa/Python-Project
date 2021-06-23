from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(400, 300)
        self.textBrowser = QtWidgets.QTextBrowser(Server)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 381, 100))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "Server"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Server = QtWidgets.QDialog()
    ui = Ui_Server()
    ui.setupUi(Server)
    Server.show()
    sys.exit(app.exec_())
