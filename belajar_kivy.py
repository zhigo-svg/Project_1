import kivy
from kivy.app import App
from kivy.uix.label import Label

class myapp(App):
    def build(self):
        return Label(font_size=28,color="red",text="Hello World")
        
if __name__ == '__main__':
    myapp().run()