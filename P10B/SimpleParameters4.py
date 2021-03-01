def calculateInterest(principal: float, interestRate: float):
    interest = principal * interestRate
    print('Principal: $ %.2f\nInterest Rate: %.2f\nInterest earned: $%.2f' % (principal, interestRate, interest))

calculateInterest(1000, 0.05)