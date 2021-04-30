bill_id = int(input("Enter bill id: "))
cust_id = int(input("Enter customer id: "))
bill_amt = int(input("Enter bill amount: "))


print("bill amount: %d Customer ID: %d Bill amount: %d" %(bill_id,cust_id,bill_amt))
if bill_amt>=1000:
    updated = bill_amt * 0.05
    bill_amt -=updated
    print("You got a discount of 5%")
    print("Your new bill amount is: ",bill_amt)
elif bill_amt>=500:
    updated = bill_amt * 0.02
    bill_amt -=updated
    print("You got a discount of 2%")
    print("Your new bill amount is: ",bill_amt)

elif bill_amt>0:
    updated = bill_amt * 0.01
    bill_amt -=updated
    print("You got a discount of 1%")
    print("Your new bill amount is: ",bill_amt)
