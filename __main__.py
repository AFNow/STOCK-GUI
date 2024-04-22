'''
This file contains the base interface, for now..., and theme settings + comments

'''

import customtkinter # UI library

from functions import *

# Window arguments
STOCK_GUI = customtkinter.CTk()
STOCK_GUI.resizable(width=False, height=True)
STOCK_GUI.title('STOCK-GUI')
rootHeight = STOCK_GUI.winfo_height()
rootWidth = STOCK_GUI.winfo_width()

# Default visual theme
customtkinter.set_appearance_mode('dark') 
customtkinter.set_default_color_theme("resources/theme.json")

# Setting window icon
STOCK_GUI.iconbitmap('resources/stock_icon-favi.ico')

# Default window size
window_size_x = 340
window_size_y = 500

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
    def __init__(self, master, stock_name, stock_cost, stock_raise, **kwargs):
        self.root = main_frame
        self.stock_name = stock_name
        super().__init__(master, **kwargs)
        self.frame = customtkinter.CTkFrame(master=main_frame,
                                            width=300, height=100,
                                            corner_radius=13, border_width=None,
                                            bg_color='transparent', fg_color='gray11',
                                            border_color=None)
        self.frame.pack(anchor=customtkinter.CENTER, expand=False, pady=10)

        # The label of stock's name 
        name_var = stock_name ###
        name_label_font = customtkinter.CTkFont(family="Roboto", size=35, weight="bold")
        actual_color = 'white' #### Later it will be changed every tick
        self.name_label = customtkinter.CTkLabel(master=self.frame, textvariable=name_var, font = name_label_font, text= name_var, text_color = actual_color)
        self.name_label.place(relx=0.1, rely=0.3, anchor=customtkinter.W)

        # The label of stock's cost 
        cost_var = stock_cost ###
        cost_label_font = customtkinter.CTkFont(family="Roboto", size=12, weight="normal")
        actual_color = 'white' #### Later it will be changed every tick
        self.cost_label = customtkinter.CTkLabel(master=self.frame, textvariable=cost_var, font = cost_label_font, text= cost_var, text_color = actual_color)
        self.cost_label.place(relx=0.1, rely=0.6, anchor=customtkinter.W)   

        # The label of stock's % 
        raise_var = stock_raise ###
        percent_label_font = customtkinter.CTkFont(family="Roboto", size=12, weight="normal")
        actual_color = 'white' #### Later it will be changed every tick
        self.cost_label = customtkinter.CTkLabel(master=self.frame, textvariable=raise_var, font = percent_label_font, text= raise_var, text_color = actual_color)
        self.cost_label.place(relx=0.1, rely=0.8, anchor=customtkinter.W)   

        delete_btn = customtkinter.CTkButton(master=self.frame, text='', command=self.delete_frame,
                                          height=10, width=295, corner_radius = 13, fg_color = 'transparent', hover_color='#9c322a')
        delete_btn.place(relx=0.5, rely=0.98, anchor=customtkinter.CENTER)


    # Создание экземпляра класса StockFrame при вызове функции open_new_frame()
    stock_frame = None
    def open_new_frame():
        global stock_frame
        entry_str = entry.get()
        if entry_str != '':
            stock_cost = get_stock_data(entry_str).get('item_cost')
            # stock_raise = get_stock_data(entry_str).get('item_raise')
            # stock_gain = get_stock_data(entry_str).get('item_gain')
            stock_frame = StockFrame(main_frame, stock_name=entry_str, stock_cost=stock_cost, stock_raise='')
    
    # Frame deleting function
    def delete_frame(self):
        self.frame.destroy()
    
    #def update_stock_data(self):
    #while True:
        #self.stock_cost = get_stock_data(self.stock_name)
        #self.cost_var = self.stock_cost
        #self.cost_label.configure(text=str(self.cost_var))  
        #time.sleep(5)


# Add button settings
add_btn = customtkinter.CTkButton(master= bottom_frame, text= 'Add new', command= StockFrame.open_new_frame, height= 35, width= 145)
add_btn.place(anchor = customtkinter.SE, relx = 0.95, rely = 0.7)

# Entry settings
entry = customtkinter.CTkEntry(master=bottom_frame, placeholder_text="The stock name", height= 35, width= 145)
entry.place (anchor = customtkinter.SW, relx = 0.05, rely = 0.7)


# The window and grid settings
STOCK_GUI.geometry(str(window_size_x)+'x'+str(window_size_y))
STOCK_GUI.attributes('-alpha', 0.8)
STOCK_GUI.grid_rowconfigure(0, weight=1)
STOCK_GUI.grid_columnconfigure(1, weight=0)
STOCK_GUI.grid_columnconfigure(0, weight=1) 
STOCK_GUI.mainloop()


# Сделать параметры создания фрейма
# Добавить цикл обновления фреймов
# Добавить файл, где будут записываться настройки фреймов
# Добавить чтение фреймов при запуске, если уже имеется файл с настройками фреймов