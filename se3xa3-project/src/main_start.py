## @file main_start.py
#  @author Muneeb Arshad, Shesan Balachandran, Bill Nguyen
#  @title main_start
#  @date April 4, 2021
from tkinter import *
# Global Variables
gameMode = ""
difficulty = ""
username = None

## @brief start_main_page 
#  @details function is used to start and display the main menu page and initializes everything in order for the game to work
def start_main_page():

    
    ## @brief back function
    #  @details This function is used to return back to the main menu
    def back():
        main_window.destroy()
        start_main_page()

    ## @brief showbackButton function
    #  @details This function is used to display the back button
    def showBackButton():

        backButton = Button(
            main_window,
            image=img1,
            bg='#e6fff5',
            border=0,
            justify='center',
            command=back,
        )

        backButton.grid(row=0, column=0, padx=20)
        

    ## @brief show enter usernmae function
    #  @details This function is used to display the username setting
    def show_enter_username():
        start_btn.destroy()
        leader_btn.destroy()
        quit_btn.destroy()
        lab_img.destroy()
        import UserGUI
        UserGUI.username_page(main_window)
        
    ## @brief show leaderboard function
    #  @details This function is used to display the leaderboard UI   
    def show_leaderboard():
        start_btn.destroy()
        leader_btn.destroy()
        quit_btn.destroy()
        lab_img.destroy()

        import leaderBoard
        showBackButton()
        leaderBoard.show()
    
    ## @brief quit function
    #  @details This function is used to quit the game
    def quit():
        main_window.destroy()


    main_window = Tk()

    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("Quizee --> Grow your kids with Quizee")
    main_window.configure(background="#e6fff5")
    main_window.iconbitmap(r'assets/quizee_logo_.ico')

    img0 = PhotoImage(file="assets/quizee_logo.png")
    img1 = PhotoImage(file="assets/back.png")

    lab_img = Label(
        main_window,
        image=img0,
        bg='#e6fff5',
    )
    lab_img.pack(pady=(50, 0))

    

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        cursor="hand2",
        command=show_enter_username,
    )
    start_btn.pack(pady=(20, 10))

    leader_btn = Button(
        main_window,
        text="Leaderboard",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        cursor="hand2",
        command=show_leaderboard,
    )
    leader_btn.pack(pady=(20, 10))

    quit_btn = Button(
        main_window,
        text="Quit",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        cursor="hand2",
        command=quit,
    )
    quit_btn.pack(pady=(20, 10))

    main_window.mainloop()


start_main_page()
