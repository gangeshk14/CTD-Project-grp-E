import json


def startpagescrs():
    with open('data.json') as file:
        scores_dict = json.load(file)
    # print(scores_dict['scores'])
    #beginner
    beginnerScores = dict(sorted(scores_dict['scores']['beginner'].items(), key = lambda x:x[1], reverse = True))
    beginnerStr = ""
    for k,v in beginnerScores.items():
        beginnerStr = beginnerStr + "{0} : {1}\n".format(k,v)
    #advanced
    advScores = dict(sorted(scores_dict['scores']['advanced'].items(), key = lambda x:x[1], reverse = True))
    advStr = ""
    for k,v in advScores.items():
        advStr = advStr + "{0} : {1} \n".format(k,v)
    return beginnerScores, advScores