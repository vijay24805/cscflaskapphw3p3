
from coreapp import app
from flask import request
import calendar
import datetime

app.debug=True

@app.route('/', endpoint="new")
def index():
    page = """
    <DOCTYPE! html>
    <html lang="en-US">
    <head>
    <title>Find Day App</title>
    <meta charset=utf-8">
    </head>
    <body>
    <h1> Find the Day of the Week</h1>
    
    <form action="/dow" method="GET">
    month
    <select name="month">
	
	<option value="1">1
	<option value="2">2
	<option value="3">3
	<option value="4">4
	<option value="5">5
	<option value="6">6
	<option value="7">7
	<option value="8">8
	<option value="9">9
	<option value="10">10
	<option value="11">11
	<option value="12">12
    </select>
    
   day
    <select name="day">
	
	<option value="1">1
	<option value="2">2
	<option value="3">3
	<option value="4">4
	<option value="5">5
	<option value="6">6
	<option value="7">7
	<option value="8">8
	<option value="9">9
	<option value="10">10
	<option value="11">11
	<option value="12">12
	<option value="13">13
	<option value="14">14
	<option value="15">15
	<option value="16">16
	<option value="17">17
	<option value="18">18
	<option value="19">19
	<option value="20">20
	<option value="21">21
	<option value="22">22
	<option value="23">23
	<option value="24">24
	<option value="25">25
	<option value="26">26
	<option value="27">27
	<option value="28">28
	<option value="29">29
	<option value="30">30
	<option value="31">31
    </select>
    
    year
    <select name="year">
	
	<option value="2010">2010
	<option value="2011">2011
	<option value="2012">2012
	<option value="2013">2013
	<option value="2014">2014
	<option value="2015">2015
    </select>
    
    <input type="submit" value="submit" name="submit">
    </form>
    </body>
    </html>
    """   
    return page


@app.route('/dow',methods=['GET','POST'],endpoint="newn")
def index():
    
	if request.method=='GET':
		mnth=request.args.get('month','')
		
		day= request.args.get('day','')
		yr= request.args.get('year','')
		if day.isdigit():
		        yr = int(yr)
		        mnth = int(mnth)
		        day = int(day)
			try:
			 dayIs=datetime.date(yr,mnth,day).weekday()
	   		 
			 page = """
   			 <DOCTYPE! html>
   			 <html lang="en-US">
   			 <head>
   			 <title>Find Day App</title>
   			 <meta charset=utf-8">
    			 </head>
   			 <body>
   			 <h1>The Day of the week is:</h1>
			 <p>
			 """
			 page2 = """
			 
			 </p>
			 </body>
			 </html>
			 """
			 return page + str(display(dayIs)) + page2
                        except Exception as e:
			 print e

		else:
			 page = """
   			 <DOCTYPE! html>
   			 <html>
   			 <head>
   			 <title>Find Day App</title>
   			 <meta charset=utf-8">
    			 </head>
   			 <body>
   			 <h1>The Day of the week is:</h1>
			 <p>Error:Missing, incomplete, or incorrect input.</p>
			 </body>
			 </html>
			 """
			 
			 return page

		
	else:
		return 'Invalid request method'

def display(daynum):
	if daynum==0:
		return 'Monday'
	elif daynum==1:
		return 'Tuesday'
	elif daynum==2:
		return 'Wednesday'
	elif daynum==3:
		return 'Thursday'
	elif daynum==4:
		return 'Friday'
	elif daynum==5:
		return 'Saturday'
	elif daynum==6:
		return 'Sunday'
	else:
		return 'Not a valid day'















