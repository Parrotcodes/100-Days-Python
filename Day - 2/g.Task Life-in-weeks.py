#Life in Weeks and in days

age = input('What is yor current age?')

current_age = int(age)
total_years= 90

remain_age_years = 100 - current_age
remain_days = remain_age_years*365
remain_weeks = remain_age_years*52
remain_months = remain_age_years*12

message = (f'You have {remain_days} days,{remain_weeks} weeks and {remain_months} months left.')
print(message)




      
