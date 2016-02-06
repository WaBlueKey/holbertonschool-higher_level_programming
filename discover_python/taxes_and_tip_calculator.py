"""Welcome to this awesome program that I, Zee Adams, wrote to help you figure out those pesky taxes and tip amounts when you are dining out. This program was written in Python. I am a Full Stack Software Engineer in training. The program will ask for your meal price before taxes and then it will ask for the tax amount as a percentage. It will then take the combined meal + tax price and add the tip percentage that you will input. Finally, you will get your total price for the meal to the 6th decimal point."""

print "Welcome to the taxes and tip calculator!"  # This print command will shows a welcome message to the user.

pretax_meal = float(input("What is the price before tax? "))  # The user is asked to input the meal price before taxes.  

tax = float(input("What are the taxes? (in %) "))   # The user is asked to input the tax rate.

tip = float(input("What do you want to tip? (in %) "))   # The user is then asked to input the tip amount they wish to add as a % of the total amount meal+tax.

total_price = (pretax_meal + (pretax_meal * (tax/100))) * (1 + (tip/100))   # The total is calculated using the variables. We add 1 when multiplying the tip to get the total and not the percentage. 

print "The price you need to pay is: $%.6f." % total_price   # Final price should print including taxes and tip. The notation .6f prints to the 6th decimal position. 
