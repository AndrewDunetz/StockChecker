import requests
from datetime import datetime
import time

while True:
	# Current time in local system
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Current Time =", current_time)

	# Checks to see if stock market is open
	start = '09:30:00'
	end = '16:00:00'
	if current_time > start and current_time < end:
	    print('Stock market is open')
	else:
	    print('Stock market is not open')
	    exit()

	# Current date in local system
	print(datetime.today().strftime('%Y-%m-%d'))
	date = datetime.today().strftime('%Y-%m-%d')

	API_KEY = '25J3D7DD57MPDMVR'

	# Stock that you wish to track
	stockTicker = 'FB' # input('Enter your desired stock ticker: ')

	url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stockTicker + '&apikey='

	r = requests.get(url + API_KEY)

	# Prints all values for stock
	if (r.status_code == 200):
	    #print(r.json())
		result = r.json()
		dataForAllDays = result['Time Series (Daily)']
		dataForSingleDate = dataForAllDays[date]
	print (stockTicker)
	print ('Open: ' + dataForSingleDate['1. open'])
	print ('High: ' + dataForSingleDate['2. high'])
	print ('Low: ' + dataForSingleDate['3. low'])
	print ('Close: ' + dataForSingleDate['4. close'])
	print ('Volume: ' + dataForSingleDate['5. volume'])

	openValue = 'Open: ' + dataForSingleDate['1. open']
	high = 'High: ' + dataForSingleDate['2. high']
	low = 'Low: ' + dataForSingleDate['3. low']
	close = 'Close: ' + dataForSingleDate['4. close']
	volume = 'Volume: ' + dataForSingleDate['5. volume']

	# Tells user if stock is up or down and by how much
	closeNumber = float(dataForSingleDate['4. close'])
	#print (closeNumber)
	openNumber = float(dataForSingleDate['1. open'])
	#print (openNumber)
	difference = float("{0:.2f}".format(abs(closeNumber - openNumber)))
	difference = str(difference)

	if (closeNumber > openNumber):
		print ('Stock is up $' + difference + ' today')

	if (closeNumber < openNumber):
		print ('Stock is down $' + difference + ' today')

	time.sleep(30)

# # Asks user if they want to send data
# askToSendData = input("Would you like to send this data?")

# if askToSendData == "no":
#     exit()

# # Emails data to desired email address
# import smtplib, ssl

# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# sender_email = "stocksprogram@gmail.com"
# receiver_email = "rplesnak@yahoo.com"
# password = input("Type your password and press enter:")
# message = """\
# Subject: Stock notification

# """ + stockTicker + " " + openValue + " " + high + " " + low + " " + close + " " + volume + """ Stock Checker has noticed recent activity for """ + stockTicker

# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)