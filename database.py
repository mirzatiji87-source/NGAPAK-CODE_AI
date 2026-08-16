import sqlite3
from config import DB_NAME

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bahasa TEXT NOT NULL,
            level TEXT NOT NULL,
            buggy_code TEXT NOT NULL,
            fixed_code TEXT NOT NULL,
            hint TEXT NOT NULL
        )
        """)
    conn.commit()
    conn.close()

def create_question(bahasa, level, buggy_code, fixed_code, hint):
    conn = get_connection()
    conn.execute(
        "INSERT INTO questions (bahasa, level, buggy_code, fixed_code, hint) VALUES (?, ?, ?, ?, ?)",
        (bahasa, level, buggy_code, fixed_code, hint)
    )
    conn.commit()
    conn.close()

def read_questions(bahasa=None, level=None):
    conn = get_connection()
    query = "SELECT * FROM questions WHERE 1=1" 
    params = []
    
    if bahasa:
        query += " AND bahasa = ?"
        params.append(bahasa)
        
    if level:
        query += " AND level = ?"
        params.append(level)
        
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return rows

def get_question_by_id(qid):
    conn = get_connection()
    row = conn.execute("SELECT * FROM questions WHERE id = ?", (qid,)).fetchone()
    conn.close()
    return row

def delete_question(qid):
    conn = get_connection()
    conn.execute("DELETE FROM questions WHERE id = ?", (qid,))
    conn.commit()
    conn.close()
    
def update_question(qid, bahasa, level, buggy_code, fixed_code, hint):
    conn  = get_connection()
    conn.execute(
        """UPDATE questions
            SET bahasa = ?, level = ?, buggy_code = ?, fixed_code = ?, hint = ?
            WHERE id = ?""",
            (bahasa, level, buggy_code, fixed_code, hint, qid)
    )
    conn.commit()
    conn.close()
