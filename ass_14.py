bill_id = int(input("Enter bill id: "))
cust_id = int(input("Enter customer id: "))
bill_amt = int(input("Enter bill amount: "))

if cust_id>=101 and cust_id<=1000:
    if bill_amt>=500:
        updated = bill_amt * 0.1
        bill_amt -=updated
        print("You got a discount of 10%")
        print("Your new bill amount is: ",bill_amt)
    
    else:
        print("You got zero discount")
        print("Your  bill amount is: ",bill_amt)
else:
    print("Invalid customer id")