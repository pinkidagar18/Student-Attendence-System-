# SVSU Dudhola Navigation System – Enhanced

An advanced, interactive **campus navigation web application** designed for **Shri Vishwakarma Skill University (SVSU), Dudhola**. The system helps students, visitors, and staff easily find buildings, facilities, and routes across the campus using a **Google Maps–like interface**, real-time location tracking, and voice-assisted navigation.

---

## 🚀 Features

### 🗺️ Smart Campus Navigation

* Interactive custom campus map (no external map services)
* Google Maps–style and Satellite view modes
* Clickable buildings with detailed information
* Smooth animated routes between locations

### 📍 Real-Time Location Tracking

* Uses browser **Geolocation API**
* Automatically detects whether the user is on-campus
* Demo & fallback mode for off-campus users

### 🔍 Advanced Search

* Search buildings and locations instantly
* **Voice-based search** using Speech Recognition
* Quick direction button for nearest destinations

### 🧭 Turn-by-Turn Directions

* Step-by-step navigation instructions
* Distance and estimated time calculation
* Multiple transport modes:

  * 🚶 Walking
  * 🚗 Driving
  * 🚲 Cycling
* Route preferences:

  * Fastest
  * Shortest
  * Scenic

### 🔊 Voice Navigation

* Text-to-Speech based voice instructions
* Toggle voice guidance during navigation

### 🏢 Rich Building Information

* Building type, description, and facilities
* Occupancy indicators
* Ratings and opening hours
* **QR code generation** for location sharing

### 🌦️ Weather Simulation

* Live simulated weather updates
* Weather-based route warnings

### 🚨 Emergency Services

* One-tap access to:

  * Campus Security
  * Medical Emergency
  * Fire Emergency

### ♿ Accessibility Support

* High contrast mode
* Large text mode
* Reduced motion
* Voice announcements

---

## 🛠️ Technology Stack

* **Frontend**: HTML5, CSS3, JavaScript (ES6)
* **Framework**: React 18 (via CDN)
* **Styling**: Tailwind CSS
* **Icons**: Google Material Icons
* **Fonts**: Google Fonts (Roboto, Inter)
* **APIs Used**:

  * Geolocation API
  * Speech Synthesis API
  * Web Speech Recognition API

---

## 📂 Project Structure

```
index.html
│
├── Tailwind & Custom CSS styles
├── React Components
│   ├── Map & Buildings
│   ├── Search Box
│   ├── Directions Panel
│   ├── Building Info Popup
│   ├── Emergency Panel
│   └── Accessibility Panel
│
├── Custom React Hooks
│   ├── useGeolocation
│   ├── useVoiceNavigation
│   ├── useWeather
│   └── useNotification
│
└── Utility Functions & Helpers
```

---

## ▶️ How to Run the Project

1. Download or clone the repository
2. Open `index.html` in any modern web browser (Chrome recommended)
3. Allow location access for best experience
4. Start searching and navigating the campus

> ✅ No backend or installation required

---

## 🎓 Use Cases

* New students navigating the campus
* Visitors finding offices, labs, or blocks
* Emergency navigation support
* University demo & presentation
* Final year / internship project

---

## 🌟 Future Enhancements

* Indoor navigation support
* Admin panel for managing buildings
* Real-time crowd data integration
* Backend + database integration
* Mobile app version (PWA / React Native)

---

## 🖼️ Screenshots
### 🔹 Splash & Welcome Screen

* Animated SVSU logo
* University branding with smooth transitions

```
/screenshots/splash-screen.png
```

### 🔹 Interactive Campus Map

* Google Maps–style view
* Satellite mode
* Clickable buildings with hover tooltips

```
/screenshots/campus-map.png
```

### 🔹 Search & Voice Navigation

* Text-based building search
* Voice-enabled search and directions

```
/screenshots/search-voice.png
```

### 🔹 Turn-by-Turn Directions Panel

* Route distance & estimated time
* Walking / Driving / Cycling modes
* Live navigation steps

```
/screenshots/directions-panel.png
```

### 🔹 Building Information Popup

* Occupancy status
* Facilities & opening hours
* QR code for sharing location

```
/screenshots/building-info.png
```

### 🔹 Emergency & Accessibility Features

* Emergency contact panel
* High contrast & large text modes

```
/screenshots/emergency-accessibility.png
```

---

## ✨ What Makes This Project Advanced

* 🚀 Fully frontend-powered **map engine without Google Maps API**
* 🧠 Smart hooks architecture using React
* 🗣️ Voice-enabled navigation & search
* 🌦️ Weather-aware route warnings
* 📍 Real-time location simulation
* ♿ Accessibility-first design
* 🎨 Highly polished UI inspired by Google Maps
* 📱 QR-based location sharing

---

## 👩‍💻 Author

**Pinki**
B.Tech (CSE – AI/ML)
Shri Vishwakarma Skill University

---

## 📜 License

This project is created for **academic and educational purposes**.

---

⭐ If you like this project, feel free to star it and share!
