#Project - 1 Day -2
#Tip Calculator

print('Welcome to the tip calculator!')

Bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give 10,12 or 15?'))
split = int(input('How many people to split the bill?'))

per_tip = tip / 100
tip_cal = Bill * per_tip
result = Bill + tip_cal


split_bill_person = result / split
#Final_Bill = split_bill_person #26.2356666686
#Final_Bill = round(split_bill_person,2) #26.23 or 26.4_

Final_Bill = '{:.2f}'.format(split_bill_person)#floating point formats -> 26.40

print(f'Each person should pay: ${Final_Bill}')#$26.40

#--Project Done!--

