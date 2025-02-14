
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, QTime, QDate, Qt
from PySide6.QtGui import QFont, QPixmap
from lora_module import LoRaHandler

class ListeningPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_timers()
        self.lora_handler = LoRaHandler()
        self.current_alert = None
        
    def setup_ui(self):
        # Layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)

        # Time label
        self.time_label = QLabel(self)
        self.time_label.setFont(QFont("sans-serif", 50, QFont.Bold))
        self.layout.addWidget(self.time_label, alignment=Qt.AlignHCenter)

        # Date label
        self.date_label = QLabel(self)
        self.date_label.setFont(QFont("sans-serif", 18, QFont.Bold))
        self.layout.addWidget(self.date_label, alignment=Qt.AlignHCenter)

        # Alert label
        self.alert_label = QLabel(self)
        self.alert_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.alert_label)
        
    def setup_timers(self):
        # Clock timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        # Alert check timer
        self.alert_check_timer = QTimer(self)
        self.alert_check_timer.timeout.connect(self.check_for_alert)
        self.alert_check_timer.start(500)

        # Listening timer
        self.listening_timer = QTimer(self)
        self.listening_timer.setSingleShot(True)
        self.listening_timer.timeout.connect(self.show_alert)
        
    def update_clock(self):
        if not self.current_alert:
            current_time = QTime.currentTime().toString("hh:mm AP")
            current_date = QDate.currentDate().toString("dddd, MMMM d")
            self.time_label.setText(current_time)
            self.date_label.setText(current_date)
            self.alert_label.clear()
            
    def check_for_alert(self):
        try:
            with open("alert.txt", "r") as file:
                alert = file.read().strip()
                if alert and alert != self.current_alert:
                    self.start_listening_phase(alert)
        except FileNotFoundError:
            pass
            
    def start_listening_phase(self, alert_type):
        self.time_label.setText("Listening...")
        self.date_label.clear()
        self.alert_label.clear()
        self.current_alert = alert_type
        self.listening_timer.start(2000)
        
    def show_alert(self):
        if self.current_alert:
            icon_path = self.get_icon_path(self.current_alert)
            if icon_path:
                pixmap = QPixmap(icon_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.alert_label.setPixmap(pixmap)
                self.time_label.setText(f"Alert: {self.current_alert.replace('_', ' ').title()}")
                self.date_label.clear()
                
    def get_icon_path(self, alert_type):
        icon_map = {
            "fire_alarm": "fire_truck.png",
            "earthquake": "earthquake.png",
            "flag_ceremony": "flag.png",
            "door_knock": "door.png",
            "car_horn": "car.png",
            "ambulance_siren": "ambulance.png",
            "police_siren": "police.png",
            "dog_bark": "dog.png",
            "loud_voice": "voice.png"
        }
        return icon_map.get(alert_type)