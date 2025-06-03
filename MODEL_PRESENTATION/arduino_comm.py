import serial
import time

def send_open_signal():
    try:
        arduino = serial.Serial('/dev/tty.usbserial-1120', 9600)  # Change port if needed
        time.sleep(2)
        arduino.write(b'1')
        print("🟢 Box opening signal sent to Arduino")
        arduino.close()
    except Exception as e:
        print("⚠️ Error communicating with Arduino:", e)
