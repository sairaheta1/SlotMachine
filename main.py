#setting up constants for max lines, bet, and min bet
MAX_LINES = 3
def main():
  deposit()
  get_num_lines()


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

def get_num_lines(): #ask user how many lines they would like to bet on
  while True:
    lines = input("How many lines would you like to bet on? Please enter a value between 1-" + str(MAX_LINES) + ". ")

    if not lines.isdigit():
      print("Please enter a valid number of lines for your bet.")
    else:
      lines = int(lines)
      if lines > MAX_LINES or lines < 1:
        print("Please enter a valid number of lines for your bet.")
      else:
        break
  return lines



main()