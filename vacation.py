def hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))

def make_payment(payment, balance):
    new_bal = add_monthly_interest(balance - payment)
    print "You still owe:" + str(new_bal)
    return new_bal
    
new_bill = make_payment(bill /2, bill)
print make_payment(100, new_bill)
	
