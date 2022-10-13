#Getting user input
name = (str(input("\nEnter your last name: ")))
airline = (float(input("Enter Airline Fare: ")))
nights = (int(input("Enter number of nights: ")))
USD = (int(input("Enter US Dollars to Naira: ")))


#printing expense report and airline cost
name = name.capitalize()
print("\n" + name + "'s Expense Report\n")
airline = "{:,.2f}".format(airline)
print("Airline Fare = $" + str(airline))

#printing hotel cost
hotel = nights * 117
hotel = "{:,.2f}".format(hotel)
print("Hotel Expenses = $" + str(hotel))

#printing total cost for hotel and airline
total = float(hotel) + float(airline)
total = "{:,.2f}".format(total)
print("Total = $" + str(total))

#printing converted currency
print("\nCurrency Converter")
Naira = (USD * 381)
Naira = "{:,.2f}".format(Naira)
print("$" + str(USD) + " U.S. Dollars = $" + str(Naira))

#printing processing fees
Fee = 0.03
Fee = "{:,.0%}".format(Fee)
fee = ((USD * 0.03) + USD)
fee = "{:,.2f}".format(fee)
print("Processing Fee: " + Fee + " = $" + str(fee))

#printing penalty rate
Rate = 0.05
Rate = "{:,.0%}".format(Rate)
rate = ((USD * 0.05) + USD)
rate = "{:,.2f}".format(rate)
print("Penalty Rate: " + Rate + " = $" + str(rate))



