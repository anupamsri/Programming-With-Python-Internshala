import score_calculator #Importing score_calculator module

#Giving Inputs as dictionary
p1={'name':'Virat Kohli', 'role':'bat', 'runs':112, '4':10, '6':0, 'balls':119, 'field':0} 
p2={'name':'du Plessis', 'role':'bat', 'runs':120, '4':11, '6':2, 'balls':112, 'field':0} 
p3={'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10, 'runs':71, 'field':1} 
p4={'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10, 'runs':45, 'field':0} 
p5={'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34, 'field':0}

players = [p1,p2,p3,p4,p5]  # Making a list of dictionaries so that we can iterate through each dictionary

scores = {}

for i in players:
    if i['role'] == 'bat':
        score = score_calculator.batscore(i)
        scores[i['name']] = score
        print("'name':{},'batscore':{}".format(i['name'],score))
    else:
        score = score_calculator.bowlscore(i)
        scores[i['name']] = score
        print("'name':{},'bowlscore':{}".format(i['name'],score))

max_scorer = max(scores,key=scores.get)

print("The maximum scorer is {} with score {}".format(max_scorer,max(scores.values())))
