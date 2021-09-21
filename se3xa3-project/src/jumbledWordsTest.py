import pytest
import json
import user
import leaderBoard
import scoreAllocator


class TestUser:
    def test_addUser(self):
        username = "testing"
        user.addUser(username)
        jsonFile = open("data/userData.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close()    
        userList = data['userdata']
        addedUser = [d['username'] for d in userList if d['username'] == username]
        assert len(addedUser) == 1
        assert addedUser[0] == username
    
    def test_updateUser(self):
        username = "testing"
        score = 50
        user.addUser(username)
        user.updateScore(username, score)
        jsonFile = open("data/userData.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close()    
        userList = data['userdata']
        addedScore = [d['score'] for d in userList if d['username'] == username]
        assert len(addedScore) == 1
        assert addedScore[0] == score
    
    def test_keepHighestUserScore(self):
        username = "testing"
        score = 50
        lowerScore = 40
        user.addUser(username)
        user.updateScore(username, score)
        user.updateScore(username, lowerScore)
        jsonFile = open("data/userData.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close()    
        userList = data['userdata']
        addedScore = [d['score'] for d in userList if d['username'] == username]
        assert len(addedScore) == 1
        assert addedScore[0] == score

class TestGame:
    def test_correct_word_list_request(self):
        targetList = ["eye", "ear", "leg", "jaw", "arm"]
        testList = []
        with open('data/words.json') as f:
            data = json.load(f)
            testList = data['bodyparts']['easy']
        
        assert targetList == testList

    def test_incorrect_word_list_request(self):
        targetList = ["eye", "ear", "leg", "jaw", "arm"]
        testList = []
        with open('data/words.json') as f:
            data = json.load(f)
            testList = data['bodyparts']['medium']
        
        assert targetList != testList
    
    def test_score_allocator_easy(self):
        points = 0
        assert 5 == scoreAllocator.addScore('easy', points)

    def test_score_allocator_medium(self):
        points = 0
        assert 10 == scoreAllocator.addScore('medium', points)

    def test_score_allocator_hard(self):
        points = 0
        assert 15 == scoreAllocator.addScore('hard', points)

    def test_wordValidator(self):
        ran_num = 1
        wordsList = ["eye", "ear", "leg", "jaw", "arm"]
        user_word = 'ear'
        assert user_word == wordsList[ran_num].lower()

class TestLeaderboard:
    def test_leaderboard_size(self):
        topUsers = leaderBoard.getLeaderboard()
        print()
        assert len(topUsers) <= 10
    
    def test_leaderboard_sorted(self):
        topUsers = leaderBoard.getLeaderboard()
        assert topUsers[0][1] >= topUsers[1][1]
    
    def test_leaderboard_topScorer(self):
        username = "leaderboardTest"
        score = 99999
        user.addUser(username)
        user.updateScore(username, score)
        topUsers = leaderBoard.getLeaderboard()
        assert topUsers[0][0] == username

    
    def test_leaderboard_topScorer(self):
        username = "leaderboardTest"
        score = 99999
        user.addUser(username)
        user.updateScore(username, score)
        topUsers = leaderBoard.getLeaderboard()
        assert topUsers[0][1] == score
        
        

    

