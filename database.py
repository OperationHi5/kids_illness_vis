import sqlite3


def create_table():
    conn = sqlite3.connect("illness_tracker.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tracker (kidname TEXT, timetaken Text, temp Text, spo2 Text, "
                "treatments Text, notes Text)")
    conn.commit()
    conn.close()


def insert(kidname, timetaken, temp, spo2, treatments, notes):
    conn = sqlite3.connect("illness_tracker.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tracker VALUES (?, ?, ?, ?, ?, ?)", (kidname, timetaken, temp, spo2, treatments, notes))
    conn.commit()
    conn.close()


def view(kidname):
    conn = sqlite3.connect("illness_tracker.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tracker WHERE kidname=?", (kidname,))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(timetaken):
    conn = sqlite3.connect("illness_tracker.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tracker WHERE timetaken=?", (timetaken,))


