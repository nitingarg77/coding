import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon 


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Demo")
        self.setGeometry(100, 100, 600, 400)
        #self.setWindowIcon(QIcon("icon.png"))  # Ensure you have an icon.png in the same directory


def main():
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()