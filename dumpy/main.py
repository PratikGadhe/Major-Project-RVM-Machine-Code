import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

# Global image references to prevent garbage collection
image_references = []

# ----------------------
# List of valid user codes
valid_codes = ["1234", "5678", "9999"]  # You can add or load from DB
# ----------------------

# ---------- Sign-Up Website ----------
def open_signup_website():
    webbrowser.open("https://your-recycle-app.com")  # Replace with actual URL

# ---------- Final Window for Bottle/Can Entry ----------
def open_bottle_entry_window():
    bottle_window = tk.Toplevel()
    bottle_window.title("Bottle/Can Entry")
    bottle_window.geometry("1440x900")

    bg_image_path = "/Users/pratikvilasgadhe/Desktop/Programming/Python/Technocave_Project/background.jpg"
    bg_image = Image.open(bg_image_path).resize((1440, 900), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    image_references.append(bg_photo)

    bg_label = tk.Label(bottle_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Heading
    heading = tk.Label(bottle_window,
                       text="Enter Number of Bottle / Can To Recycle",
                       font=("Helvetica", 22, "bold"),
                       fg="white", bg="black")
    heading.place(relx=0.5, rely=0.3, anchor="center")

    # Entry box
    bottle_entry = tk.Entry(bottle_window,
                            font=("Helvetica", 20),
                            justify='center',
                            width=10)
    bottle_entry.place(relx=0.5, rely=0.4, anchor="center")

    # Submit button
    def handle_bottle_submit():
        num_bottles = bottle_entry.get()
        print("Number of bottles entered:", num_bottles)
        # You can now move to camera scanning or next step

    submit_btn = tk.Button(bottle_window,
                           text="Proceed",
                           font=("Helvetica", 16),
                           bg="#007acc", fg="black",
                           padx=20, pady=10,
                           command=handle_bottle_submit)
    submit_btn.place(relx=0.5, rely=0.5, anchor="center")

# ---------- Code Entry Window ----------
def open_second_window():
    second_window = tk.Toplevel()
    second_window.title("Recycle Coin Login")
    second_window.geometry("1440x900")

    bg_image_path = "/Users/pratikvilasgadhe/Desktop/Programming/Python/Technocave_Project/background.jpg"
    bg_image = Image.open(bg_image_path).resize((1440, 900), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    image_references.append(bg_photo)

    bg_label = tk.Label(second_window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Title
    title = tk.Label(second_window,
                     text="ENTER YOUR 4-DIGIT CODE TO GET RECYCLE COINS",
                     font=("Helvetica", 22, "bold"),
                     fg="#003366", bg="#e6f2ff")
    title.pack(pady=60)

    code_entry = tk.Entry(second_window,
                          font=("Helvetica", 20),
                          justify='center',
                          width=10,
                          show="*")
    code_entry.pack(pady=10)

    # Submit code logic
    def handle_code_submit():
        user_code = code_entry.get()
        if user_code in valid_codes:
            print("Valid code:", user_code)
            open_bottle_entry_window()
        else:
            error_label.config(text="Invalid code. Try again.", fg="red")

    # Submit button
    code_btn = tk.Button(second_window,
                         text="Submit Code",
                         font=("Helvetica", 16),
                         bg="#007acc", fg="black",
                         padx=20, pady=10,
                         command=handle_code_submit)
    code_btn.pack(pady=20)

    # Error label
    error_label = tk.Label(second_window, text="", font=("Helvetica", 14), bg="#e6f2ff")
    error_label.pack()

    # Promo
    promo = tk.Label(second_window,
                     text="WANT TO BE A RECYCLE WARRIOR?\nSIGN UP AND GET RECYCLE PRODUCTS FREE!",
                     font=("Helvetica", 16),
                     fg="#004d00", bg="#e6f2ff")
    promo.pack(pady=30)

    # Sign Up Button
    signup_btn = tk.Button(second_window,
                           text="Sign Up",
                           font=("Helvetica", 16),
                           bg="#28a745", fg="black",
                           padx=20, pady=10,
                           command=open_signup_website)
    signup_btn.pack(pady=10)

    # Skip Button
    skip_btn = tk.Button(second_window,
                         text="Skip",
                         font=("Helvetica", 14),
                         bg="#6c757d", fg="black",
                         padx=15, pady=8,
                         command=open_bottle_entry_window)
    skip_btn.pack(pady=10)

# ---------- Main Window ----------
window = tk.Tk()
window.title("Recycling Machine Interface")
window.geometry("1440x900")

bg_image_path = "/Users/pratikvilasgadhe/Desktop/Programming/Python/Technocave_Project/background.jpg"
bg_image = Image.open(bg_image_path).resize((1440, 900), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
image_references.append(bg_photo)

bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(window,
                       text="WELCOME TO PLASTIC/CAN RECYCLING MACHINE",
                       font=("Helvetica", 24, "bold"),
                       fg="white", bg="black")
title_label.place(relx=0.5, y=50, anchor="center")

start_button = tk.Button(window,
                         text="Start Recycling",
                         font=("Helvetica", 16),
                         bg="#28a745", fg="black",
                         padx=20, pady=10,
                         command=open_second_window)
start_button.place(relx=0.5, rely=0.5, anchor="center")

footer_label = tk.Label(window,
                        text="Published by: Pratik Gadhe | Anushka Dhawale | Om Jadhav | Harshvardhini Bhadane",
                        font=("Helvetica", 12),
                        fg="white", bg="black")
footer_label.place(relx=0.5, rely=0.95, anchor="center")

window.mainloop()
