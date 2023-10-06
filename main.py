import sys
from PyQt5 import QtCore, QtGui, QtWidgets

windowsSize = [500, 500]

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("colored qrcodes")
        Dialog.resize(windowsSize[0], windowsSize[1])
 
        self.trackerTopLeft = QtWidgets.QGraphicsRectItem()
        #self.trackerTopLeft.setGeometry(QtCore.QRect(150, 70, 93, 28))
 
        #self.label = QtWidgets.QLabel(Dialog)
        #self.label.setGeometry(QtCore.QRect(130, 149, 151, 31))
        #self.label.setText("")
 
        #self.retranslateUi(Dialog)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        # adding signal and slot
        #self.pushButton.clicked.connect(self.showmsg)
 
    #def retranslateUi(self, Dialog):
        #_translate = QtCore.QCoreApplication.translate
        #Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        #self.pushButton.setText(_translate("Dialog", "Click"))
         
    #def showmsg(self):
        # slot
        #self.label.setText("You clicked me")
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
 
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())