import sys
from PySide.QtCore import*
from PySide.QtGui import*

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setMinimumSize(500, 500)

    def mousePressEvent(self, e):

        

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.anim_area = Animation_area()

        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)

        label = QLabel("                                                                  Drag the mouse to draw")
        layout.addWidget(label)

        clearButton = QPushButton("Clear")
        layout.addWidget(clearButton)

        self.setLayout(layout)
        self.setMinimumSize(530, 600)

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())