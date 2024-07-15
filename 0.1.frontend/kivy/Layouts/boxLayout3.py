from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutApp(App): 
	
	def build(self):

		superBox = BoxLayout(orientation ='vertical')

		HB = BoxLayout(orientation ='horizontal')
		
		btn1 = Button(text ="One")
		btn2 = Button(text ="Two")

		HB.add_widget(btn1)
		HB.add_widget(btn2)


		VB = BoxLayout(orientation ='vertical')

		btn3 = Button(text ="Three")
		btn4 = Button(text ="Four")

		VB.add_widget(btn3)
		VB.add_widget(btn4)

		superBox.add_widget(HB)
		superBox.add_widget(VB)

		return superBox

root = BoxLayoutApp() 
if __name__ == "__main__":
    root.run() 
