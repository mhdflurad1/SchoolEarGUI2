# mainpage.py
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from listen_page import ListeningPage
from stylesheet import StyleSheet

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        # Apply the stylesheet
        self.setStyleSheet(StyleSheet.MAIN_STYLE)
        self.resize(500, 300)
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        
        # Add the listening page
        self.listening_page = ListeningPage()
        layout.addWidget(self.listening_page)

def main():
    app = QApplication(sys.argv)
    window = MainPage()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()