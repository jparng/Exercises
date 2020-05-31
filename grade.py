score = input("enter a score between 0.0 and 1.0 ")
def computegrade(x):
    try:
        x = float(x)
        if x >= 0.9 and x <= 1.0:
            print('A')
        elif x >= 0.8 and x < 0.9:
            print('B')
        elif x >= 0.7 and x < 0.8:
            print('C')
        elif x >= 0.6 and x < 0.7:
            print('D')
        elif x <= 0.5 and x > 0:
            print('F')
        elif x > 1 or x == 0:
            print('Bad score')
    except:
        print('Bad score')
        
        
computegrade(score)
