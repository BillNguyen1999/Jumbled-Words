## @file leaderBoard.py
#  @author Muneeb Arshad, Shesan Balachandran, Bill Nguyen
#  @title LeaderBoard
#  @date April 4, 2021
from tkinter import *
from random import *
from tkinter import messagebox
import user
import time
import scoreAllocator

ANIMALS_WORD = ['DRBI', 'DGO', 'OENDYK', 'GFRIEFA', 'GLOILARTA', 'TAC', 'EHSOR', 'OLIN', 'MYOEKN', 'EEB', 'KDUC',
                'RGFO', 'TPNLEHEA', 'ORCDCIELO', 'POLNIHD', 'LARLIGO', 'EMSUO', 'EGTRI', 'ABRITB', 'ATR', ]

ANIMALS_ANSWER = ['BIRD', 'DOG', 'DONKEY', 'GIRAFFE', 'ALLIGATOR', 'CAT', 'HORSE', 'LION', 'MONKEY', 'BEE', 'DUCK',
                  'FROG', 'ELEPHANT', 'CROCODILE', 'DOLPHIN', 'GORILLA', 'MOUSE', 'TIGER', 'RABBIT', 'RAT', ]



points = 0
time_countdown = 30


import json
## @brief shuffleWords function
#  @details This function is used to shuffle the given list of words
#  @param words a list of strings
#  @return a list of stings which are the new shuffled words
def shuffleWords(words):
    new_list = []
    for s in words:
        sr = ''.join(sample(s, len(s)))
        new_list.append(sr)
    return new_list

## @brief getWords function
#  @details This function is used to get a list of words based on category and difficulty level
#  @param category is a string representing the desired category
#  @param difficulty is a string representing the desired difficulty level
#  @return a list of stings which represents words based on category and difficulty level
def getWords(category, difficulty):
    with open('data/words.json') as f:
        data = json.load(f)
    return data[category][difficulty]

## @brief main function
#  @details This function is used to start up the game screen to play the game
#  @param category is a string representing the desired category
#  @param difficulty is a string representing the desired difficulty level
#  @param gameMode is a string representing the desired game mode
#  @param username is a string representing the desired username
def main(gameMode, difficulty, username, category):
    global ran_num
    wordsList = getWords(category, difficulty)
    shuffleList = shuffleWords(wordsList)
    print(wordsList)
    print(shuffleList)
    ran_num = randrange(0, (len(shuffleList)))
    jumbled_rand_word = shuffleList[ran_num]
    
    def back():
        global time_countdown
        global points
        points = 0
        time_countdown = 30
        my_window.destroy()
        import main_start
        main_start.start_main_page()

    ## @brief change function
    #  @details This function is used to change the word
    def change():
        global ran_num
        ran_num = randrange(0, (len(shuffleList)))
        word.configure(text=shuffleList[ran_num])
        get_input.delete(0, END)
       
    ## @brief check function
    #  @details This function is used check whether the user guessed the word correctly or incorrectly
    def cheak():
        global points, ran_num
        user_word = get_input.get().lower()
        if user_word == wordsList[ran_num].lower(): 
            if gameMode == "Ranked Game Mode":       
                points = scoreAllocator.addScore(difficulty,points)
                score.configure(text="Score: " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(shuffleList)))
            word.configure(text=shuffleList[ran_num])
            get_input.delete(0, END)
            
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

    ## @brief countdown function
    #  @details This function acts as the timer and countdowns the time until timer is zero
    def countdown():
        global time_countdown,user
        if time_countdown>0:
            timer.configure(text="Timer: " + str(time_countdown))
            time_countdown = time_countdown - 1
            timer.after(1000, countdown)
        elif time_countdown==0:
           
            timer.destroy()
            score.destroy()
            word.destroy()
            submit.destroy()
            change.destroy()
            
            get_input.destroy()
            Label(text=f'Congrats!', bg="#e6fff5",height="2",  font=("Arial",30)).pack()
            Label(text=f'Your Score Is {points}', bg="#e6fff5",height="2",  font=("Arial",30)).pack()
            print("got here", username, points)
            user.updateScore(username,points)

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Quizee-Animals_jumbled_words ")
    my_window.configure(background="#e6fff5")
    my_window.iconbitmap(r'assets/quizee_logo_.ico')
    img1 = PhotoImage(file="assets/back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#e6fff5',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    if gameMode == "Ranked Game Mode":
        timer = Label(
            text="Timer: ",
            pady=10,
            bg="#e6fff5",
            fg="#000000",
            font="Titillium  14 bold"
        )
        timer.pack(anchor="n")

    if gameMode == "Ranked Game Mode":
        score = Label(
            text="Score: 0",
            pady=10,
            bg="#e6fff5",
            fg="#000000",
            font="Titillium  14 bold"
        )
        score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  50 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=change,
    )
    change.pack()

    if gameMode == "Ranked Game Mode":
        countdown()

    my_window.mainloop()
