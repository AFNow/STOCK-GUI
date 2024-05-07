'''
This file contains the base interface and main class functions, theme settings + comments

'''
import time

import customtkinter # UI library
import tkinter

from functions import *

from threading import Thread


# Window arguments
STOCK_GUI = customtkinter.CTk()
STOCK_GUI.resizable(width=False, height=True)
STOCK_GUI.title('STOCK-GUI')
rootHeight = STOCK_GUI.winfo_height()
rootWidth = STOCK_GUI.winfo_width()

# Default visual theme
customtkinter.set_appearance_mode('dark') 
customtkinter.set_default_color_theme("resources/theme.json") # resources/theme.json

# Setting window icon
STOCK_GUI.iconbitmap('resources/stock_icon-favi.ico') # resources/stock_icon-favi.ico

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
                                    corner_radius= 0, border_width= None, fg_color= 'gray10', width=300, height=120,
                                    border_color= None)
bottom_frame.grid(row=9, column=0, sticky='nsew')

#Stock frame class
class StockFrame(customtkinter.CTkFrame):
    def __init__(self, master, stock_name, index_name, close_stock_cost, now_stock_cost, stock_change, stock_raise, **kwargs):
        self.root = main_frame
        self.stock_name = stock_name
        self.index_name = index_name
        super().__init__(master, **kwargs)
        self.frame = customtkinter.CTkFrame(master=main_frame,
                                            width=300, height=110,
                                            corner_radius=13, border_width=None,
                                            bg_color='transparent', fg_color='gray11',
                                            border_color=None)
        self.frame.pack(anchor=customtkinter.CENTER, expand=False, pady=10)

        customtkinter.FontManager.load_font('Roboto.ttf')
        main_label_font = customtkinter.CTkFont(family='Roboto', size=35, weight='bold')
        secondary_label_font = customtkinter.CTkFont(family='Roboto', size=12, weight='bold')

        # The font color operation for the stock var's
        if stock_change > 0:
            actual_color = 'green'
        elif stock_change < 0:
            actual_color = 'red'
        else:
            actual_color = 'white'


        # The label of stock's name 
        self.name_var = tkinter.StringVar(value=stock_name)
        self.name_label = customtkinter.CTkLabel(master=self.frame, textvariable=self.name_var, font = main_label_font, text_color = 'white')
        self.name_label.place(relx=0.1, rely=0.3, anchor=customtkinter.W)

        # The label of stock's close cost 
        self.close_cost_var = tkinter.StringVar(value=close_stock_cost)
        self.cost_label = customtkinter.CTkLabel(master=self.frame, textvariable=self.close_cost_var, font = secondary_label_font, text_color = actual_color)
        self.cost_label.place(relx=0.1, rely=0.63, anchor=customtkinter.W)   

        # The label of stock's actual cost 
        self.now_cost_var = tkinter.StringVar(value=now_stock_cost)
        self.cost_label = customtkinter.CTkLabel(master=self.frame, textvariable=self.now_cost_var, font = secondary_label_font, text_color = actual_color)
        self.cost_label.place(relx=0.1, rely=0.83, anchor=customtkinter.W)   

        # The label of stock's raise
        self.change_var = tkinter.StringVar(value='Earnings: $' + str(stock_change))
        self.change_label = customtkinter.CTkLabel(master=self.frame, textvariable=self.change_var, font = secondary_label_font, text_color = actual_color)
        self.change_label.place(relx=0.9, rely=0.63, anchor=customtkinter.E)   
        
        # The label of stock's raise %
        self.raise_percent_var = tkinter.StringVar(value=str(stock_raise) + '%')
        self.raise_percent_label = customtkinter.CTkLabel(master=self.frame, textvariable=self.raise_percent_var, font = main_label_font, text_color = actual_color)
        self.raise_percent_label.place(relx=0.9, rely=0.3, anchor=customtkinter.E)   

        delete_btn = customtkinter.CTkButton(master=self.frame, text='', command=self.delete_frame,
                                          height=10, width=295, corner_radius = 13, fg_color = 'transparent', hover_color='#9c322a')
        delete_btn.place(relx=0.5, rely=0.98, anchor=customtkinter.CENTER)

        # The updating function for added varuables in every time.sleep() period
        def update():
            global stock_frame
            while True:
                time.sleep(1800)
                stock_data = get_stock_data(stock_name, index_name)
                updated_close_cost_label = 'Last close: $' + stock_data.get('last_close')
                self.close_cost_var.set(updated_close_cost_label)
                updated_now_stock_cost = 'Now: $' + stock_data.get('item_cost')
                self.now_cost_var.set(updated_now_stock_cost)
                updated_stock_change = round(stock_data.get('change'))
                self.change_var.set('Earnings: $' + str(updated_stock_change))
                updated_stock_raise = round((float(updated_stock_change) / float(stock_data.get('item_cost'))) * 100, 2)
                self.raise_percent_var.set(str(updated_stock_raise)  + '%')
        # Threading for the update function
        def update_available():
            thread = Thread(target = update, daemon = True)
            thread.start()
            return thread
        update_available()


    # The stock_frame default state
    stock_frame = None
    # Creation of the StockFrame example at INIT from stocks.json file
    def restore_frames():
        global stock_frame
        with open('stocks.json', mode = 'r', encoding='utf-8') as file: # stocks.json
            text = file.read()
            if text != '':
                splitted_text = text.split()
                index = 0
                while index != len(splitted_text):
                    stock_data = get_stock_data(splitted_text[index], splitted_text[index+1])
                    close_stock_cost = 'Last close: $' + stock_data.get('last_close')
                    now_stock_cost = 'Now: $' + stock_data.get('item_cost')
                    stock_change = round(stock_data.get('change'))
                    stock_raise = round((float(stock_change) / float(stock_data.get('item_cost'))) * 100, 2)
                    stock_frame = StockFrame(main_frame, stock_name=splitted_text[index], index_name = splitted_text[index+1], 
                                             close_stock_cost=close_stock_cost, now_stock_cost=now_stock_cost, stock_change=stock_change, stock_raise=stock_raise)
                    index += 2
            else:
                pass    

    # The creation of class example open_new_frame()
    def open_new_frame():
        try:
            global stock_frame
            entry_str = name_entry.get()
            index_choice = index_entry.get()
            if entry_str != '':
                stock_data = get_stock_data(entry_str, index_choice)
                close_stock_cost = 'Close: $' + stock_data.get('last_close')
                now_stock_cost = 'Now: $' + stock_data.get('item_cost')
                stock_change = round(stock_data.get('change'))
                stock_raise = round((float(stock_change) / float(stock_data.get('item_cost'))) * 100, 2)
                stock_frame = StockFrame(main_frame, stock_name=entry_str, index_name = index_choice, close_stock_cost=close_stock_cost, now_stock_cost=now_stock_cost, stock_change=stock_change, stock_raise=stock_raise)
                info_label.configure(text = 'Stock added', text_color = 'green')
                save_stock(entry_str, index_choice)
                index_entry.delete(0, 'end')
                name_entry.delete(0, 'end')
        except AttributeError:
            info_label.configure(text = 'Wrong names', text_color = 'red')
            index_entry.delete(0, 'end')
            name_entry.delete(0, 'end')

    # Threading for the creation method
    def new_frame_threading():
        thread = Thread(target = StockFrame.open_new_frame, daemon = True)
        thread.start()
        return thread


    # Frame deleting function
    def delete_frame(self):
        self.frame.destroy()
        with open('stocks.json', mode = 'r', encoding='utf-8') as file: # stocks.json
            text = file.readlines()
            text = [item.replace(self.stock_name + ' ' + self.index_name +'\n', '') for item in text]
        with open('stocks.json', 'w', encoding='utf-8') as file: # stocks.json
            file.writelines(text)
        info_label.configure(text = 'Stock deleted', text_color = 'white')

