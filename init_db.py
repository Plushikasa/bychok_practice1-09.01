import sqlite3

# ---------- 1. ПОДКЛЮЧЕНИЕ ----------
conn = sqlite3.connect('app.db')

# ---------- 2. СОЗДАНИЕ КУРСОРА ----------
cursor = conn.cursor()

# ---------- 3. ВЫПОЛНЕНИЕ DDL ----------
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id     INTEGER PRIMARY KEY,
        title  TEXT NOT NULL,
        status TEXT DEFAULT 'new'
    )
""")

# ---------- 4. ФИКСАЦИЯ (COMMIT) ----------
conn.commit()

# ---------- 5. ЗАКРЫТИЕ СОЕДИНЕНИЯ ----------
conn.close()

print("База данных и таблица tasks успешно созданы.")