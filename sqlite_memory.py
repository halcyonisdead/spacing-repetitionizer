import sqlite3

class database_memory:

    def   __init__(mem, db_name="sched.db"):
        mem.conn = sqlite3.connect(db_name)
        mem.cursor = mem.conn.cursor()
        mem.setup_database()
    def setup_database(mem):
        mem.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS schedule(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        topic TEXT NOT NULL,
                        date_started TEXT NOT NULL,
                        firstreview TEXT NOT NULL,
                        secondreview TEXT NOT NULL,
                        thirdreview TEXT NOT NULL,
                        finalreview TEXT NOT NULL
                        )
                    """)
        mem.conn.commit()
    def add_topic(mem, topic, date_started, review_dates):
        mem.cursor.execute("""
            INSERT INTO schedule (topic, date_started, firstreview, secondreview, thirdreview, finalreview)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (topic, str(date_started), str(review_dates[0]), str(review_dates[1]), str(review_dates[2]), str(review_dates[3])))
        mem.conn.commit()
    def get_all_topics(mem):
        mem.cursor.execute("SELECT * FROM schedule ORDER BY date_started desc")
        return mem.cursor.fetchall()

        
    def close(mem):
        mem.conn.close

        