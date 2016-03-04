import sys
from PySide.QtCore import*
from PySide.QtGui import*

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(255, 255, 255))
        p.setBrush(QColor(0, 255, 255))
        p.drawPolygon([QPoint(50, 200), QPoint(450, 200), QPoint(50, 400), QPoint(450, 400),])
        
        p.end

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())