from spydetails import spy_name,spy_age,spy_rating #importing varibles from spydetails.py
def add_friend(): #function to add friend
    #taking friends detail input
    frnd_name=raw_input('What is your friend\'s  name : ' )
    frnd_age=input('What is the age : ' )
    frnd_rating=input('What are the rating : ' )
    if len(frnd_name)>0 and 15<frnd_age<50 and frnd_rating>spy_rating: #checking for spy details
        #adding the details in the respective lists
        friend_name.append(frnd_name)
        friend_age.append(frnd_age)
        friend_rating.append(frnd_rating)
        friend_is_online.append(True)
    else:
        print'The friend cannot be added '
    return len(friend_name) #returning the lenght of list friend_name


def add_status(c_status): #function to add status
    if c_status!=None: #checking if the status is none
        print'Your current status is : '+c_status
    else:
        print'You don\'t have any status currently'
    existing_status=raw_input ('You want to add from old status? Y/N ' )#taking new status from user
    if existing_status.upper()=='N':
        new_status=raw_input('Enter your status : ' )
        if len(new_status)>1:
            updated_status=new_status
            old_status.append(updated_status) #adding the new status in the status list
        else:
            print'Enter a valid status'
    elif existing_status.upper()=='Y':#checking if user want to addan old status
        serial_no=1
        for status in old_status: #printing the old status
            print str(serial_no)+'. '+status
            serial_no=serial_no+1
        status_choice=input('Enter your choice : ')
        updated_status=old_status[status_choice-1] #updating the status
    return updated_status #returning the new updated status


def spy_chat(spy_name,spy_age,spy_rating): #function spy_chat to display menu
    current_status=None
    choice = -1 #choice variable set to -1
    print 'Here are your option ' + spy_name
    while choice!=0: #while loop will run until user choose to exit
        print'      MENU       \n 1. Add a status \n 2. Add a friend \n 0. Exit' #printing menu
        choice=input('Enter your choice : ' ) #taking choice input
        if choice==1:#choice 1
            current_status=add_status(current_status)
            print'Updated status is : '+current_status
        elif choice==2: #choice 2
            friend=1 #counter to print no. of friends
            no_of_friends=add_friend() #calling function add friend to add friend
            print ' You have ' + str(no_of_friends) + ' number of friends' #printing number of friends
            for i in friend_name:
                print str(friend)+'. '+i
                friend=friend+1
        elif choice==0: #exit
            print 'Exit'
        else: #for any invalid input
            print 'Invalid input'

print 'Hello..!!' #printing hello
print 'Let\'s get started'
old_status=['Spy plots are hard,really hard','Spy is such a short ugly word','I\m a girl who enjoy hrslf vry much..smtyms I lose,smtyms I win','At home'] #list of status
#list to store friend details
friend_name=['Rahul']
friend_age=[20]
friend_rating=[5.3]
friend_is_online=[True]
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

