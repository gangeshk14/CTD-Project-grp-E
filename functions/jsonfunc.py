import json


def startpagescrs():
    with open('data.json') as file:
        scores_dict = json.load(file)
    # print(scores_dict['scores'])
    #beginner
    beginnerScores = dict(sorted(scores_dict['scores']['beginner'].items(), key = lambda x:x[1], reverse = True))
    #advanced
    advScores = dict(sorted(scores_dict['scores']['advanced'].items(), key = lambda x:x[1], reverse = True))
    return beginnerScores, advScores

def endpagescr(nameInput,game_mode,score):
    with open('data.json','r') as file:
        scores_dict = json.load(file)
    scores_dict["scores"][game_mode][nameInput] = score
    with open('data.json','w') as file:
        json.dump(scores_dict,file,indent=4)
