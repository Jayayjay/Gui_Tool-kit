from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class FloatingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Floating Window")
        self.setGeometry(100, 100, 300, 100)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        layout = QHBoxLayout()

        tools_button = QPushButton("Tools")
        layout.addWidget(tools_button)

        mic_button = QPushButton("🎤")
        mic_button.setStyleSheet("background-color: red; color: white;")
        layout.addWidget(mic_button)

        settings_button = QPushButton("Settings")
        layout.addWidget(settings_button)

        question_button = QPushButton("?")
        layout.addWidget(question_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

def main():
    app = QApplication(sys.argv)
    window = FloatingWindow()
    window.show()
    sys.exit(app.exec_())

main()
