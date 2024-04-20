'''
This file contains the base interface, for now..., and theme settings + comments

'''

import customtkinter # UI library


# Default visual theme
customtkinter.set_appearance_mode('dark') 
customtkinter.set_default_color_theme("resources/theme.json")


# Window arguments
STOCK_GUI = customtkinter.CTk()
STOCK_GUI.resizable(width=False, height=True)
STOCK_GUI.title('STOCK-GUI')
rootHeight = STOCK_GUI.winfo_height()
rootWidth = STOCK_GUI.winfo_width()


# Setting window icon
STOCK_GUI.iconbitmap('resources/stock_icon-favi.ico')


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



window_size_x = 340
window_size_y = 500

# Add button settings
add_btn = customtkinter.CTkButton(master= bottom_frame, text= 'Add new', command= '???', height= 35, width= 145)
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


# Сделать параметры создания фрейма
# Добавить цикл обновления фреймов
# Добавить файл, где будут записываться настройки фреймов
# Добавить чтение фреймов при запуске, если уже имеется файл с настройками фреймов
# Переделать создание StockFrame класса