"""
birthday.py
Author: Rachel Matthew
Credit: none
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name

name=input('Hello, what is your name? ')
bmon=input('Hi {0}, what was the name of the month you were born in? '.format(name))
byear=int(input('And what year were you born in, {0}? '.format(name)))
bday=input('And the day? ')

if bmon=='january' or bmon=='1':
    bmon=='January'
elif bmon=='february' or bmon=='2':
    bmon='February'
elif bmon=='march' or bmon=='3':
    bmon='March'
elif bmon=='april' or bmon=='4':
    bmon='April'
elif bmon=='may' or bmon=='5':
    bmon='May'
elif bmon=='june' or bmon=='6':
    bmon='June'
elif bmon=='july' or bmon=='7':
    bmon='July'
elif bmon=='august' or bmon=='8':
    bmon='August'
elif bmon=='september' or bmon=='9':
    bmon='September'
elif bmon=='october' or bmon=='10':
    bmon='October'
elif bmon=='november' or bmon=='11':
    bmon='November'
elif bmon=='december' or bmon=='12':
    bmon='December'

if bmon==month_name[datetime.today().month] and int(bday)==datetime.today().day:
    statement='Happy birthday!'
elif (bmon=='October') and bday=='31':
    statement='You were born on Halloween!'
else:
    if byear>1979 and byear<1990:
        year='eighties'
    elif byear>1989 and byear<2000:
        year='nineties'
    elif byear<1980:
        year='Stone Age'
    else: 
        year='two thousands'
    if bmon=='December' or bmon=='January' or bmon=='February':
        mo='winter'
    elif bmon=='March' or bmon=='April' or bmon=='May':
        mo='spring'
    elif bmon=='June' or bmon=='July' or bmon=='August':
        mo='summer'
    else:
        mo='fall'
    statement='{0}, you are a {1} baby of the {2}.'.format(name, mo, year)
    
print(statement)
