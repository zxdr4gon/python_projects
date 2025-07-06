# Number guessing game

import random
import sleep
import sys
import time

def typewriter(text, delay=0.03):
# Prints the text in a typewriter effect, +/- delay to make faster/slower
  for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline at the end
