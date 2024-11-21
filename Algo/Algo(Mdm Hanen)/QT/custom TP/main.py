from PyQt5.uic import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import serial
from serial import Serial


class SerialReaderThread(QThread):
    new_message = pyqtSignal(str)  # Signal to send data to the GUI

    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial_conn = None
        self.running = True

    def run(self):
        try:
            # Initialize serial connection
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connected to {self.port} at {self.baudrate} baud")

            # Read from the serial port continuously
            while self.running:
                if self.serial_conn.in_waiting > 0:  # Check if data is available
                    line = self.serial_conn.readline().decode('utf-8').strip()
                    self.new_message.emit(line)  # Emit signal with the received message
        except serial.SerialException as e:
            self.new_message.emit("no signal")
        finally:
            if self.serial_conn and self.serial_conn.is_open:
                self.serial_conn.close()

    def stop(self):
        self.running = False
        self.quit()
        self.wait()

def app():
    app = QApplication([])
    w = loadUi("main.ui")

    # Initialize and start the serial reader thread
    serial_thread = SerialReaderThread()
    serial_thread.new_message.connect(w.result.setText)  # Update the GUI with new serial data
    serial_thread.start()

    w.show()

    def close_app():
        serial_thread.stop()
        app.quit()

    w.closeEvent = lambda event: close_app()

    app.exec()


app()
message_receiver()