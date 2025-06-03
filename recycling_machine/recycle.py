import sqlite3
from barcode_scanner import scan_barcode
from arduino_comm import send_open_signal

scanned_bottles = []

def get_bottle_data(barcode):
    conn = sqlite3.connect('bottle_database.db')
    c = conn.cursor()
    c.execute("SELECT barcode, reward, brand, type FROM bottle_data WHERE barcode = ?", (barcode,))
    result = c.fetchone()
    conn.close()
    return result

def calculate_total_reward(bottles):
    return sum(float(bottle['reward']) for bottle in bottles)

def main():
    print("♻️ Welcome to the Plastic Recycling Machine ♻️")
    num_bottles = int(input("Enter number of bottles to recycle: "))

    for i in range(num_bottles):
        print(f"\n📷 Scanning bottle {i + 1} of {num_bottles}...")
        barcode = scan_barcode()

        if barcode:
            print(f"✅ Barcode detected: {barcode}")
            bottle_data = get_bottle_data(barcode)

            if bottle_data:
                barcode, reward, brand, bottle_type = bottle_data
                print(f"✔️ Valid bottle! Brand: {brand}, Type: {bottle_type}, Reward: ₹{reward}")
                scanned_bottles.append({'barcode': barcode, 'reward': reward, 'brand': brand, 'type': bottle_type})
                send_open_signal()
            else:
                print("❌ Invalid barcode. Bottle not recognized.")
        else:
            print("⚠️ No barcode detected.")

    total = calculate_total_reward(scanned_bottles)
    print("\n✅ Recycling complete!")
    print("🧾 Receipt:")
    for bottle in scanned_bottles:
        print(f"- {bottle['brand']} ({bottle['type']}): ₹{bottle['reward']}")
    print(f"💰 Total Reward: ₹{total:.2f}")

if __name__ == '__main__':
    main()
