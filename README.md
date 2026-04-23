# 🌤️ Weather App

A Python desktop weather app that shows real-time weather data with auto location detection and emoji icons.

---

## ✨ Features

- 🌍 **Auto location detection** — automatically detects your city on launch
- 🌡️ **Real-time weather data** — fetches live temperature, description and weather condition
- 😎 **Emoji icons** — visual weather representation using emojis
- ⚠️ **Error handling** — handles network errors, invalid cities and API errors gracefully
- ⌨️ **Keyboard support** — press Enter to fetch weather without clicking the button

---

## 🖥️ Preview

> Search for any city or let the app auto-detect your location!

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **PyQt5** — Desktop GUI
- **OpenWeatherMap API** — Weather data
- **ip-api** — Auto location detection
- **python-dotenv** — Environment variable management

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/akshit2s/weather-app.git
cd weather-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
- Get a free API key from [openweathermap.org](https://openweathermap.org/api)
- Create a `.env` file in the project folder:
```
OPENWEATHER_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
python weatherapi.py
```

---

## 📁 Project Structure

```
weather-app/
├── weatherapi.py       # Main application file
├── weathericon.png     # App window icon
├── requirements.txt    # Project dependencies
├── .env                # API key (not pushed to GitHub)
└── .gitignore          # Ignored files
```

---

## 📦 Requirements

```
PyQt5
requests
python-dotenv
```

---

## 🙏 Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for the weather API
- [ip-api](http://ip-api.com/) for the IP-based location detection

---

## 👤 Author

**Akshit**  
GitHub: [@akshit2s](https://github.com/akshit2s)