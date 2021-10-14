Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def gurubala(month,date):
	if month > 12 or date >31:
		print("Invalid month or Date ")
	else:
		print("valid month and Date")

		
>>> gurubala(1,11)
valid month and Date
>>> gurubala(13,32)
Invalid month or Date 
>>> gurubala(13,30)
Invalid month or Date 
>>> gurubala(1,35)
Invalid month or Date 
>>> 
