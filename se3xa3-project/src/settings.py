## @file settings.py
#  @author Muneeb Arshad, Shesan Balachandran, Bill Nguyen
#  @title Settings
#  @date April 4, 2021
from tkinter import *

username = None

def back(main_window):
    main_window.destroy()
    import main_start
    main_start.start_main_page()

## @brief optionGameMode function
#  @details This function is used to display the game mode setting page and save the selected game mode
#  @param main_window
#  @param user represents the selected user
def optionGameMode(main_window,user):
        global username
        username = user


        gameMode1 = Button(
            text="Ranked Game Mode",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: showOptionDifficulty(1),
        )

        gameMode2 = Button(
            text="Practice Game Mode",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: showOptionDifficulty(2),
        )

      
        gameMode1.grid(row=1, column=4, pady=(100, 0), padx=50, )
        gameMode2.grid(row=2, column=4, pady=(50, 0), padx=50, )

        def showOptionDifficulty(args):
            gameMode1.destroy()
            gameMode2.destroy()
            global gameMode
            global difficulty
            if args == 1:
                gameMode = "Ranked Game Mode"
                print(gameMode)
                optionDifficulty(main_window)
            elif args == 2:
                gameMode = "Practice Game Mode"
                print(gameMode)
                optionDifficulty(main_window)

## @brief optionDifficulty function
#  @details This function is used to display difficulty setting page and save selected difficulty level
#  @param main_window
def optionDifficulty(main_window):

    sel_btn1 = Button(
        text="Easy",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        cursor="hand2",
        command=lambda: show_option(1),
    )

    sel_btn2 = Button(
        text="Medium",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        cursor="hand2",
        command=lambda: show_option(2),
    )

    sel_btn3 = Button(
        text="Hard",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        cursor="hand2",
        command=lambda: show_option(3),
    )

    
    
    sel_btn1.grid(row=1, column=4, pady=(50, 0), padx=50, )
    sel_btn2.grid(row=2, column=4, pady=(10, 0), padx=50, )
    sel_btn3.grid(row=3, column=4, pady=(10, 0), padx=50, )

    def show_option(args):
        sel_btn1.destroy()
        sel_btn2.destroy()
        sel_btn2.destroy()

        global gameMode
        global difficulty
        if args == 1:
            difficulty = "easy"
            print(difficulty)
            option(main_window)
        elif args == 2:
            difficulty = "medium"
            print(difficulty)
            option(main_window)
        elif args == 3:
            difficulty = "hard"
            print(difficulty)
            option(main_window)

## @brief start_game function
#  @details Once all settings have been selected this method is used to start the game based on the given settings
#  @param args
#  @param main_window
def start_game(args,main_window):
    main_window.destroy()
    import Game
    
    if args == 1:
        
        
        Game.main(gameMode, difficulty, username, 'animals')
    elif args == 2:
        
        Game.main(gameMode, difficulty, username, 'bodyparts')
    elif args == 3:
        
        Game.main(gameMode, difficulty, username, 'colours')
    elif args == 4:
        
        Game.main(gameMode, difficulty, username, 'fruits')
    elif args == 5:
        
        Game.main(gameMode, difficulty, username, 'shapes')
    elif args == 6:
        
        Game.main(gameMode, difficulty, username, 'vegetables')
    elif args == 7:
        
        Game.main(gameMode, difficulty, username, 'vehicles')

## @brief option function
#  @details This function is used to display the categories setting page and save the selected category
#  @param main_window
def option(main_window):
 
    sel_btn1 = Button(
        text="Animals",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        cursor="hand2",
        command=lambda: start_game(1,main_window),
    )

    sel_btn2 = Button(
        text="Body parts",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        cursor="hand2",
        command=lambda: start_game(2,main_window),
    )

    sel_btn3 = Button(
        text="Colour",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        cursor="hand2",
        command=lambda: start_game(3,main_window),
    )

    sel_btn4 = Button(
        text="Fruits",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        cursor="hand2",
        command=lambda: start_game(4,main_window),
    )

    sel_btn5 = Button(
        text="Shapes",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        cursor="hand2",
        command=lambda: start_game(5,main_window),
    )

    sel_btn6 = Button(
        text="Vegetable",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        cursor="hand2",
        command=lambda: start_game(6,main_window),
    )

    sel_btn7 = Button(
        text="Vehicles",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        cursor="hand2",
        command=lambda: start_game(7,main_window),
    )
    
    sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
    sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
    sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
    sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
    sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
    sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )
    sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=50, )