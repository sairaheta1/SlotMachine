#collect user input to get deposit from user
def deposit ():
  while True:
    amount = input("How much would you like to deposit? $")
    if not amount.isdigit():
      print("Not valid. Deposit must be a number greater than 0.")
    else:
      amount = int(amount)
      if amount < 0:
        print("Not valid. Deposit must be a number greater than 0.")
      else:
        break
  return amount


deposit()