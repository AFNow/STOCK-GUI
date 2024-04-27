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
                                    corner_radius= 0, border_width= None, fg_color= 'gray10', width=300, height=120,
                                    border_color= None)
bottom_frame.grid(row=9, column=0, sticky='nsew')

#Stock frame class
class StockFrame(customtkinter.CTkFrame):
    def __init__(self, master, stock_name, stock_cost, stock_change, stock_raise, **kwargs):
        self.root = main_frame
        self.stock_name = stock_name
        super().__init__(master, **kwargs)
        self.frame = customtkinter.CTkFrame(master=main_frame,
                                            width=300, height=110,
                                            corner_radius=13, border_width=None,
                                            bg_color='transparent', fg_color='gray11',
                                            border_color=None)
        self.frame.pack(anchor=customtkinter.CENTER, expand=False, pady=10)

        main_label_font = customtkinter.CTkFont(family="Roboto", size=35, weight="bold")
        secondary_label_font = customtkinter.CTkFont(family="Roboto", size=12, weight="bold")

        # The font color operation for the stock var's
        if stock_change > 0:
            actual_color = 'green'
        elif stock_change < 0:
            actual_color = 'red'
        else:
            actual_color = 'white'

        # The label of stock's name 
        name_var = stock_name 
        self.name_label = customtkinter.CTkLabel(master=self.frame, textvariable=name_var, font = main_label_font, text= name_var, text_color = 'white')
        self.name_label.place(relx=0.1, rely=0.3, anchor=customtkinter.W)

        # The label of stock's cost 
        cost_var = stock_cost 
        self.cost_label = customtkinter.CTkLabel(master=self.frame, textvariable=cost_var, font = secondary_label_font, text= cost_var, text_color = actual_color)
        self.cost_label.place(relx=0.1, rely=0.63, anchor=customtkinter.W)   

        # The label of stock's raise
        stock_change_var = 'Earnings: $' + str(stock_change) 
        self.change_label = customtkinter.CTkLabel(master=self.frame, textvariable=stock_change_var, font = secondary_label_font, text= stock_change_var, text_color = actual_color)
        self.change_label.place(relx=0.1, rely=0.83, anchor=customtkinter.W)   
        
        # The label of stock's raise %
        raise_percent_var = str(stock_raise) + '%'
        self.raise_percent_label = customtkinter.CTkLabel(master=self.frame, textvariable=raise_percent_var, font = main_label_font, text= raise_percent_var, text_color = actual_color)
        self.raise_percent_label.place(relx=0.9, rely=0.3, anchor=customtkinter.E)   

        delete_btn = customtkinter.CTkButton(master=self.frame, text='', command=self.delete_frame,
                                          height=10, width=295, corner_radius = 13, fg_color = 'transparent', hover_color='#9c322a')
        delete_btn.place(relx=0.5, rely=0.98, anchor=customtkinter.CENTER)

    # Cоздание экземпляра класса StockFrame при запуске, из файла stocks.json
    #stock_frame = None
    #def restore_frame(entry_str):
    #    global stock_frame
    #    if entry_str != '':
    #        stock_data = get_stock_data(entry_str)
    #        stock_cost = 'Last close: $' + stock_data.get('last_close') + '    ' + 'Now :$' + stock_data.get('item_cost')
    #        stock_change = round(stock_data.get('change'))
    #        stock_raise = round((float(stock_change) / float(stock_data.get('item_cost'))) * 100, 2)
    #        stock_frame = StockFrame(main_frame, stock_name=entry_str, stock_cost=stock_cost, stock_change=stock_change, stock_raise=stock_raise)

    # The creation of class example open_new_frame()
    def open_new_frame():
        try:
            global stock_frame
            entry_str = entry.get()
            index_choice = combo_box.get()
            if entry_str != '':
                stock_data = get_stock_data(entry_str, index_choice)
                stock_cost = 'Close: $' + stock_data.get('last_close') + '          ' + 'Now :$' + stock_data.get('item_cost')
                stock_change = round(stock_data.get('change'))
                stock_raise = round((float(stock_change) / float(stock_data.get('item_cost'))) * 100, 2)
                stock_frame = StockFrame(main_frame, stock_name=entry_str, stock_cost=stock_cost, stock_change=stock_change, stock_raise=stock_raise)
                info_label.configure(text = 'Done')
                saving_stock(entry_str, index_choice)
        except KeyError:
            info_label.configure(text = 'Error')
   
    # Frame deleting function
    def delete_frame(self):
        self.frame.destroy()


# Add button settings
add_btn = customtkinter.CTkButton(master= bottom_frame, text= 'Add new', command= StockFrame.open_new_frame, height= 35, width= 145)
add_btn.place(anchor = customtkinter.SE, relx = 0.95, rely = 0.8)

# Entry settings
entry = customtkinter.CTkEntry(master=bottom_frame, placeholder_text="The stock name", height= 35, width= 145)
entry.place (anchor = customtkinter.SW, relx = 0.05, rely = 0.8)

# Combo box for the stock index selection
combo_box = customtkinter.CTkComboBox(master=bottom_frame, width = 145, values= ['NASDAQ', 'NYSE', 'index3'])
combo_box.place (anchor = customtkinter.SW, relx = 0.05, rely =0.4)



# Info-label 
main_label_font = customtkinter.CTkFont(family="Roboto", size=20, weight="bold")
status = None  ###

# The font color operation for the status
info_label = customtkinter.CTkLabel(master=bottom_frame, textvariable=status, font = main_label_font, text= status, text_color = 'white')
info_label.place(anchor = customtkinter.CENTER, relx = 0.73, rely = 0.3)


    
# The window and grid settings
STOCK_GUI.geometry(str(window_size_x)+'x'+str(window_size_y))
STOCK_GUI.attributes('-alpha', 0.9)
STOCK_GUI.grid_rowconfigure(0, weight=1)
STOCK_GUI.grid_columnconfigure(1, weight=0)
STOCK_GUI.grid_columnconfigure(0, weight=1)

# The reading stocks.json operation if it contains something
#with open('stocks.json', mode = 'r', encoding='utf-8') as file:
#    text = [file.read()]
#    print (text)
#    if text != '':
#        pass
#            while index != len(read_stock_name):
#                stock_name = read_stock_name[0:index]
            
#        print(read_stock_name)
            #StockFrame.restore_frame(reading_stock_name[0:4])
            #if reading_stock_name != ' ':
#        break
        
STOCK_GUI.mainloop()

# Добавить цикл обновления фреймов
# Добавить чтение фреймов при запуске, если уже имеется файл с настройками фреймов