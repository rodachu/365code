import random

# variables
# distance to border, distance of guards from user, and user health
border_dist = 30 
guard_dist = -10 #guards cover 1-5miles per turn
guard_run = 0 #how far the guards run in a specific turn, changes every move

#moving costs 1 health, full speed costs 2 health;
#when health == 0, game over
user_health = 4 
health = ("filler", "You need a break", "You could use a rest", "You can still go on", "You're feeling great!")

guard_report = ("filler ")


print"""
Prison Break!
You jumped the prison fence and escaped. The guards are chasing you.
The border is 30 more miles away. Cross the border and you're free."""

# main while loop
quitGame = False
while quitGame == False:
    print """
A. Drink from your water #health +1-2
B. Run at decent speed  # covers 1-6 miles, health -1
C. Run at full speed #covers  6-12, health -2
D. Status check
Q. Quit
"""
    move1 = raw_input() 
    if move1.upper() == "Q": #user decides to quit, loop ends
        quitGame = True

    elif move1.upper() == "A": #increase user_health, guards move, are they close to/caught user?
        guard_run = random.randint(1,6) #guard movement
        guard_dist += guard_run #guard distance = -distance + movement
        
        #guard movement (are they close? did they catch user?)
        if guard_dist >=0:
            print "While napping, the guards catch up. \n You're going away for a long time buddy"
            quitGame = True
        elif guard_dist >-5:
            user_health += random.randint(1,3)
            print "You rest and recuperate. \n The border is %i miles away" % border_dist
            print "The guards are getting close..."
        elif guard_dist <=-5:
            user_health += random.randint(1,3)
            print "You rest and recuperate. \n The border is %i miles away" % border_dist

    elif move1.upper() == "B": #user runs, guards run, user health ok? guard distance? border distance?
         #user and guard runs    
        moderate_run = random.randint(1,7)
        guard_run = random.randint(1,4)

        #border and guard distance
        border_dist -= moderate_run 
        guard_dist -= moderate_run - guard_run       
        
        #is health low/zero? did guards catch up? then present user results
        user_health -= 1
        if user_health <= 0:
            print "your legs cramp up, you fall down, and pass out."
            quitGame = True  
        elif user_health == 1:
            if border_dist <= 0:
                print "Sayonara! \n You run %i miles and cross the border, starting a new life as a papaya farmer." % moderate_run
                quitGame = True
            elif guard_dist >=0:
                print "the guards got you."
                quitGame = True
            elif guard_dist >-5:
                print "You run %i miles. The border is %i away." % (moderate_run, border_dist)
                print "The guards are close and you're very tired. Oh oh"
            elif guard_dist <=-5:
                print "You run %i miles. The border is %i miles away. You should rest now" % (moderate_run, border_dist)
                
        elif user_health == 2:
            if border_dist <= 0:
                print "Sayonara! \n You run %i miles and cross the border, starting a new life as a papaya farmer." % moderate_run
                quitGame = True
            elif guard_dist >=0:
                print "the guards got you."
                quitGame = True
            elif guard_dist >-5:
                print "You run %i miles. The border is %i miles away." % (moderate_run, border_dist)
                print "The guards are close and you're a bit tired, but you can go on"
            elif guard_dist <=-5:
                print "You run %i miles. The border is %i miles away. You're a bit tired" % (moderate_run, border_dist)
           
        elif user_health >= 3:
            if border_dist <= 0:
                print "Sayonara! \n You run %i miles and cross the border, starting a new life as a papaya farmer." % moderate_run
                quitGame = True
            elif guard_dist >=0:
                print "the guards got you."
                quitGame = True
            elif guard_dist >-5:
                print "You run %i miles. The border is %i miles away." % (moderate_run, border_dist)
                print "The guards are close, keep running"
            elif guard_dist <=-5:
                print "You run %i miles. The border is %i miles away." % (moderate_run, border_dist)
    
    elif move1.upper() == "C": #user runs full speed, guards run, border dist changes, user health changes
        #user and guard run
        fast_run = random.randint(6,14)
        guard_run = random.randint(1,5)
        
        #border and guard distance
        border_dist -= fast_run 
        guard_dist -= fast_run - guard_run
        
        #is health low/zero? did guards catch up? then present user results
        user_health -= random.randint(1,3)
        if user_health <= 0:
            print "your legs cramp up, you fall down, and pass out."
            quitGame = True  
        elif user_health == 1:
            if border_dist <= 0:
                print "Sayonara! \n You run %i miles and cross the border, starting a new life as a papaya farmer." % fast_run
                quitGame = True
            elif guard_dist >=0:
                print "the guards got you."
                quitGame = True
            elif guard_dist >-5:
                print "You run %i miles. The border is %i away." % (fast_run, border_dist)
                print "The guards are close and you're very tired. Oh oh"
            elif guard_dist <=-5:
                print "You run %i miles. The border is %i miles away. You should rest now" % (fast_run, border_dist)
                
        elif user_health == 2:
            if border_dist <= 0:
                print "Sayonara! \n You run %i miles and cross the border, starting a new life as a papaya farmer." % fast_run
                quitGame = True
            elif guard_dist >=0:
                print "the guards got you."
                quitGame = True
            elif guard_dist >-5:
                print "You run %i miles. The border is %i miles away." % (fast_run, border_dist)
                print "The guards are close and you're a bit tired, but you can go on"
            elif guard_dist <=-5:
                print "You run %i miles. The border is %i miles away. You're a bit tired" % (fast_run, border_dist)
           
        elif user_health >= 3:
            if border_dist <= 0:
                print "Sayonara! \n You run %i miles and cross the border, starting a new life as a papaya farmer." % fast_run
                quitGame = True
            elif guard_dist >=0:
                print "the guards got you."
                quitGame = True
            elif guard_dist >-5:
                print "You run %i miles. The border is %i miles away." % (fast_run, border_dist)
                print "The guards are close, keep running"
            elif guard_dist <=-5:
                print "You run %i miles. The border is %i miles away." % (fast_run, border_dist)

    
    elif move1.upper() == "D": #status check
        print "You are %i miles away from the border, %s , the guards are" % (border_dist, health[user_health])
        

#i'm gonna get a tuple range error if user health > 4
#not sure how to have tuple for guard distance, since guard distance can be a range
        
#guard dist, movement distance and all that stuff needs to changed to improve gameplay, but that's beyond this exercise.
        
        
