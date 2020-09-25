from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class calculator(FloatLayout):
    pass	


class MyApp(App):
    def build(self):
        return calculator()

if __name__ == '__main__':
    MyApp().run()
