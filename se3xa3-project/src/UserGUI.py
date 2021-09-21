## @file UserGUI.py
#  @author Muneeb Arshad, Shesan Balachandran, Bill Nguyen
#  @title UserGUI
#  @date April 4, 2021
from tkinter import *


## @brief username_page
#  @details This function is used to display the username setting page
#  @param main_window
def username_page(main_window):
        
        def submit_username():
            username = name_entry.get()
            sub_btn.destroy()
            name_label.destroy()
            name_entry.destroy()
            
            # Adds username to the userData JSON file
            import user
            user.addUser(username)
            import settings
            settings.optionGameMode(main_window,username)
            
            

        name_var= StringVar()

        # enter username text
        name_label = Label(main_window,text="Enter Username", bg="#e6fff5",height="2",  font=("Arial",20,'bold'))
        
        #username input box
        name_entry = Entry(
            main_window,
            textvariable = name_var,
            font="none 20",
            borderwidth=5,
            justify='center',
        )

        # Submit button
        sub_btn = Button(
            text="Submit",
            width=18,
            borderwidth=8,
            font=("", 13),
            fg="#000000",
            bg="#99ffd6",
            command=submit_username,
        )

       
        
        
        name_label.pack(pady=(150, 20))
        name_entry.pack(pady=(10, 20))
        sub_btn.pack(pady=(10, 20))