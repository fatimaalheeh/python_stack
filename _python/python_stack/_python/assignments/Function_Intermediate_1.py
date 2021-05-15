
import random  # so we can generate  random number, we imported random
def randInt(min=0, max=100):
    print("Your max is: ",max," and your min is: ",min)
    if max < 0:
        print('The max must be > 0')  # supposly the user entered 0 for the max
    elif min > max:
        # supposly the user entered a vlaue less than min for the max
        print('The max must be > min')
    else:
        if max != 100 and min != 0:
            return round(random.random()*(max-min)+min)
        if min != 0:
            return round(random.random()*(100-min)+min)
        if max != 100:
            return round(random.random()*max)
    return round(random.random()*100)

print( "    here is a random for your pleasure: ",randInt(100,10))
print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))