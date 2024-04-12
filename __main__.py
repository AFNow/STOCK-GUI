import sys
import tkinter
import customtkinter

import yfinance
import pandas
import flask
from functions import add_varuable

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('theme.json')

STOCK_GUI = customtkinter.CTk()
STOCK_GUI.title('STOCK-GUI')
STOCK_GUI.geometry('400x400')


add_btn = customtkinter.CTkButton(master= STOCK_GUI, text= 'Add new', command= add_varuable())
add_btn.place(relx = 0.98, rely = 0.98, anchor = tkinter.SE)

stock_frame = customtkinter.CTkFrame(master= STOCK_GUI, 
                                    width= 400, height= 150, 
                                    corner_radius= 25, border_width= None, 
                                    bg_color= 'transparent',fg_color= '#212121', 
                                    border_color= None)

stock_frame.pack(padx= 10, pady= 10)

STOCK_GUI.mainloop()
# if __name__ == '__main__':
#       main(sys.argv)


# Добавить возможность создания новых фреймов при нажатии на кнопку
# Сделать окно создания фрейма
# Добавить возможность удаления фреймов при нажатии на кнопку самого фрейма
#