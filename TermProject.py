#TermProject.py
#Zodiac Calculator

def retrieve_DOB():
#this requires the user input of their DOB
	month=int(input("Please enter the month you were born in numerical form (1-12):"))
	day= int(input("Please enter the day you were born (1-31):"))
	return month, day
	    
def validation(month,day):
#this is used to validate whether the input was received correctly to establish a zodiac sign based on the integers gathered from the user
	if month <1 or month >12:
	    return False
#days in months
	days_in_month={
	    1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
	}
#manual check for days in month
	if day<1 or day> days_in_month[month]:
	    return False
	return True

def Zodiac_Calculation(month,day):
#here we take the correct integers and establish their zodiac sign based on parameters
	if(month==3 and day >=21) or (month==4 and day <=19):
	    return "Aries"
	if(month==4 and day>=20) or (month==5 and day <=20):
	    return "Taurus"
	if (month==5 and day >=21) or (month==6 and day <=20):
	    return "Gemini"
	if (month==6 and day >=21) or (month==7 and day <=22):
	    return "Cancer"
	if (month==7 and day >=23) or (month==8 and day <=22):
	    return "Leo"
	if (month==8 and day >=23) or (month==9 and day <=22):
	    return "Virgo"
	if (month==9 and day >=23) or (month==10 and day <=22):
	    return "Libra"
	if (month==10 and day >=23) or (month==11 and day <=21):
	    return "Scorpio"
	if (month==11 and day >=22) or (month==12 and day <=21):
	    return "Sagittarius"
	if (month==12 and day >=22) or (month==1 and day <=19):
	    return "Capricorn"
	if (month==1 and day >=20) or (month==2 and day<=18):
	    return "Aquarius"
	if (month==2 and day >=19) or (month==3 and day<=20):
	    return "Pisces"
	else:
	    return "Invalid date"

def main():
	print("Zodiac Calculator")
	month,day= retrieve_DOB()
	if not validation(month,day):
	    print("Invalid user input.")
	    return

	sign=Zodiac_Calculation(month,day)
	print("Your zodiac is:", sign)

if __name__=="__main__":
	main()


   	
		