from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self, robot_list):
        super().__init__()
        self.setWindowTitle("DASC Ground Station")
        self.setFixedSize(QSize(1920, 1080))
        layout = QVBoxLayout()
        for robot in robot_list:
            button = QPushButton(robot)
            layout.addWidget(button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
app = QApplication([])
window = MainWindow(["drone1", "drone2"])
window.show()

app.exec()