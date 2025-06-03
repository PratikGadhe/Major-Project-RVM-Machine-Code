import sqlite3

conn = sqlite3.connect('bottle_database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS bottle_data (
    barcode TEXT PRIMARY KEY,
    reward TEXT,
    brand TEXT,
    type TEXT
)
''')

sample_data = [
    ('123456789012', '5.0', 'Bisleri', 'Thin'),
    ('987654321098', '7.0', 'Kinley', 'Thick'),
    ('555555555555', '6.0', 'Aquafina', 'Thin'),
    ('8901491103084',16,'Kurkure','thin')
]

c.executemany("INSERT OR IGNORE INTO bottle_data VALUES (?, ?, ?, ?)", sample_data)
conn.commit()
conn.close()

print("✅ Database setup complete.")
