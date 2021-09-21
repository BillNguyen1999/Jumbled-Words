## @file scoreAllocator.py
#  @author Muneeb Arshad, Shesan Balachandran, Bill Nguyen
#  @title Score Allocator
#  @date April 4, 2021

## @brief addScore function
#  @details This function is used to allocate score to the user based on difficulty level
#  @param points is an integer representing the number of points
#  @param difficulty is a string representing the desired difficulty level
#  @return an integer representing the total number points in one session
def addScore(difficulty,points):
    if(difficulty == "easy"):
        points += 5
    
    elif(difficulty == "medium"):
        points += 10
    elif(difficulty=="hard"):
        points +=15

    return points 

    
    