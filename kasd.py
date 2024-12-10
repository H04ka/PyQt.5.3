from PyQt5 import QtWidgets
import pasd 

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = pasd.Ui_Form()
        self.ui.setupUi(self)
        self.a = 0
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.pushButton.clicked.connect(self.pervoe)
        self.ui.pushButton_2.clicked.connect(self.vtoroe)
        self.ui.pushButton_3.clicked.connect(self.tretie)
        self.ui.pushButton_4.clicked.connect(self.chetvertoe)
        self.ui.pushButton_5.clicked.connect(self.pyatoe)
        self.ui.pushButton_6.clicked.connect(self.shestoe)
        self.ui.pushButton_8.clicked.connect(self.sedmoe)
        self.ui.pushButton_7.clicked.connect(self.dom2)

    def pervoe(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def vtoroe(self):
        if self.ui.radioButton_2.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(2)
    def tretie(self):
        if self.ui.radioButton_6.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(3)
    def chetvertoe(self):
        if self.ui.radioButton_9.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(4)
    def pyatoe(self):
        if self.ui.radioButton_12.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(5)
    def shestoe(self):
        if self.ui.radioButton_15.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(6)
    def sedmoe(self):
        if self.ui.radioButton_16.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(7)

        ocencka = {
            0 : 2,
            1 : 2,
            2 : 2,
            3 : 3,
            4 : 4,
            5 : 4,
            6 : 5,
        }
        
        self.ui.label_9.setText(f"= {self.a}")
        self.ui.label_11.setText(f" = {ocencka[self.a]}")

    def dom2(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.a = 0
        for btn in [self.ui.radioButton, self.ui.radioButton_2, self.ui.radioButton_3, self.ui.radioButton_4, self.ui.radioButton_5, self.ui.radioButton_6, self.ui.radioButton_7, self.ui.radioButton_8, self.ui.radioButton_9, self.ui.radioButton_10, self.ui.radioButton_11, self.ui.radioButton_12, self.ui.radioButton_13, self.ui.radioButton_14, self.ui.radioButton_15, self.ui.radioButton_16, self.ui.radioButton_17, self.ui.radioButton_18 ]:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.repaint()
            btn.setAutoExclusive(True)
            btn.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    