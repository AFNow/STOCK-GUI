import sys # Will be useful later

import customtkinter # UI library

import googlefinance # Will be useful later
import pandas # Will be useful later
import flask # Will be useful later

import datetime


# Default visual theme
customtkinter.set_appearance_mode('dark') 
customtkinter.set_default_color_theme("theme.json")

# Window arguments
STOCK_GUI = customtkinter.CTk()
STOCK_GUI.resizable(width=False, height=True)
STOCK_GUI.title('STOCK-GUI')
rootHeight = STOCK_GUI.winfo_height()
rootWidth = STOCK_GUI.winfo_width()

# Setting window icon
STOCK_GUI.iconbitmap('stock_icon-favi.ico')

# Background frame
main_frame = customtkinter.CTkScrollableFrame(master= STOCK_GUI,  # The main background frame
                                    width= 290, height= rootHeight-20, 
                                    corner_radius= 18, border_width= None, 
                                    bg_color= 'transparent',fg_color= 'gray8', 
                                    border_color= None,scrollbar_button_color= 'gray8')
main_frame.grid(row=0, column=0, sticky='ns')

# Bottom frame
bottom_frame = customtkinter.CTkFrame(master= STOCK_GUI,  # The bottom frame for button and entry 
                                    corner_radius= 0, border_width= None, fg_color= 'gray10', width=300, height=80,
                                    border_color= None)
bottom_frame.grid(row=9, column=0, sticky='nsew')


#Stock frame class
class StockFrame(customtkinter.CTkFrame):
    frame_qty = 1
    def __init__(self, master, **kwargs):
        self.root = main_frame
        super().__init__(master, **kwargs)
        self.frame = customtkinter.CTkFrame(master=main_frame,
                                            width=stock_frame_size_x, height=stock_frame_size_y,
                                            corner_radius=13, border_width=None,
                                            bg_color='transparent', fg_color='gray11',
                                            border_color=None)
        self.frame.pack(anchor=customtkinter.CENTER, expand=False, pady=10)

        # The label of stock's name 
        name_var = 'Stock_Name' ###
        name_label_font = customtkinter.CTkFont(family="Roboto", size=35, weight="bold")
        actual_color = 'white' #### Later it will be changed every tick
        self.name_label = customtkinter.CTkLabel(master=self.frame, textvariable=name_var, font = name_label_font, text= 'STCK', text_color = actual_color)
        self.name_label.place(relx=0.1, rely=0.3, anchor=customtkinter.W)

        # The label of stock's cost 
        text_var = 'Stock_Cost' ###
        cost_label_font = customtkinter.CTkFont(family="Roboto", size=12, weight="normal")
        actual_color = 'white' #### Later it will be changed every tick
        self.cost_label = customtkinter.CTkLabel(master=self.frame, textvariable=text_var, font = cost_label_font, text= '$1.000', text_color = actual_color)
        self.cost_label.place(relx=0.1, rely=0.6, anchor=customtkinter.W)   

        # The label of stock's % 
        text_var = 'Stock_%' ###
        percent_label_font = customtkinter.CTkFont(family="Roboto", size=12, weight="normal")
        actual_color = 'white' #### Later it will be changed every tick
        self.cost_label = customtkinter.CTkLabel(master=self.frame, textvariable=text_var, font = percent_label_font, text= '0.025%', text_color = actual_color)
        self.cost_label.place(relx=0.1, rely=0.8, anchor=customtkinter.W)   

        delete_btn = customtkinter.CTkButton(master=self.frame, text='', command=self.delete_frame,
                                          height=10, width=295, corner_radius = 13, fg_color = 'transparent', hover_color='#9c322a')
        delete_btn.place(relx=0.5, rely=0.98, anchor=customtkinter.CENTER)

    # New frame creating function
    def open_new_frame(self):
        new_frame = StockFrame(self.root)
    # Frame deleting function
    def delete_frame(self):
        self.frame.destroy()

# StockFrame varuables
stock_frame_size_x = 300
stock_frame_size_y = 100
window_size_x = (stock_frame_size_x * 1) +40
window_size_y = (stock_frame_size_y) + 300
# Binding the StockFrame to the main_frame
stock_frame = StockFrame(main_frame) 


# Add button settings
add_btn = customtkinter.CTkButton(master= bottom_frame, text= 'Add new', command= stock_frame.open_new_frame, height= 35, width= 145)
add_btn.place(anchor = customtkinter.SE, relx = 0.95, rely = 0.7)

# Entry settings
entry = customtkinter.CTkEntry(master=bottom_frame, placeholder_text="The stock name", height= 35, width= 145)
entry.place (anchor = customtkinter.SW, relx = 0.05, rely = 0.7)


# The window settings
STOCK_GUI.geometry(str(window_size_x)+'x'+str(window_size_y))
STOCK_GUI.attributes('-alpha', 1)
STOCK_GUI.grid_rowconfigure(0, weight=1)
STOCK_GUI.grid_columnconfigure(1, weight=0)  # Фиксированный размер для первого фрейма
STOCK_GUI.grid_columnconfigure(0, weight=1) 
STOCK_GUI.mainloop()


# if __name__ == '__main__':
#       main(sys.argv)

# Сделать параметры создания фрейма

# Добавить цикл обновления фреймов
# Добавить файл, где будут записываться настройки фреймов
# Добавить чтение фреймов при запуске, если уже имеется файл с настройками фреймов