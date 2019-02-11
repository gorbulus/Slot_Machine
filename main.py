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
import random
from random import randint
import slot_machine.output_literals
import slot_machine.console_output as co
import slot_machine.game_outcome as go
import slot_machine.slot_machine as sm
import slot_machine.output_literals

# Data structures
slot_machine = {
  1 : "Cherries",
  2 : "Oranges",
  3 : "Plums",
  4 : "Melons",
  5 : "Bells"
}

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
  my_slot = []
  
  # Gambling time~!
  co.game_title()
  rules()
  # Start game?
  engage = co.start_game(engage)
  
  while engage == "y":
    # 'Sentinel' counter is true
    total_plays += 1
    
    # Gameplay
    co.pull_lever()
    
    # Build the 5 slot list
    slot_picks = sm.slot_seed(slot_picks)
    
    # Draw 3 random items from the seeded list
    draw = sm.play_slot(DRAW_MAX, draw, slot_picks)
    
    # Fill slots
    slot_1 = sm.get_slot_1(draw, slot_1)
    slot_2 = sm.get_slot_2(draw, slot_2)
    slot_3 = sm.get_slot_3(draw, slot_3)

    # Get values in slot_machine dict from draw list keys
    my_slot = sm.user_draw(slot_machine, draw, my_slot, slot_1, slot_2, slot_3)
    
    # Reset the draw for another round
    draw = sm.clear_draw(draw)

    # Game outcome/summary
    # Calculate earnings in a single draw
    draw_earnings = go.draw_income(slot_1, slot_2, slot_3, draw_earnings)

    # Calculate total earnings in gameplay
    total_earnings = go.total_income(total_earnings, draw_earnings)

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
    game_exit()
    # Final game summary
    co.total_income_output(total_plays, total_earnings)
    
# Control initiating event
if __name__ == "__main__":
  main()
