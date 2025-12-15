from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
import sqlite3
import cv2
import numpy as np
import base64
import os
from datetime import datetime
from database.db_utils import get_db_connection, init_db
from face_recognition.detector import detect_faces
from face_recognition.recognizer import recognize_face, train_recognizer

app = Flask(__name__)

# Ensure the model directory exists
os.makedirs('face_recognition/models', exist_ok=True)

# Initialize database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    conn = get_db_connection()
    courses = conn.execute('SELECT * FROM courses').fetchall()
    conn.close()
    return render_template('courses.html', courses=courses)

@app.route('/add_course', methods=['POST'])
def add_course():
    course_code = request.form['course_code']
    course_name = request.form['course_name']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO courses (course_code, course_name) VALUES (?, ?)',
                 (course_code, course_name))
    conn.commit()
    conn.close()
    
    return redirect(url_for('courses'))

@app.route('/students')
def students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('students.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    student_id = request.form['student_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO students (student_id, first_name, last_name) VALUES (?, ?, ?)',
                 (student_id, first_name, last_name))
    conn.commit()
    conn.close()
    
    return redirect(url_for('students'))

@app.route('/register_face/<int:student_id>', methods=['GET', 'POST'])
def register_face(student_id):
    if request.method == 'POST':
        image_data = request.form['image_data']
        # Remove the data:image/jpeg;base64, part
        image_data = image_data.split(',')[1]
        
        # Convert base64 to image
        image_bytes = base64.b64decode(image_data)
        np_array = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        
        # Save the face encoding
        success = train_recognizer(img, student_id)
        
        if success:
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'error', 'message': 'No face detected or multiple faces detected'})
    
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,)).fetchone()
    conn.close()
    
    return render_template('register_face.html', student=student)

@app.route('/take_attendance/<int:course_id>', methods=['GET'])
def take_attendance(course_id):
    conn = get_db_connection()
    course = conn.execute('SELECT * FROM courses WHERE id = ?', (course_id,)).fetchone()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('take_attendance.html', course=course, students=students, date=today)

@app.route('/recognize_face', methods=['POST'])
def recognize_student():
    image_data = request.form['image_data']
    # Remove the data:image/jpeg;base64, part
    image_data = image_data.split(',')[1]
    
    # Convert base64 to image
    image_bytes = base64.b64decode(image_data)
    np_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    # Recognize the face
    student_id = recognize_face(img)
    
    if student_id:
        conn = get_db_connection()
        student = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,)).fetchone()
        conn.close()
        
        if student:
            return jsonify({
                'status': 'success',
                'student_id': student['id'],
                'student_name': f"{student['first_name']} {student['last_name']}"
            })
    
    return jsonify({'status': 'error', 'message': 'No matching student found'})

@app.route('/record_attendance', methods=['POST'])
def record_attendance():
    course_id = request.form['course_id']
    student_id = request.form['student_id']
    date = request.form['date']
    status = 'present'  # Default status when using face recognition
    
    conn = get_db_connection()
    
    # Check if attendance already recorded
    existing = conn.execute(
        'SELECT * FROM attendance WHERE course_id = ? AND student_id = ? AND date = ?',
        (course_id, student_id, date)
    ).fetchone()
    
    if existing:
        conn.execute(
            'UPDATE attendance SET status = ? WHERE course_id = ? AND student_id = ? AND date = ?',
            (status, course_id, student_id, date)
        )
    else:
        conn.execute(
            'INSERT INTO attendance (course_id, student_id, date, status) VALUES (?, ?, ?, ?)',
            (course_id, student_id, date, status)
        )
    
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success'})

@app.route('/attendance_summary/<int:course_id>', methods=['GET'])
def attendance_summary(course_id):
    date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
    
    conn = get_db_connection()
    course = conn.execute('SELECT * FROM courses WHERE id = ?', (course_id,)).fetchone()
    
    attendance_data = conn.execute('''
        SELECT s.id, s.student_id as roll_number, s.first_name, s.last_name, a.status
        FROM students s
        LEFT JOIN attendance a ON s.id = a.student_id AND a.course_id = ? AND a.date = ?
        ORDER BY s.student_id
    ''', (course_id, date)).fetchall()
    
    conn.close()
    
    return render_template('attendance_summary.html', 
                          course=course, 
                          date=date, 
                          attendance_data=attendance_data)

if __name__ == '__main__':
    app.run(debug=True)
