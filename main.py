#setting up constants for max lines, bet, and min bet
MAX_LINES = 3

def main():
  balance = deposit()
  bet_lines = get_num_lines()
  bet = get_bet(balance, bet_lines)
  print(bet)


def valid_bet(bet, balance):
  if bet > balance:
    return False
  return True

#ask user how much they would like to bet on each line
def get_bet(balance, bet_lines):
  while True:
    amountToBet= input("How much would you like to bet? $")
    if not amountToBet.isdigit():
      print("Not valid. Bet must me a number greater than 0.")
    else:
      totalBet = bet_lines * int(amountToBet)
      if not valid_bet(totalBet, balance):
        print(f"Not valid. Your bet requires a minimum balance of ${totalBet}. You currently have ${balance}.") # totalBet, balance
      else:
        break
  return totalBet

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
#NEXT THING TO WORK ON:
 # get the amount they want to bet on each line
 # check to see if the amount they want to bet * lines is within their current balance
  