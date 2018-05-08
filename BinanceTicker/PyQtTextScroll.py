import CoinData as cd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
print(cd.getCoinData('BTC',1)) #Testing Class import

class TickerWidget(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=parent)
        self.timer = QTimer(self)
        def paintme():
            self.update()
        self.xint = 0
        self.timer.timeout.connect(paintme)
        self.timer.start(10)
        
    def paintEvent(self,event):
        super().paintEvent(event)
        painter = QPainter(self)
        fontsize = self.size().height()/5;
        font = QFont('Arial',fontsize)
        painter.setFont(font)
        fm = painter.fontMetrics()
        origin = QPoint(self.xint,fontsize)
        textwidth = fm.width('lmao')
        painter.drawText(origin,'Lmao')
        self.scroll(textwidth)
    def scroll(self,textlength):
        size = self.size()
        self.xint = self.xint + size.width()/1000
        if self.xint+textlength > size.width():
            self.xint = 0
        
if __name__ == '__main__':
    a = QApplication(sys.argv)
    w = TickerWidget()
    w.resize(500,500)
    w.show()
    sys.exit(a.exec_())
