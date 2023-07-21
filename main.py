from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import re


Window.size = (500, 700)
Builder.load_file("style.kv")


class MyLayout(Widget):
    def number_press(self, number):
        # self.ids.calc_input will get you TextInput
        prior = self.ids.calc_input.text
        # following Regex split string into a list of substring based on +-*/
        prior_split = re.split("[\-+\*/]", prior)

        if prior == "0":
            self.ids.calc_input.text = f'{number}'
        elif prior_split[-1] == "0":
            pass
        else:
            self.ids.calc_input.text = f'{prior}{number}'

    def dot(self):
        prior = self.ids.calc_input.text
        prior_split = re.split("[\-+\*/]", prior)

        if prior[-1] == "+" or prior[-1] == "-" or prior[-1] == "*" or prior[-1] == "/":
            self.ids.calc_input.text = f'{prior}0.'
        elif prior[-1] == ".":
            pass
        else:
            if "." in prior_split[-1]:
                pass
            else:
                self.ids.calc_input.text = f'{prior}.'

    def reverse_sign(self):
        prior = self.ids.calc_input.text
        target = prior[-1]
        if target == "*" or target == "/" or target == "+" or target == "/" or target == "%":
            self.ids.calc_input.text = f'{prior}-'
        elif prior == "0":
            self.ids.calc_input.text = f'-{prior}'

    def math_operate(self, math_symbol):
        prior = self.ids.calc_input.text
        if prior[-1].isnumeric():
            self.ids.calc_input.text = f'{prior}{math_symbol}'

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            self.ids.calc_input.text = str(eval(prior))
        except SyntaxError:
            pass

    def clear(self):
        self.ids.calc_input.text = "0"

    def clear_entry(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]
        if len(self.ids.calc_input.text) == 0:
            self.ids.calc_input.text = "0"


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()


