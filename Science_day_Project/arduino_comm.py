import serial
import time

def send_open_signal():
    try:
        # Replace 'COM3' with your Arduino port (e.g., 'COM4' on Windows or '/dev/ttyUSB0' on Linux)
        arduino = serial.Serial('/dev/tty.usbserial-1120', 9600, timeout=1)
        time.sleep(2)  # Wait for connection to establish

        arduino.write(b'O')  # Send 'O' as signal to open box
        print("✅ Signal sent to Arduino to open the box.")

        arduino.close()
    except Exception as e:
        print(f"❌ Error sending signal to Arduino: {e}")
