# create variables of different types
day_of_week = "Monday"
current_week = 1
current_day_of_week = 1
total_course_weeks = 16
total_course_days_per_week = 5

# call the print function using the variables and some operators
# we also use the str() function to convert integers to strings

print("Today is " + day_of_week + ", Week " + str(current_week) 
      + " Day " + str(current_day_of_week) + " of CodeClan")

# another example

def weeks_to_go():
  weeks_left = total_course_weeks - current_week
  days_left = total_course_days_per_week - current_day_of_week
  print(f"Only {weeks_left} weeks and {days_left} days to go!")
    

def motivate_me():
  print("We got this!! You're doing great!!!")


weeks_to_go()
motivate_me()