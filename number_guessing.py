# Number guessing game

import random
import os
import time

list1 = [str(i) for i in range(1,1001)]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def effect(text, end='\n', delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end, end='')

def ask_num():
  while True:
        effect("Enter a number (1-1000) or 'q' to quit: ")
        number = input('')
        if number in list1:
            return int(number)
        if number=='q':
            return None
        else:
            continue


if __name__ == '__main__':
  
  correct_ans = random.randint(1,1000)
  while True:
    guess = ask_num()

    if guess is None:
      effect("Game exited.")
      exit()

    if guess == correct_ans:
      effect("🎉 Yay! You've got it!")
      input('Enter to leave. ')
      break

    elif abs(guess - correct_ans) <= 2:
        hint = "Try a bit higher!" if guess < correct_ans else "Try a bit lower!"
        effect(f"🔥 Ooh, really close, you got this! {hint}")

    elif abs(guess - correct_ans) <= 10:
        hint = "Go a little higher!" if guess < correct_ans else "Go a little lower!"
        effect(f"✨ Pretty close, you're almost there! {hint}")

    elif abs(guess - correct_ans) <= 100:
        hint = "Guess higher!" if guess < correct_ans else "Guess lower!"
        effect(f"❌ Wrong number, but you're not far. Try again! {hint}")

    elif abs(guess - correct_ans) > 500:
        hint = "Way too low!" if guess < correct_ans else "Way too high!"
        effect(f"💀 Oof, you're way off. {hint}")

    else:
        hint = "Try higher." if guess < correct_ans else "Try lower."
        effect(f"🙁 Not quite. {hint}")
