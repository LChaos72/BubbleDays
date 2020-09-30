import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyAppDesign(BoxLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.lb = Label()
		self.lb.text = ''
		self.lb.color = (222/255,18/255,237/237,1)
		self.lb.font_size = 20
		
		self.lb.halign = 'center'
		self.lb.valign = 'bottom'
		
		bt = Button()
		bt.text = 'Click to reveal message'
		bt.color = (1,1,1,1)
		bt.halign = 'center'
		bt.valign = 'center'
		bt.background_color = (1,0,0,1)
		bt.background_normal = ''
		
		bt.bind(on_release = self.reveal)
		
		
		self.add_widget(self.lb)
		
		self.add_widget(bt)
	def reveal(self,instance):

		self.lb.text = 'Happy birthday to myself'
		instance.text = 'Surprise!'
        

class practiceApp(App):
	def build (self):
		return MyAppDesign()
if __name__ == '__main__':
	practiceApp().run()
	
		

