# 🎓 Student Attendance System (Face Recognition Based)

## 📌 Project Analysis

The **Student Attendance System** is a smart web-based application that automates attendance marking using **Face Recognition technology**. Instead of manual attendance, the system detects and recognizes student faces through a camera and records attendance directly into a database.

From your project structure and files, the system is built using **Python (Flask framework)** with a clear separation of backend logic, face recognition modules, database handling, and frontend UI.

### 🔍 Key Observations from the Project

* Uses **Flask** for backend routing and server logic
* Implements **Face Detection & Recognition** using OpenCV-based models
* Stores attendance records in a **SQLite database**
* Has a clean **MVC-like structure** (routes, models, templates, static files)
* Provides separate UI pages for:

  * Student registration
  * Face registration
  * Attendance capture
  * Attendance summary

This makes the project **academically strong** and **industry-relevant**, especially for AI/ML and Computer Vision roles.

---

## 🚀 Features

* 👤 Student registration and management
* 📸 Face registration using webcam
* 🧠 Face recognition–based attendance marking
* 📊 Attendance summary and reports
* 🗄️ SQLite database for storing attendance data
* 🌐 Web-based interface using HTML, CSS & JavaScript

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* OpenCV
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript

### Tools & Libraries

* NumPy
* OpenCV (cv2)
* Flask Templates (Jinja2)

---

## 📂 Project Structure

```
attendance_system/
│── app.py
│── requirements.txt
│── attendance.db
│
├── database/
│   ├── db_utils.py
│   └── models.py
│
├── face_recognition/
│   ├── detector.py
│   ├── recognizer.py
│   └── models/
│       ├── trainer.yml
│       └── label_map.pkl
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       ├── camera.js
│       └── main.js
│
└── templates/
    ├── index.html
    ├── register_face.html
    ├── take_attendance.html
    ├── attendance_summary.html
    ├── students.html
    └── courses.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/pinkidagar18/Student-Attendence-System-.git
cd attendance_system
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
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

## 🧪 How It Works

1. Admin registers students in the system
2. Student faces are captured and trained
3. Camera detects faces in real-time
4. Recognized students are marked present
5. Attendance is saved in the database
6. Summary can be viewed anytime

---

## 📈 Use Cases

* Schools & Colleges
* Universities
* Training institutes
* Smart classroom systems

---

## 🔮 Future Enhancements

* Cloud database integration
* Admin authentication & roles
* CSV/PDF attendance export
* Mobile app integration
* Real-time analytics dashboard

---

## 👩‍💻 Author

**Pinki Dagar**
B.Tech (CSE – AI/ML)

---

## ⭐ Support

If you find this project useful, don’t forget to ⭐ star the repository!
