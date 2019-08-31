from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen

class MyLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False
    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()

    def mouseReleaseEvent(self, event):
        self.flag = False

    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        rect = QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(rect)
