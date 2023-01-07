import sys
import random
from datetime import datetime
random.seed(datetime.now().timestamp())
#setting up constants for max lines, bet, and min bet
MAX_LINES = 3
MIN_BET = 1

ROWS = 3
COLS = 3

#symbols within the reels of the slot machine
symbol_count = {
  "A": 2,
  "E": 4,
  "I": 6,
  "O": 8, 
  "U": 10, 
}

slotMachineValues = [] #possible values for slot reels

def create_list_values():
  for symbol, count in symbol_count.items():
    slotMachineValues.extend([symbol] * count) #add each symbol to the list for a specified amount of times

def create_cols():
  valuesToChooseFrom = slotMachineValues.copy()
  slotMachine = [];
  for col in range(COLS):
    x = []
    slotMachine.append(x)
    for row in range(ROWS):
      value = RNG(len(valuesToChooseFrom))
      x.append(valuesToChooseFrom[value])
      del valuesToChooseFrom[value]
  return slotMachine

def print_slot_machine(reels):
  print(reels)
  for row in range(ROWS):
    print("|", end="")
    for col in reels:
      print(" " + col[row], end=" |")
    print()

def count_winnings(reels):
  winCount = 0
  for row in range(ROWS):
    currentSymbol = reels[0][row]
    rowCount = 0
    for line in range(COLS):
      if reels[line][row] != currentSymbol:
        break
    else:
        winCount += 1 #need to add a way to add multiplier for the symbol
  return winCount

def update_balance(balance, bet, winnings):
  return (balance - bet) + winnings


def RNG(max_range):
  return random.randrange(0, max_range)

def main():
  userChoice = input("Welcome to Sam Slots. Get 3 in a row to win. Press (c) to continue or (q) to quit. ") #need to add input validators
  while not (userChoice == "c" or userChoice == "q"):
    userChoice = str(input("Welcome to Sam Slots. Get 3 in a row to win. Press (c) to continue or (q) to quit. ")) #need to add input validators
  #need to add while loop to keep playin
  if userChoice == "q":
    sys.exit("Goodbye")

  balance = deposit()
  betLines = get_num_lines()
  bet = get_bet(balance, betLines)
  print(f"Your total bet is: ${bet}")
  print("Press (s) to spin the machine.") #need to make sure machine only spins on (s) press
  create_list_values()
  reels = create_cols()
  print_slot_machine(reels)
  winnings = count_winnings(reels)
  newBalance = update_balance(balance, bet, winnings)
  print(f"You won on {winnings} rows. You won $MONEY") #ADD WIN AMOUNT
  print(f"Your new balance is ${newBalance}.") #UPDATE BALANCE



def valid_bet(bet, balance):
  if bet > balance:
    return False
  return True

#ask user how much they would like to bet on each line
def get_bet(balance, bet_lines):
  while True:
    amountToBet= input("How much would you like to bet on each line? $")
    if not amountToBet.isdigit():
      print("Not valid. Bet must me a number greater than 0.")
    else:
      if int(amountToBet) < MIN_BET:
        print(f"Not valid. Your bet must be greater than the minimum value required, ${MIN_BET}.")
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

#NEXT TO WORK ON:
  #adding multipliers to game
  #adding or subtracting win/loss from current balance
  #more options for user