from gui import *
import galoisproject
import sys




class GUI(Ui_Dialog):
    def __init__(self,Dialog):
        self.setupUi(Dialog)
        self.pushButton.clicked.connect(self.evaluate)
        
        
    def evaluate(self):
        isBin=self.checkBox.isChecked()
        if isBin:
        	a = int(self.textEdit.toPlainText(),2)
        	b = int(self.textEdit_2.toPlainText(),2)
        else:
        	a = int(self.textEdit.toPlainText(),16)
        	b = int(self.textEdit_2.toPlainText(),16)
        m = int(self.comboBox.currentText())
        op = self.comboBox_2.currentText()
        
        if op == 'Add':
            result=galoisproject.add(a,b,m,isBin)
        elif op == 'Subtract':
            result=galoisproject.sub(a,b,m,isBin)
        elif op == 'Multiply':
            result=galoisproject.multiply(a,b,m,isBin)
        elif op == 'Divide':
            result=galoisproject.divide(a,b,m,isBin)
        elif op == 'Inverse':
            result=galoisproject.invert(a,m,isBin)
        elif op == 'Modulo':
            result=galoisproject.modulo(a,m,isBin)
            
        self.textBrowser.setText(str(result))

def main():           
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = GUI(MainWindow)
	MainWindow.show()
	app.exec_()

if __name__ == '__main__':
    main()
