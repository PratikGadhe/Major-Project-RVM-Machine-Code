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
        volume_ml INTEGER
    )
''')

# ✅ Insert multiple rows with volume in milliliters
bottle_entries = [
    ("8906017290064", "Bisleri Packaged Drinking Water", "Thin", 30.0, 2000),   # 2 L
    ("8906119860028", "Swaras Mango Juice", "Thick", 40.0, 600),               # 600 ML
    ("8906156540075", "Royal Club Soda", "Thick", 12.0, 300),                  # 300 ML
    ("8908000682641", "Jagira Spice Soda", "Thick", 50.0, 2000),
    ("8906017290033", "Bisleri Packaged Drinking Water", "Thin", 10.0, 500),
    ("8902579304041", "Parle Agro Packaged Drinking Water", "Thin", 7.0, 250)         
]

c.executemany("INSERT INTO bottle_data VALUES (?, ?, ?, ?, ?)", bottle_entries)

conn.commit()
conn.close()

print("✅ Table dropped, recreated, and new bottle data inserted with volume in ml.")
