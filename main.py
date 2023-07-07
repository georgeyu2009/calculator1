from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (500, 700)
Builder.load_file("style.kv")

class MyLayout(Widget):

    def press(self):
        self.ids.calc_input.text = "0"



class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()


