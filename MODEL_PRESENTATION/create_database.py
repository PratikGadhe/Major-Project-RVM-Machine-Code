import sqlite3

# Create or connect to the database
conn = sqlite3.connect('barcode_rewards.db')
cursor = conn.cursor()

# Create a single table for all bottles with an extra 'type' column
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bottle_data (
        barcode TEXT PRIMARY KEY,
        reward INTEGER,
        brand TEXT,
        type TEXT  -- 'thin' or 'thick'
    )
''')

# Sample data (barcode, reward, brand, type)
sample_data = [
    ('8901234567890', 10, 'Bisleri', 'thin'),
    ('8909876543210', 20, 'Sprite', 'thick'),
    ('8901112223334', 10, 'Aquafina', 'thin'),
    ('8905554443332', 20, 'Pepsi', 'thick'),
    ('8902442220232',10,'Youva','thin'),
    ('8904035416282',25,'Joy Sunscreen','thick'),
    ('8901765126122',4,'XO Huaser pen','thick'),
    ('8902442220225',15,'Youva','thin'),
    ('8901324051599',15,'Apsara nootbook','thin'),
    ('8901491103084',16,'Kurkure','thin'),
    ('8906119860028',10,'Mango Juice','thin')
]

# Insert the sample data
cursor.executemany('INSERT OR REPLACE INTO bottle_data VALUES (?, ?, ?, ?)', sample_data)

conn.commit()
conn.close()

print("✅ Database and unified table created successfully with sample data!")
