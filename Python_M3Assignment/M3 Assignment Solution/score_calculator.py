# functions used for score calculation

def batscore(x):
    runs = x['runs']
    strike_rate = runs/x['balls']
    score = runs//2 + (5 if runs >= 50 else 0) + (10 if runs >= 100 else 0) + (2 if strike_rate >= 80/100 and strike_rate <= 1 else 0) + (4 if strike_rate > 1 else 0) + x['4'] + x['6']*2
    return score
    return {'name':x['name'],'batscore':score}

def bowlscore(x):
    wkts = x['wkts']
    economy_rate = x['runs']/x['overs']
    fields=x['field']
    score = 10*wkts + (10*fields if fields>=1 else 0 ) +(5 if wkts>=3 else 0) + (10 if wkts>=5 else 0) + (4 if economy_rate>=3.5 and economy_rate<=4.5 else 0) + (7 if economy_rate>=2 and economy_rate<3.5 else 0) + (10 if economy_rate<2 else 0)
    return score
    return {'name':x['name'],'bowlscore':score}
