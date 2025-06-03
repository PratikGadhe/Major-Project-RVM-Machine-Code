import tkinter as tk
from tkinter import messagebox
from barcode_scanner import scan_barcode
from arduino_comm import send_open_signal  # ✅ Correctly import the function
import sqlite3
from PIL import Image, ImageTk
import qrcode
import threading

scanned_bottles = []

def get_bottle_data(barcode):
    conn = sqlite3.connect('bottle_database.db')
    c = conn.cursor()
    c.execute("SELECT barcode, brand, type, actual_price, volume_ml FROM bottle_data WHERE barcode = ?", (barcode,))
    result = c.fetchone()
    conn.close()
    return result

class RecyclingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plastic Recycling Machine")
        self.bottle_count = 0
        self.current_bottle = 0
        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="♻️ Welcome to the Plastic Recycling Machine ♻️", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Start Recycling", font=("Arial", 14), command=self.enter_bottle_count).pack(pady=10)

    def enter_bottle_count(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter number of bottles to recycle:", font=("Arial", 14)).pack(pady=10)
        self.bottle_entry = tk.Entry(self.root, font=("Arial", 14))
        self.bottle_entry.pack(pady=10)
        tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.start_scanning).pack(pady=10)

    def start_scanning(self):
        try:
            self.bottle_count = int(self.bottle_entry.get())
            if self.bottle_count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        self.current_bottle = 0
        scanned_bottles.clear()
        self.scan_next_bottle()

    def scan_next_bottle(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Scanning bottle {self.current_bottle + 1} of {self.bottle_count}", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="Simulate Scan", font=("Arial", 14), command=self.simulate_scan).pack(pady=10)

    def simulate_scan(self):
        barcode = scan_barcode()
        if barcode:
            bottle_data = get_bottle_data(barcode)
            if bottle_data:
                barcode, brand, bottle_type, actual_price, volume_ml = bottle_data

                # 💰 Reward logic based on type and volume
                if bottle_type.lower() == "thin":
                    rate_per_ml = 0.003
                elif bottle_type.lower() == "thick":
                    rate_per_ml = 0.005
                else:
                    rate_per_ml = 0.004

                reward = round(volume_ml * rate_per_ml, 2)

                scanned_bottles.append({
                    'barcode': barcode,
                    'brand': brand,
                    'type': bottle_type,
                    'volume': volume_ml,
                    'actual_price': actual_price,
                    'reward': reward
                })

                # ✅ Correctly send signal to Arduino using external function
                threading.Thread(target=send_open_signal).start()

                messagebox.showinfo("Valid Bottle",
                    f"✔️ Brand: {brand}\nType: {bottle_type}\nVolume: {volume_ml}ml\nReward: ₹{reward}\n\nPlease insert the bottle into the machine.")
            else:
                messagebox.showerror("Invalid Bottle", "❌ Bottle not recognized in our database.")
        else:
            messagebox.showwarning("Scan Failed", "⚠️ No barcode detected.")

        self.current_bottle += 1
        if self.current_bottle < self.bottle_count:
            self.scan_next_bottle()
        else:
            self.show_calculating_screen()

    def show_calculating_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="⚙️ Calculating your reward...", font=("Arial", 16)).pack(pady=40)
        self.root.after(2000, self.show_receipt_screen)

    def show_receipt_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="🎉 Thanks for Recycling!", font=("Arial", 18, "bold")).pack(pady=10)

        total_reward = sum(bottle['reward'] for bottle in scanned_bottles)

        receipt_frame = tk.Frame(self.root)
        receipt_frame.pack(pady=10)

        for bottle in scanned_bottles:
            info = (
                f"• {bottle['brand']} ({bottle['type']}, {bottle['volume']}ml): "
                f"Price: ₹{bottle['actual_price']} | Reward: ₹{bottle['reward']}"
            )
            tk.Label(receipt_frame, text=info, font=("Arial", 12)).pack(anchor="w")

        tk.Label(self.root, text=f"\n💰 Total Reward: ₹{total_reward:.2f}", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(self.root, text="Generate QR Code", font=("Arial", 12), command=lambda: self.generate_qr_code(total_reward)).pack(pady=5)

        tk.Label(self.root, text="Published by Pratik Gadhe | Anushka Dhawale | Harshvardhini Bhadane | Om Jadhav", font=("Arial", 10), fg="gray").pack(side="bottom", pady=10)

    def generate_qr_code(self, total_reward):
        qr_data = f"Reward: ₹{total_reward:.2f}"
        qr = qrcode.make(qr_data)
        qr.save("reward_qr.png")

        qr_img = Image.open("reward_qr.png")
        qr_img = qr_img.resize((150, 150))
        qr_photo = ImageTk.PhotoImage(qr_img)

        qr_window = tk.Toplevel(self.root)
        qr_window.title("QR Code")
        tk.Label(qr_window, text="Scan to Claim Your Reward", font=("Arial", 14)).pack(pady=10)
        tk.Label(qr_window, image=qr_photo).pack()
        qr_window.qr_photo = qr_photo  # Prevent garbage collection

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1800x900")
    app = RecyclingApp(root)
    root.mainloop()
