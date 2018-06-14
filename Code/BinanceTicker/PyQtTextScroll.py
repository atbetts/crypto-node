import CoinData as cd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time

class TickerWidget(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=parent)
        self.timer = QTimer(self)
        def paintme():
            self.update()
        self.xint = 0
        self.timer.timeout.connect(paintme)
        self.text = 'lmao dude'     
        self.timer.start(10)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
   

    def setText(self,text):
        self.text = text
    def paintEvent(self,event):
        super().paintEvent(event)
        painter = QPainter(self)
        fontsize = self.size().height()/10;
        font = QFont('Arial',fontsize)
        painter.setFont(font)
        fm = painter.fontMetrics()
        origin = QPoint(self.xint,fontsize)
        textwidth = fm.width(self.text)
        painter.drawText(origin,self.text)
        self.scroll(textwidth)
    
    def scroll(self,textlength):
        size = self.size()
        self.xint = self.xint + size.width()/1000
        if self.xint > size.width():
            self.xint = -textlength
        
if __name__ == '__main__':
    a = QApplication(sys.argv)
    w = TickerWidget()
    w.resize(500,500)
    w.show()
    w.setText('chili')
    sys.exit(a.exec_())
