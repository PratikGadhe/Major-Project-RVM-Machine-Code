import cv2
from pyzbar.pyzbar import decode

def scan_barcode():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        for barcode in decode(frame):
            barcode_data = barcode.data.decode('utf-8')
            cap.release()
            cv2.destroyAllWindows()
            return barcode_data

        cv2.imshow("Scanning... Show barcode to camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None
