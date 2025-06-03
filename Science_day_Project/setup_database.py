import sqlite3

conn = sqlite3.connect('bottle_database.db')
c = conn.cursor()

# 🔄 Drop old table if it exists (caution: this will delete previous data)
c.execute("DROP TABLE IF EXISTS bottle_data")

# ✅ Create table with all required columns
c.execute('''
    CREATE TABLE bottle_data (
        barcode TEXT PRIMARY KEY,
        brand TEXT,
        type TEXT,
        actual_price REAL,
        quality TEXT
    )
''')

# ✅ Insert multiple rows
bottle_entries = [
    ("8906017290064", "Bisleri Packaged Drinking Water", "Thin",30.0, "2 L"),
    ("8906119860028", "Swaras Mango Juice", "Thick",25.0, "600 ML"),
    ("8906156540075", "Royal Club Soda", "Thick", 15.0, "300 ML"),
    ("8908000682641", "Jagira Spice Soda", "Thick", 40.0, "2.25 L")
]

c.executemany("INSERT INTO bottle_data VALUES (?, ?, ?, ?, ?)", bottle_entries)

conn.commit()
conn.close()

print("✅ Table dropped, recreated, and new bottle data inserted.")
