from PyQt5 import QtWidgets,uic

def convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text())*81.92))
app=QtWidgets.QApplication([])
dlg=uic.loadUi("test.ui")

dlg.pushButton.clicked.connect(convert)
dlg.show()
app.exec()