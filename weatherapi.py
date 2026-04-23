import sys
import requests
import os
from dotenv import load_dotenv
load_dotenv()
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QLineEdit,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt 



class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
      
        self.setWindowTitle("Weather")
        self.setWindowIcon(QIcon("image.png"))
        self.wel=QLabel("Enter the City",self)
        self.location=QLineEdit(self)
        self.display1=QLabel(self)
        self.display2=QLabel(self)
        self.display3=QLabel(self)
        self.get_weather=QPushButton("Get Weather",self)
        self.initUI()

    def initUI(self):
      
          vbox=QVBoxLayout()
          vbox.addWidget(self.wel)
          vbox.addWidget(self.location)
          vbox.addWidget(self.get_weather,alignment=Qt.AlignCenter)
          vbox.addWidget(self.display1)
          vbox.addWidget(self.display2)
          vbox.addWidget(self.display3)

          self.wel.setObjectName("start")
          self.display1.setObjectName("emoji")
          self.display2.setObjectName("temp")
          self.display3.setObjectName("description")

          self.setStyleSheet("""QLineEdit{
                             font-size: 20px;
                             color:black;
                             font-family:Arial;}

                             QLabel#start{
                             font-size:30px;
                             color:black;
                             font-weight:Bold;}

                             QLabel#emoji{
                             font-size:100px;
                             font:"Segoe UI Emoji";}
                             
                             QLabel#temp{
                             font-size:30px;
                             color:blue;
                             font-weight:Bold;}

                             QLabel#description{
                             font-size:20px;
                             color:black;
                            }""")
          
          self.location.setMaximumSize(320,60)
          self.get_weather.setMaximumSize(120,50)
          self.location.setMinimumSize(320,60)
          self.get_weather.setMinimumSize(120,50)
          self.wel.setAlignment(Qt.AlignCenter)
          self.location.setAlignment(Qt.AlignCenter)
          self.display1.setAlignment(Qt.AlignCenter)
          self.display2.setAlignment(Qt.AlignCenter)
          self.display3.setAlignment(Qt.AlignCenter)

          self.setLayout(vbox)
          self.location.setPlaceholderText("Enter city or auto detected...")

          self.get_weather.clicked.connect(self.fetch_weather)
          self.location.returnPressed.connect(self.fetch_weather)

          city=self.auto_location()
          if city:
               self.location.setText(city)
            
           

    def fetch_weather(self):
   
        api_key= os.getenv("OPENWEATHER_API_KEY")
        city=self.location.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try: 
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()
          
            if str(data["cod"])=="200":
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
         
            match response.status_code:
                 case 400:
                      self.display_error("bad request:\nPlease check input")
                 case 401:
                      self.display_error("unauthorized:\nPlease check api key")
                 case 403:
                      self.display_error("forbiddden\naccess denied")
                 case 404:
                      self.display_error("no data \nplease enter a valid city")
                 case 500:
                      self.display_error("internal server error\nPlease try again later")
                 case 503:
                      self.display_error("service unavailable \nserver is down")
                 case 504:
                      self.display_error("Gateway timeout\n No response from the server")
                 case 502:
                      self.display_error("bad request\nInvalid response from the server")
                    
                 case _:
                      self.display_error(f"http error occured{http_error}")
                 
        except requests.exceptions.ConnectionError:
                
            
                self.display_error("connection error\n check your internt connection")
        except requests.exceptions.Timeout:
                
            
                self.display_error("timeout error\n The request timed out")
        except requests.exceptions.TooManyRedirects:
                
            
                self.display_error("Too many redirects \n check the URL")
        except requests.exceptions.RequestException as req_error:
                
            
                self.display_error(f"Request Error\n{req_error}")
      
    def display_error(self,message):
        self.display1.setStyleSheet("font-size:30px;")
        self.display1.setText("")
        self.display2.setText("")
        self.display3.setText(message)
    def display_weather(self,data):
     
        tempr=data["main"]["temp"]

        self.display2.setText(f"{tempr-273.15:.1f}°c")
        weather_description=data["weather"][0]["description"]
        weather_id=data["weather"][0]["id"]
        self.display3.setText(weather_description)
       
        self.display1.setText(self.weather_emoji(weather_id))
    @staticmethod
    def weather_emoji(weather_id):
         if weather_id<233 and weather_id>=200:
              return("⛈️")

         elif weather_id<322 and weather_id>=300:
              return("🌦️")
       
         elif weather_id<532 and weather_id>=500:
              return("🌧️")
         elif weather_id<623 and weather_id>=600:
             return("❄️")
         elif 701 <= weather_id <= 781:
              return"🌫️"
         elif weather_id==800:
             return("☀️")
         elif weather_id<805 and weather_id>800:
             return("☁️")

         else:
             return("❓")
         
    def auto_location(self):
         try:
              response=requests.get("http://ip-api.com/json/")
              data=response.json()
              city=data.get("city")
              return city
         except requests.exceptions.RequestException:
              return None
def main():
    app=QApplication(sys.argv)
    window=Mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()