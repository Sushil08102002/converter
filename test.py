from PyQt5 import QtWidgets,uic

def convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text())*81.92))
app=QtWidgets.QApplication([])
dlg=uic.loadUi("test.ui")


# when we start our program then we already have our cursor on ruoees baar
dlg.lineEdit.setFocus()
# To place the place holder so that we know which value is to enter where
dlg.lineEdit.setPlaceholderText("Rupees")
dlg.lineEdit_2.setPlaceholderText("Dollar")

# run our program even when we hit enter
dlg.lineEdit.returnPressed.connect(convert)

#run our program when we click our push butoon
dlg.pushButton.clicked.connect(convert)

#this function is used so that our result cant be changed
dlg.lineEdit_2.setReadOnly(True)
dlg.show()
app.exec()