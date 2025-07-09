#
# program to calculate pay based on:
# cost of gas - miles per gallon and cost of gas
# vehicle wear and tear -  $0.50 to $0.60 per mile
# time and convenience - for example, $15/hour
# MOST IMPORTANTLY, Friendship factor

# cost of gas
miles_per_gallon = 21
cost_of_gas = 2.89
# cost_of_gas = input('What is the cost of gas today? ')
miles_driven = input('How many miles were driven? ')
print('You drove ' + miles_driven + ' miles today!')

total_cost_of_gas = (int(miles_driven) / miles_per_gallon) * cost_of_gas
print(f'Based on {miles_per_gallon} miles per gallon costing ${cost_of_gas} per gallon'
      f', the total cost of gas for today is: ${round(total_cost_of_gas,2)}')\

# vehicle wear and tear $.50 to $.60 per mile
vehicle_wear_tear = int(miles_driven) * .50
print(f'The total vehicle wear and tear charge for today is: ${vehicle_wear_tear}')

# driver's time
driving_time = input('How much time did you spend driving today in hours? ')
print('You spent ' + driving_time + ' hours driving today!')
per_hour_pay = 15.0
time_charge = int(driving_time) * per_hour_pay
print(f'The total time charge for today (at ${per_hour_pay} per hour) is: ${time_charge}')

print(f'The total charges for today are: ${(round(total_cost_of_gas,2) + vehicle_wear_tear + time_charge)}')

