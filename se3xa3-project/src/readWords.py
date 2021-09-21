## @file readWords.py
#  @author Muneeb Arshad, Shesan Balachandran, Bill Nguyen
#  @title Read Words
#  @date April 4, 2021
import json

## @brief getWords function
#  @details This function is used to get a list of words based on category and difficulty level
#  @param category is a string representing the desired category
#  @param difficulty is a string representing the desired difficulty level
#  @return a list of stings which represents words based on category and difficulty level
def getWords(category, difficulty):
    with open('data/words.json') as f:
        data = json.load(f)
    return data[category][difficulty]

# print(getWords("animals", "medium"))