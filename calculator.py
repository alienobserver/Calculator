# Calculator App
# install python kivy with $ pip install kivy

from kivy.app import App
from kivy.config import Config

# Size of app
width = 350
height = 500

Config.set( 'graphics', 'resizable' , False )
Config.set( 'graphics', 'width' , width )
Config.set( 'graphics', 'height' , height )

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window

from math import sqrt, sin, cos, tan, radians
from mpmath import cot, pi
import os, sys

Window.clearcolor = (0.1, 0.1, 0.1, 1)

# sin, cos, tan, cot function for degrees
def sinA(deg):
    return sin(radians(deg))

def cosA(deg):
    return cos(radians(deg))

def tanA(deg):
    return tan(radians(deg))

def cotA(deg):
    return cot(radians(deg))

# The main class
class CalculatorApp(App):
    # calculate the result in label if theres an error return message
    def calc_result(self, instance):
        try:
            self.lb.text = str(eval(self.lb.text))

        except ZeroDivisionError:
            self.formula = "Can\'t divide by 0"
            self.lb.text = self.formula

        except SyntaxError:
            self.formula = "Wrong Expression"
            self.lb.text = self.formula

        except ValueError:
            self.formula = "Wrong Expression"
            self.lb.text = self.formula

        else:
            self.formula = "0"

    def update_label(self):
        self.lb.text  = self.formula

    def add_number(self, instance):
        # Clear the label before adding nums
        if self.formula == "0" or self.formula == "Wrong Expression" or self.formula == "Can\'t divide by 0":
            self.formula = ""

        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        # Clear the label before adding opers
        if self.formula == "0" or self.formula == "Wrong Expression" or self.formula == "Can\'t divide by 0":
            self.formula = ""

        # Translate the needed words to functions
        if str(instance.text).lower() == "x":
            self.formula += '*'

        elif str(instance.text).lower() == "^":
            self.formula += '**'

        elif str(instance.text).lower() == "√":
            self.formula += 'sqrt('

        elif str(instance.text).lower() == "sin":
            self.formula += 'sinA('

        elif str(instance.text).lower() == "cos":
            self.formula += 'cosA('

        elif str(instance.text).lower() == "tan":
            self.formula += 'tanA('

        elif str(instance.text).lower() == "cot":
            self.formula += 'cotA('

        else:
            self.formula += str(instance.text)

        self.update_label()

    def clear(self, instance):
        self.formula = "0"

    def build(self):
        # Setting icon's path
        self.icon =  (os.path.abspath(os.path.dirname(sys.argv[0])) + "/keys.png").replace("\\", "/")
        self.formula = "0"
        self.colNums = [0.2, 0.2, 0.2, 1]
        self.colOpers = [0.15, 0.15, 0.15, 1]

        #The main Box Layout
        bl = BoxLayout( orientation = 'vertical', padding = [3] )

        # The main gridlayout where are all buttons
        gl = GridLayout( cols = 5, spacing = 3, size_hint = (1, .6) )

        # The main label
        self.lb = Label( text = "0",font_size = 30, halign = "right", valign = "center", size_hint = (1, .4), text_size = (width - 50, height * .4 - 50) , color = [1, 1, 1, 1] )

        # Add The GridLayout and The label to The BoxLayout 
        bl.add_widget( self.lb )
        bl.add_widget( gl )

        # Setting all buttons and adding them to the gridlayout
        gl.add_widget( Button( text = "√", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )
        gl.add_widget( Button( text = "^", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )
        gl.add_widget( Button( text = "(", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )
        gl.add_widget( Button( text = ")", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )
        gl.add_widget( Button( text = "CE", on_press = self.clear, background_color = self.colOpers , background_normal = '' ) )

        gl.add_widget( Button( text = "7", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "8", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "9", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "X", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )
        gl.add_widget( Button( text = "sin", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )

        gl.add_widget( Button( text = "4", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "5", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "6", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "-", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )
        gl.add_widget( Button( text = "cos", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )

        gl.add_widget( Button( text = "1", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "2", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "3", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "+", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )
        gl.add_widget( Button( text = "tan", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )

        gl.add_widget( Button( text = "=", on_press = self.calc_result, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "0", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = ".", on_press = self.add_number, background_color = self.colNums , background_normal = '' ) )
        gl.add_widget( Button( text = "/", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )
        gl.add_widget( Button( text = "cot", on_press = self.add_operation, background_color = self.colOpers , background_normal = '' ) )

        return bl

if __name__ == "__main__":
    CalculatorApp().run()
