# 🎓 Face Recognition Based Attendance System

An intelligent **Flask-based Attendance Management System** that uses **Face Recognition** to automatically record student attendance. This project eliminates manual attendance, reduces proxy issues, and provides an efficient way to manage courses, students, and attendance records.

---

## 🚀 Project Overview

This application allows:

* 📚 Course management
* 👨‍🎓 Student management
* 📸 Face registration for each student
* 🧠 Face recognition using OpenCV
* ✅ Automatic attendance marking
* 📊 Attendance summary by date & course

The system captures images through a webcam, recognizes students using trained facial data, and records attendance in a SQLite database.

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite3
* **Computer Vision:** OpenCV
* **Machine Learning:** Face recognition model
* **Others:** NumPy, Base64

---

## 📁 Project Structure

```bash
attendance_system/
│
├── app.py                     # Main Flask application
├── database/
│   └── db_utils.py             # Database connection & initialization
├── face_recognition/
│   ├── detector.py             # Face detection logic
│   ├── recognizer.py           # Face recognition & training
│   └── models/                 # Trained face models
├── templates/
│   ├── index.html
│   ├── courses.html
│   ├── students.html
│   ├── register_face.html
│   ├── take_attendance.html
│   └── attendance_summary.html
├── static/
│   └── css / js / images
└── README.md
```

---

## ✨ Features

### 📘 Course Management

* Add and view courses

### 👩‍🎓 Student Management

* Add students with roll number & name

### 📸 Face Registration

* Capture student face using webcam
* Train face recognition model
* Supports validation (single face detection)

### 🧠 Face Recognition

* Recognizes registered students
* Matches face with trained data

### ✅ Attendance System

* Automatic attendance marking
* Prevents duplicate attendance
* Attendance status stored as **Present**

### 📊 Attendance Summary

* View attendance by course and date
* Displays student-wise attendance status

---

## 🔄 Application Flow

1. Add **Courses**
2. Add **Students**
3. Register **Student Face**
4. Select course & date
5. Capture image → Face Recognition
6. Attendance recorded automatically
7. View attendance summary

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/face-recognition-attendance.git
cd face-recognition-attendance
```

### 2️⃣ Install Dependencies

```bash
pip install flask opencv-python numpy
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Database Used

* **SQLite3**
* Tables:

  * `students`
  * `courses`
  * `attendance`

Database is automatically initialized on first run.

## 🔒 Security & Validation

* Single face detection check
* Duplicate attendance prevention
* Server-side validation

---

## 🌟 Future Enhancements

* 📱 Mobile-friendly UI
* 🔐 Admin authentication
* 📈 Attendance analytics
* 📤 Export attendance to CSV/PDF
* ☁️ Cloud database integration
* 🎥 Live camera stream recognition

---

## 👩‍💻 Author

**Pinki Dagar**
B.Tech CSE (AI/ML) Student

---

## 📄 License

This project is for **academic and learning purposes**.

---

✨ *Smart Attendance using AI & Face Recognition* ✨

