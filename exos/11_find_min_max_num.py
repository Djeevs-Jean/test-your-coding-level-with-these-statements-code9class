import random 

def find_min_max_num(x=5, y=200):
    INTERVAL = list(range(x,y+1))
    random.shuffle(INTERVAL)

    min = max = INTERVAL[0]
    for i in INTERVAL:
        if i > max: max = i
        elif i < min: min = i
    print( f"{max = }, {min = }" )
