print 'Hello..!!'
print 'Let\'s get started'
spy_name = raw_input('What is your spy name? ' ) #take name as input from user
if len(spy_name)>=2: #checking for lenght of the string
    print 'Welcome '+ spy_name + ' Glad to have you back with us. ' #concatinating strings
    spy_salutation = raw_input('What should we call you (Mr. or Ms.) ' )
    if spy_salutation == 'Mr.' or spy_salutation == 'Ms.': #using if to check the condition
        spy_name = spy_salutation + " "  + spy_name
        print 'Alright '+spy_name+' I\'d like to know more about you...'
        age=input('What is your age ')
        if 50>=age<=15: #nested if statement to check the range of age
            print 'You are not eligible to be spy'
        else:
            rating=input('What are your rating ' )
            if rating>=7:
                print 'GOOD SPY'
            elif 7>rating>=5.5: #elif statement for mpre than one condition
                print 'AVERAGE SPY'
            elif 5.5>rating>=3.5:
                print 'Need to work hard..!!'
            else:
                print 'Who hired you..'
            spy_is_online = True
            print 'Authentication complete. Welcome ' + spy_name + ' age: ' + str(age) + ' rating: ' + str(rating) #typecasting of integer to string
    else:
        print 'Enter a valid salutation'
elif spy_name.issapce(): #to check for space
    print 'Please enter a valid name.'
else:
    print 'Ooppss! Enter a valid name '

