import CoinData as cd
from PyQtTextScroll import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time

class StockWidget(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=parent)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.ticker = TickerWidget()
        self.ticker.setText('Welcome')
        self.layout.addWidget(self.ticker)
        self.textEdit = QTextEdit()
        self.textEdit.resize(200,200)
        self.layout.addWidget(self.textEdit)
        self.button = QPushButton('Search For Conversion')
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.updateTicker)
    def updateTicker(self):
        coin = self.textEdit.toPlainText()
        coinlist = cd.getCoinData(coin,1)
        connector = '-'
        self.ticker.setText(connector.join(coinlist))
        self.textEdit.clear()
if __name__ == '__main__':
    a=QApplication(sys.argv)
    sw = StockWidget()
    sw.resize(500,500)
    sw.show()
    sys.exit(a.exec_())

