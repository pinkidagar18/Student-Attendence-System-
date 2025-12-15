import sqlite3

def get_db_connection():
    """Create a connection to the SQLite database"""
    conn = sqlite3.connect('attendance.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database by creating tables if they don't exist"""
    conn = get_db_connection()
    
    # Create courses table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_code TEXT NOT NULL UNIQUE,
        course_name TEXT NOT NULL
    )
    ''')
    
    # Create students table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL UNIQUE,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        face_encoding TEXT
    )
    ''')
    
    # Create attendance table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        status TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (course_id) REFERENCES courses (id),
        FOREIGN KEY (student_id) REFERENCES students (id)
    )
    ''')
    
    conn.commit()
    conn.close()