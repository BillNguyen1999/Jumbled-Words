## @file leaderBoard.py
#  @author Muneeb Arshad, Shesan Balachandran, Bill Nguyen
#  @title LeaderBoard
#  @date April 4, 2021
from tkinter import *
from random import *
from tkinter import ttk
from tkinter import messagebox
import time
import json

## @brief getScores function
#  @details This function is used to get all the scores from the userData.json file
#  @return a list of users and their scores
def getScores():
    users=[]
    with open('data/userData.json') as f:
        data = json.load(f)
    userData = data['userdata']
    for user in userData:
        users.append((user['username'],user['score']))
    return users

## @brief getLeaderboard function
#  @details This function is used to gets the top 10 highest scores
#  @return a list with the top 10 users
def getLeaderboard():
    users = getScores()
    # Sort users according to the scores
    users.sort(key=lambda x: x[1], reverse=True)
    # Get top 10 users
    topUsers = users[0:10]
    return topUsers

## @brief show function
#  @details function is used to display the leaderboard
def show():

    # Styling for the leaderboard
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0,bg="#e6fff5", font=('Calibri', 11)) # Modify the font of the body

 
    # Leaderboard title
    Label(text="Leaderboard", bg="#e6fff5",height="2",  font=("Arial",30)).grid(row=1,column=1,padx=55)
    
    # create Treeview with 3 columns
    cols = ('Position', 'Name', 'Score')
    listBox = ttk.Treeview(columns=cols, show='headings', style="mystyle.Treeview")

    topUsers = getLeaderboard()
    # Add users to the board
    for i, (name, score) in enumerate(topUsers, start=1):
        listBox.insert("", "end", values=(i, name, score))
    
    
    # set column headings and column size
    for col in cols:
        listBox.heading(col, text=col)
        listBox.column(col,width=120,stretch=True)    
    listBox.grid(row=2, column=1)
    