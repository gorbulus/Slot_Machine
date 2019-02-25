# main.py
# William Ponton
# 2.10.19
# Slot machine program implementation

'''
A Python program which simulates a "free" slot machine which displays a random combination of 3 of the following items (as text):

      Cherries, Oranges, Plums, Melons, and Bells

        If none of the items match, the user wins nothing.
        If only two of the items match, the user wins $5
        If all three items match, the user wins $10
        If the user matches 3 Bells, the user wins $50
'''

# Import modules
import csv
import random
from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt
import slot_machine.output_literals
import slot_machine.console_output as co
import slot_machine.game_outcome as go
import slot_machine.slot_machine_game as sm
import slot_machine.output_literals as ol
import slot_machine.data_structures as ds
import slot_machine.statistical_analysis as sa

CSV_STATS = "statistics.csv"


# Main function
def main():
  # Locals
  draw_earnings = 0 
  total_earnings = 0
  total_plays = 0
  engage = ""
  slot_1 = "" 
  slot_2 = "" 
  slot_3 = ""
  slot_picks = []
  draw = []

  #Statistical locals
 
  
  # Gambling time~!
  co.game_title()
  co.rules()
  # Start game?
  engage = co.start_game(engage)
  
  while engage == "y":
    # 'Sentinel' counter is true
    total_plays += 1
    
    # Gameplay
    co.pull_lever()
    
    # Build the 5 slot list
    slot_picks = sm.slot_seed(slot_picks)
    print(slot_picks)
    
    # Draw 3 random items from the seeded list
    draw = sm.play_slot(ol.DRAW_MAX, draw, slot_picks)
    print(draw)
    
    # Fill slots
    slot_1 = sm.get_slot_1(draw, slot_1)
    print(slot_1)
    slot_2 = sm.get_slot_2(draw, slot_2)
    print(slot_2)
    slot_3 = sm.get_slot_3(draw, slot_3)
    print(slot_3)
    
    # Reset the draw for another round
    draw = sm.clear_draw(draw)

    # Game outcome/summary
    # Calculate earnings in a single draw
    draw_earnings = go.draw_income(slot_1, slot_2, slot_3, draw_earnings)
    print(draw_earnings)

    # Calculate total earnings in gameplay
    total_earnings = go.total_income(total_earnings, draw_earnings)
    print(total_earnings)
    
    # plot draw searnings and turns
    with open(CSV_STATS, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["Slot 1", "Slot 2", "Slot 3"])
        filewriter.writerow([slot_1, slot_2, slot_3])
    
    # Console output of draw and winnings
    co.draw_output(slot_1, slot_2, slot_3)

    # Single draw winnings output
    co.draw_income_output(draw_earnings)
    
    # Cumulative earnings in gameplay
    co.total_income_output(total_plays, total_earnings)

    # Clear draw earnings for next round
    draw_earnings = sm.clear_draw_earnings(draw_earnings)

    # Try again?
    engage = co.start_game(engage)
  else:
    # Exit & game summary
    co.game_exit()
    # Final game summary
    co.total_income_output(total_plays, total_earnings)
    
# Control initiating event
if __name__ == "__main__":
  main()
