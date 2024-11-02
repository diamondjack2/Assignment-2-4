# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here

stateTax = salary * .065
federalTax = salary * .28
dependentDeduction = salary * .025 * numDependents
takeHomePay = stateTax + federalTax + dependentDeduction

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))