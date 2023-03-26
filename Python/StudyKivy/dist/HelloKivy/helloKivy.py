import kivy
#from os.path import join, dirname, exists, abspath
from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

from wolframclient.evaluation import WolframLanguageSession 
from wolframclient.language import wl,wlexpr

#res_path = kivy.resources.resource_paths
#font_msyh = kivy.resources.resource_find("msyh.ttf")

class Wolfram_Kivy(BoxLayout):
	def __init__(self, **kwargs):
		super(Wolfram_Kivy, self).__init__(**kwargs)
		self.add_widget(Button(text='btn 1',on_press=self.btn_pressed))

		cb = CustomBtn()
		#cb.bind(pressed=cb.on_pressed)
		self.add_widget(cb)
		self.add_widget(Button(text='btn 2'))
		self.lable = Label(text = "111111")
		self.add_widget(self.lable)
		#Button(text = "Button",font_name = font_msyh)
		#self.text = str(select)
		#def callback(self,instance):
		#print('The button <%s> is being pressed' % instance.text)
	def btn_pressed(self, instance):
		with WolframLanguageSession() as session:
			select = session.evaluate(wl.RandomInteger(10))
			self.lable.text = str(select)


class CustomBtn(Widget):
     pressed = ListProperty([0, 0])

     def on_touch_down(self, touch):
         if self.collide_point(*touch.pos):
             self.pressed = touch.pos
             # we consumed the touch. return False here to propagate
             # the touch further to the children.
             return True
         return super(CustomBtn, self).on_touch_down(touch)

     def on_pressed(self, instance, pos):
         print ('pressed at {pos}'.format(pos=pos))


class HelloKivyApp(App):
	"""docstring for HelloWorld"""
	def build(self):
		return Wolfram_Kivy()

HelloKivyApp().run()
		
