## @file user.py
#  @author Muneeb Arshad, Shesan Balachandran, Bill Nguyen
#  @title User
#  @date April 4, 2021
import json

filename = "data/userData.json"
## @brief addUser function
#  @details This function is used to add user to database
#  @param username is a string representing the selected username
def addUser(username):
    # Check if user exists
    jsonFile = open(filename, "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    userData = data['userdata']
    userExists = False
    for user in userData:
        if(user['username'] == username):
            userExists = True 
        
  

    # Add user to the json
    if(not userExists):
        print("Adding user")
        jsonFile = open(filename, "w+")
        temp = data['userdata'] 
        newUser = {"username":username, 
                "score": 0
        }  
        temp.append(newUser) 
        newJson = {"userdata":temp}
        jsonFile.write(json.dumps(newJson))
        
## @brief updateScore function
#  @details This function is used to update the score of selected user to the database
#  @param username is a string representing the selected username
#  @param score is an integer that represents the score of the user
def updateScore(username,score):
    jsonFile = open(filename, "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close()

    
    user = data['userdata']
    for i in range(len(user)):
        if(user[i]['username'] == username and user[i]['score'] < score):
            user[i]['score'] = score
            jsonFile = open("data/userData.json", "w")
            newJson = {"userdata":user}
            json.dump(newJson,jsonFile)
           
