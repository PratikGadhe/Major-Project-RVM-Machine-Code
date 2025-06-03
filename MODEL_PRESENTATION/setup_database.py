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
    ("123456789012", "Bisleri", "Thick", 20.0, "Large"),
    ("8906119860028", "Mango Juice", "Thin",40.0, "Medium"),
    ("8908002937695", "Pooja Oil", "Thin", 10.0, "Medium"),
    ("987654321098", "Aquafina", "Thin", 10.0, "Medium"),
    ("8908000682641", "Gina's Spicy Soda", "Thin",50.0, "Large"),
    ("8906156540075", "Royal Club Soda", "Thin",15.0, "Small")
]

c.executemany("INSERT INTO bottle_data VALUES (?, ?, ?, ?, ?)", bottle_entries)

conn.commit()
conn.close()

print("✅ Table dropped, recreated, and new bottle data inserted.")
