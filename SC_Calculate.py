import sys
from PyQt6.QtWidgets import (QApplication ,QMainWindow , QLabel , QLineEdit , QPushButton , QGraphicsView , QGraphicsScene)
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie
import random

gifs = (
    "animation/pizza.gif",
    "animation/dance_cate.gif",
    "animation/eats_cate.gif"
)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("UI/appUI.ui" , self)
        
        self.windowTitle = "SC_Calculate.exe"
        
        if not gifs is None and len(gifs) > 0:
            self.scene = QGraphicsScene()
            self.graphics_gif.setScene(self.scene)
        
            self.movie = QMovie(gifs[random.randint(0 , len(gifs)-1)])
            self.movie.setCacheMode(QMovie.CacheMode.CacheAll)
        
            self.label = QLabel()
            self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.label.setMovie(self.movie)
        
            self.proxy = self.scene.addWidget(self.label)
        
            self.resizeEvent = self.on_resize
            but = QPushButton()
            
            self.line_price.returnPressed.connect(self.focus_amount_line)
            self.line_amount.returnPressed.connect(self.button_click)
            
            self.button_calculate.pressed.connect(self.button_click)
            
            self.movie.start()
            
    def focus_amount_line(self):
        self.line_amount.setFocus()
    
    
    def valid(self):
        amount = self.line_amount.text().replace(" " , "")
        price = self.line_price.text().replace(" " , "")
        if len(amount) and len(price):
            try:
                self.amount = float(amount)
                self.price = float(price)
                return True
            except ValueError:
                self.label_output_value.setText("ТО ЧТО ТЫ НАКАЛЯКАЛ\nНЕ ЯВЛЯЕТСЯ ЧИСЛОМ :(")
                return False
        else:
            self.label_output_value.setText("Я ТЕБЕ НЕ МЕДИУМ\nПО ПУСТОТЕ УГАДЫВАТЬ\nНЕ УМЕЮ :(")

    def button_click(self):
        valid = self.valid()
        if valid and not valid is None:
            output = str(self.price / self.amount)
            self.label_output_value.setText(f"{self.line_output_this_float(output)} x {self.amount}")
    
    def line_output_this_float(self , output:str):
        
        intPart , floatPart = output.split('.',1)
        
        floatPart = floatPart[0:2]
        
        if len(intPart) > 3:
            formInt = self.format_output_value(intPart)
            return f"{formInt}.{floatPart}"
        else:
            return f"{intPart}.{floatPart}"    
        
            
    def format_output_value(self , output:str):
        if len(output)<=3:
            return output
        
        parts = []
        for i in range(len(output) , 0 , -3):
            start = max(0 ,i - 3)
            parts.append(output[start:i])
        
        return " ".join(parts[::-1])
    
    def on_resize(self , event):
        view_size = self.graphics_gif.size()
        if not self.movie.currentPixmap().isNull():
            pixmap_size = self.movie.currentPixmap().size()
            scale = min((view_size.width()*0.97) / pixmap_size.width(),
                        (view_size.height()*0.97) / pixmap_size.height())
            self.proxy.setScale(scale)
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()
    
    sys.exit(app.exec())       