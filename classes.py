#Stock frame class
class StockFrame(customtkinter.CTkFrame):
    frame_qty = 1
    def __init__(self, master, stock_name = 'NASDAQ', stock_cost=None, **kwargs):
        self.root = main_frame
        self.stock_name = stock_name
        super().__init__(master, **kwargs)
        self.frame = customtkinter.CTkFrame(master=main_frame,
                                            width=stock_frame_size_x, height=stock_frame_size_y,
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
        cost_var = '' ###
        cost_label_font = customtkinter.CTkFont(family="Roboto", size=12, weight="normal")
        actual_color = 'white' #### Later it will be changed every tick
        self.cost_label = customtkinter.CTkLabel(master=self.frame, textvariable=cost_var, font = cost_label_font, text= cost_var, text_color = actual_color)
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

    #def update_stock_data(self):
        #while True:
            #self.stock_cost = get_stock_data(self.stock_name)
            #self.cost_var = self.stock_cost
            #self.cost_label.configure(text=str(self.cost_var))  
            #time.sleep(5)
    # New frame creating function
    
    def open_new_frame():
        entry_str = entry.get()
        if entry_str != '':
            new_frame = StockFrame(entry_str)
        return entry_str
    
    def update_interface(self):
        self.cost_label.config(text=str(self.cost_var))

    # Frame deleting function
    def delete_frame(self):
        self.frame.destroy()

# Binding the StockFrame to the main_frame
stock_frame = StockFrame(main_frame, stock_name='')

