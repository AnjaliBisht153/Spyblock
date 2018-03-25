from spydetails import spy_name,spy_age,spy_rating #importing varibles from spydetails.py
def spy_chat(spy_name,spy_age,spy_rating): #function spy_chat to display menu
    choice = -1 #choice variable set to -1
    print 'Here are your option ' + spy_name
    while choice!=0: #while loop will run until user choose to exit
        print'      MENU        \n 1. Add a status \n 2. Add a friend \n 0. Exit' #printing menu
        choice=input('Enter your choice : ' ) #taking choice input
        if choice==1: #choice 1
            print 'will add a status'
        elif choice==2: #choce 2
            print 'will add a friend'
        elif choice==0: #exit
            print 'Exit'
        else: #for any invalid input
            print 'Invalid input'

print 'Hello..!!' #printing hello
print 'Let\'s get started'
spy_reply=raw_input('Are you anew user? Y/N ' ) #asking the user if he is new user or not
if spy_reply.upper()=='N':
    print 'Welcome back..!! ' +spy_name+'. Your age is '+ str(spy_age)+' and your rating is '+ str(spy_rating)
    spy_chat(spy_name,spy_age,spy_rating) #calling function spy_chat
elif spy_reply.upper()=='Y':
    spy_name = raw_input('What is your spy name? ' ) #take name as input from user
    if spy_name.isspace(): #to check for space input
        print 'Enter a valid name'
    elif spy_name.isdigit(): #to check digit input
        print 'Enter a valid name'
    elif len(spy_name)>=2: #checking for lenght of the string
        print 'Welcome '+ spy_name + ' Glad to have you back with us. ' #concatenating strings
        spy_salutation = raw_input('What should we call you (Mr. or Ms.) ' )
        if spy_salutation == 'Mr.' or spy_salutation == 'Ms.': #using if to check the condition
            spy_name = spy_salutation + " "  + spy_name
            print 'Alright '+spy_name+' I\'d like to know more about you...'
            age=input('What\'s your age ')
            if 50>=age<=15: #nested if statement to check the range of age
                print 'You are not eligible to be a spy'
            else:
                rating=input('What is your rating ' )
                if rating>=7:
                    print 'GOOD SPY'
                elif 7>rating>=5.5: #elif statement for more than one condition
                    print 'AVERAGE SPY'
                elif 5.5>rating>=3.5:
                    print 'Need to work hard..!!'
                else:
                    print 'Who hired you..'
                spy_is_online = True
                print 'Authentication complete. Welcome..!! '+ spy_name +'. Your age is '+ str(age)+' and your rating is '+ str(rating) #typecasting of integer to string
                spy_chat(spy_name,spy_age,spy_rating) #calling function spy_chat

        else:
            print 'Enter a valid salutation'
    else:
        print 'Ooppss! Enter a valid name '

