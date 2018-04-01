from spydetails import spy #importing varibles from spydetails.py
from steganography.steganography import Steganography #importing steganography library
from datetime import datetime #importing datetime library

def select_frnd(): #function to select a friend
    print'select your friend'
    serial_no=1
    for frnd in friends: #print list of friends
        print str(serial_no) + '. ' + frnd['name']
        serial_no=serial_no+1
    user_selected_frnd=input('Enter your choice : ' ) #user selecting friend
    user_selected_frnd_index=user_selected_frnd-1
    return user_selected_frnd_index #to return the selected friend index

def send_message(): #function for sending message
    selected_friend=select_frnd() #calling the select_friend function
    original_image=raw_input('What is the name of original image : ' ) #take name of original image as input
    secret_text=raw_input('Enter your secret message : ' ) #entering the secret message
    output_path='output.jpg' #name of the image after encoding the message
    Steganography.encode(original_image,output_path,secret_text) #calling encode() functions to encode message in image
    print'Message Encoded'
    #dictionary to store details of a message
    new_chat={'message':secret_text,
              'time':datetime.now(),
              'send by me':True}
    friends[selected_friend]['chats'].append(new_chat) #appending chats in the friends list
    print'Your secret message is ready'

def read_message(): #function for reading message
    selected_friend=select_frnd() #calling select friend function
    output_path=raw_input('Which image you want to decode? ' ) #the name of the to be decoded
    secret_text=Steganography.decode(output_path) #calling decode() function to decode
    print'The decoded message is '+ secret_text #printing the secret text
    #dictionary to store details of message
    new_chat={'message':secret_text,
              'time':datetime.now(),
              'send by me':False}
    friends[selected_friend]['chats'].append(new_chat)

def add_friend(): #function to add friend
    #taking friends details input
    frnd={'name':'',
          'age':0,
          'ratings':0.0,
          'is_online':True,
          'chats':[]} #dictionary for details of friend
    frnd['name']=raw_input('What is your friend\'s name : ' )
    frnd['age']=input('What is the age : ' )
    frnd['rating']=input('What are the rating : ' )
    if len(frnd['name'])>0 and 15<frnd['age']<50 and frnd['rating']>spy['rating']: #checking for spy details
        #adding the details in the respective lists
        friends.append(frnd) #appending friend details in friends list
    else:
        print'The friend cannot be added '
    return len(friends) #returning the lenght of list friend_name


def add_status(c_status): #function to add status
    if c_status!=None: #checking if the status is none
        print'Your current status is : '+c_status #printing the current status
    else:
        print'You don\'t have any status currently'
    existing_status=raw_input ('You want to add from old status? Y/N ' )#taking new status from user
    if existing_status.upper()=='N':
        new_status=raw_input('Enter your status : ' ) #taking new status as input
        if len(new_status)>0:
            updated_status=new_status
            old_status.append(updated_status) #adding the new status in the status list
        else:
            print'Enter a valid status'
    elif existing_status.upper()=='Y':#checking if user want to add an old status
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
        print'      MENU       \n 1. Add a status \n 2. Add a friend \n 3. Send a message \n 4. Read a message \n 0. Exit' #printing menu
        choice=input('Enter your choice : ' ) #taking choice input
        if choice==1:#choice 1
            current_status=add_status(current_status)
            print'Updated status is : '+current_status
        elif choice==2: #choice 2
            friend_no=1 #counter to print no. of friends
            no_of_friends=add_friend() #calling function add friend to add friend
            print ' You have ' + str(no_of_friends) + ' number of friends' #printing number of friends
            for i in friends: #printing name of friends
                print str(friend_no)+'. '+i['name']
                friend_no=friend_no+1
        elif choice==3: #choice 3
            send_message() #calling send_message() function
        elif choice==4: #choice 4
            read_message() #calling read_message() function
        elif choice==5: #to read a user's message
            print'will read a user\'s message'
        elif choice==0: #exit
            print 'Exit'
        else: #for any invalid input
            print 'Invalid input'

f=datetime.now() #calling function now() from datetime library
print f.strftime('%b %d %Y %H:%M:%S') #use of stringtimeformat
print 'Hello..!! WELCOME TO SPYCHAT' #printing hello
print 'Let\'s get started'
old_status=['Spy plots are hard,really hard','Spy is such a short ugly word','I\m a girl who enjoy hrslf vry much..smtyms I lose,smtyms I win','At home'] #list of old status
friends=[{'name' : 'Rahul','age' : 20,'rating' : 5.8,'is_online' : True,'chats' : []},{'name' : 'Vinod','age' : 20,'rating' : 4.7,'is_online' : True,'chats' : []}] #list to store friend details
spy_reply=raw_input('Are you anew user? Y/N ' ) #asking the user if he is new user or not
if spy_reply.upper()=='N':
    print 'Welcome back..!! ' +spy['name']+'. Your age is '+ str(spy['age'])+' and your rating is '+ str(spy['rating'])
    spy_chat(spy['name'],spy['age'],spy['rating']) #calling function spy_chat
elif spy_reply.upper()=='Y':
    spy={'name' : '','age' : 0,'rating' : 0.0} #dictionary to store spy details
    spy['name'] = raw_input('What is your spy name? ' ) #take name as input from user
    if spy['name'].isspace(): #to check for space input
        print 'Enter a valid name'
    elif spy['name'].isdigit(): #to check for digit input
        print 'Enter a valid name'
    elif len(spy['name'])>=2: #checking for lenght of the string
        print 'Welcome '+ spy['name'] + ' Glad to have you back with us. ' #concatenating strings
        spy_salutation = raw_input('What should we call you (Mr. or Ms.) ' )
        if spy_salutation == 'Mr.' or spy_salutation == 'Ms.': #using if to check the condition
            spy_name = spy_salutation + " "  + spy['name']
            print 'Alright '+spy_name+' I\'d like to know more about you...'
            spy['age']=input('What\'s your age ')
            if 50>=spy['age']<=15: #nested if statement to check the range of age
                print 'You are not eligible to be a spy'
            else:
                spy['rating']=input('What is your rating ' ) #taking rating as input
                if spy['rating']>=7:
                    print 'GOOD SPY'
                elif 7>spy['rating']>=5.5: #elif statement for more than one condition
                    print 'AVERAGE SPY'
                elif 5.5>spy['rating']>=3.5:
                    print 'Need to work hard..!!'
                else:
                    print 'Who hired you..'
                spy_is_online = True
                print 'Authentication complete. Welcome..!! '+ spy['name'] +'. Your age is '+ str['age']+' and your rating is '+ str['rating'] #typecasting of integer to string
                spy_chat(spy['name'],spy['age'],spy['rating']) #calling function spy_chat

        else:
            print 'Enter a valid salutation'
    else:
        print 'Ooppss! Enter a valid name '

