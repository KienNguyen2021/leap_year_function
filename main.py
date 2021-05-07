def is_leap(year) :
  if year % 4 ==0 :
    if year % 100 ==0 :
      if year % 400 == 0:
       return True        # or print (" Leap year ")
      else :
        return False      # or print ("Not leap year " )
    else :
      return True     # or print ("Leap year")    
  else :
     return False       #  or print ("Not leap year " )

def days_in_month(year, month):

  if month >12 or month <1 :
      return "Invalid month"

  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   

  if is_leap(year) and month ==2 :
     
     return 29      # if  leap year is true, february has 29 days
     
  return month_days[month -1]   # -1 because 28 in month_day is index 1, but month =2 = 28, so month -1


  #do not change any of the code above :
year = int (input("Enter a year :"))   
month  =int (input("Enter a month : "))
days  = days_in_month (year, month)

print (days)
