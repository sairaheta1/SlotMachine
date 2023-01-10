import sys, random, time
from datetime import datetime
random.seed(datetime.now().timestamp())

#setting up constants for max lines, bet, and min bet
MAX_LINES = 3
MIN_BET = 1

ROWS = 3
COLS = 3

#symbols within the reels of the slot machine
symbol_count = {
  "A": 3,
  "E": 4,
  "I": 6,
  "O": 8, 
  "U": 10
}
#the monetary values for the symbols
symbol_multipliers = {
  "A": 100,
  "E": 10, 
  "I": 5,
  "O": 2,
  "U": 1
}

slotMachineValues = [] #possible values for slot reels

def main():
  getStartingChoice()
  balance = deposit()

  while True:
    betLines = get_num_lines(balance)
    bet = get_bet(balance, betLines)
    print(f"Your total bet is: ${bet}")

    reels = None
    reels = spin_machine(reels)
    winnings = count_winnings(bet, reels)
    balance = update_balance(balance, bet, winnings)
    
    print(f"Your current balance is ${balance}.")
    
    keepPlaying(balance)
    if balance == 0:
      while balance == 0:
        newDeposit = input("Please deposit more money to keep playing or press (q) to quit. $ ")
        try:
          balance += int(newDeposit)
        except:
          if newDeposit == "q":
            sys.exit(f"You left with ${balance}. Goodbye.")
          print(f"{newDeposit} is not valid.")

def getStartingChoice():
  userChoice = input("Welcome to Sam Slots. Get 3 in a row to win. Press (c) to continue or (q) to quit. ") #need to add input validators
  while not (userChoice == "c" or userChoice == "q"):
    userChoice = str(input("Welcome to Sam Slots. Get 3 in a row to win. Press (c) to continue or (q) to quit. ")) #need to add input validators
  if userChoice == "q":
    sys.exit("Goodbye.")
#collect user input to get deposit from user
def deposit ():
  while True:
    amount = input("How much would you like to deposit? $")
    if not amount.isdigit():
      print("Not valid. Deposit must be a number greater than 0.")
    else:
      amount = int(amount)
      if amount <= 0:
        print("Not valid. Deposit must be a number greater than 0.")
      else:
        break
  return amount

def get_num_lines(balance): #ask user how many lines they would like to bet on
  while True:
    lines = input("How many lines would you like to bet on? Please enter a value between 1-" + str(MAX_LINES) + ". ")

    if not lines.isdigit():
      print("Please enter a valid number of lines for your bet.")
    else:
      lines = int(lines)     
      if lines > MAX_LINES or lines < 1 or lines > balance:
        if lines > balance:
          print(f"You can only bet a maximum of {balance} lines with ${balance}.")
        print("Please enter a valid number of lines for your bet.")
      else:
        break
  return lines

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

def valid_bet(bet, balance):
  if bet > balance:
    return False
  return True

def spin_machine(reels):
  spin = input("Press (s) to spin the machine. ")
  while (spin != "s"):
    spin = input("Press (s) to spin the machine. ")
  
  create_list_values()
  reels = create_cols()
  print_slot_machine(reels)
  return reels
    
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
  time.sleep(2)
  print()
  for row in range(ROWS):
    print("|", end="")
    for col in reels:
      print(" " + col[row], end=" |")
    print()
  print()

def RNG(max_range):
  return random.randrange(0, max_range)
  
def count_winnings(bet, reels):
  winCount = 0
  amountWon = 0
  for row in range(ROWS):
    currentSymbol = reels[0][row]
    rowCount = 0
    for line in range(COLS):
      if reels[line][row] != currentSymbol:
        break
    else:
        winCount += 1 #need to add a way to add multiplier for the symbol
        amountWon += bet * symbol_multipliers[currentSymbol]
  print(f"You won on {winCount} rows.")
  print(f"You won ${amountWon}.")
  
  return amountWon

def update_balance(balance, bet, winnings):
  return (balance - bet) + winnings

def keepPlaying(balance):
  keepPlaying = input("Press (p) to play or (q) to quit. ")
  while not (keepPlaying == "p" or keepPlaying == "q"):
    keepPlaying = input("Press (p) to play or (q) to quit. ")
  if keepPlaying == "q":
    sys.exit(f"You left with ${balance}. Goodbye.")

main()