# Add button settings
add_btn = customtkinter.CTkButton(master= bottom_frame, text= 'Add new', command= StockFrame.new_frame_threading, height= 35, width= 145)
add_btn.place(anchor = customtkinter.SE, relx = 0.95, rely = 0.8)

# Entry for the stock name's settings
name_entry = customtkinter.CTkEntry(master=bottom_frame, placeholder_text="The stock name", height= 35, width= 145)
name_entry.place (anchor = customtkinter.SW, relx = 0.05, rely = 0.8)

# Entry for the index name's settings
index_entry = customtkinter.CTkEntry(master=bottom_frame, placeholder_text="The index", height= 35, width= 145)
index_entry.place (anchor = customtkinter.SW, relx = 0.05, rely = 0.4)

# Info-label 
main_label_font = customtkinter.CTkFont(family="Roboto", size=20, weight="bold")
status = None
info_label = customtkinter.CTkLabel(master=bottom_frame, textvariable=status, font = main_label_font, text= status)
info_label.place(anchor = customtkinter.CENTER, relx = 0.73, rely = 0.3)


# The window and grid settings
STOCK_GUI.geometry(str(window_size_x)+'x'+str(window_size_y))
STOCK_GUI.attributes('-alpha', 0.9)
STOCK_GUI.grid_rowconfigure(0, weight=1)
STOCK_GUI.grid_columnconfigure(1, weight=0)
STOCK_GUI.grid_columnconfigure(0, weight=1)


# The frame restore and mainloop
StockFrame.restore_frames()
STOCK_GUI.mainloop()