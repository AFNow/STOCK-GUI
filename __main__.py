import sys # Will be useful later

import tkinter # UI library
import customtkinter # UI library

import yfinance # Will be useful later
import pandas # Will be useful later
import flask # Will be useful later

from functions import add_varuable # Will be useful later


# Default visual theme
customtkinter.set_appearance_mode('dark') 
customtkinter.set_default_color_theme("STOCK-GUI/theme.json")

# Window arguments
STOCK_GUI = customtkinter.CTk()
STOCK_GUI.resizable(width=False, height=True)
STOCK_GUI.title('STOCK-GUI')
rootHeight = STOCK_GUI.winfo_height()
rootWidth = STOCK_GUI.winfo_width()

# Setting window icon
STOCK_GUI.iconbitmap('STOCK-GUI/stock_icon-favi.ico')

# Background frame
main_frame = customtkinter.CTkScrollableFrame(master= STOCK_GUI,  # The main background frame
                                    width= rootWidth, height= rootHeight-20, 
                                    corner_radius= 25, border_width= None, 
                                    bg_color= 'transparent',fg_color= 'gray8', 
                                    border_color= None,scrollbar_button_color= 'gray8')
main_frame.pack(anchor = customtkinter.SE, padx= 10, pady= 10, fill='both', expand=True)

#Stock frame class
class StockFrame(customtkinter.CTkFrame):
    frame_qty = 1
    def __init__(self, master, **kwargs):
        self.root = main_frame
        super().__init__(master, **kwargs)
        self.frame = customtkinter.CTkFrame(master= main_frame, 
                                    width= stock_frame_size_x, height= stock_frame_size_y, 
                                    corner_radius= 13, border_width= None, 
                                    bg_color= 'transparent',fg_color= 'gray11', 
                                    border_color= None)
        self.frame.pack(anchor = customtkinter.CENTER, expand=True, pady = 10)

    def open_new_frame(self):
        new_frame = StockFrame(self.root)

# StockFrame varuables
stock_frame_size_x = 300
stock_frame_size_y = 100
window_size_x = (stock_frame_size_x * 1) +20
window_size_y = (stock_frame_size_y) + 300

stock_frame = StockFrame(main_frame) # Binding the StockFrame to the main_frame

#Button settings
add_btn = customtkinter.CTkButton(master= STOCK_GUI, text= 'Add new', command= stock_frame.open_new_frame)
add_btn.pack(anchor = customtkinter.SE, padx = 10, pady = 10)

# The window settings
STOCK_GUI.geometry(str(window_size_x)+'x'+str(window_size_y))
STOCK_GUI.attributes('-alpha', 0.85)
STOCK_GUI.mainloop()



# if __name__ == '__main__':
#       main(sys.argv)


# Добавить возможность создания новых фреймов при нажатии на кнопку
# Сделать окно создания фрейма
# Добавить возможность удаления фреймов при нажатии на кнопку самого фрейма
#

#stock_frame = customtkinter.CTkFrame(master= main_frame, 
#                                    width= stock_frame_size_x, height= stock_frame_size_y, 
#                                    corner_radius= 13, border_width= None, 
#                                    bg_color= 'transparent',fg_color= 'gray11', 
#                                    border_color= None)
#stock_frame.pack(padx= 10, pady= 10, expand=False)