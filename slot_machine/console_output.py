# console_output.py
# William Ponton
# 2.10.19

# Import modules
import * from slot_machine.output_literals 

# Console output======================
# game_title
def game_title():
  return print(DIV_LINE + NEW_LINE + WELCOME + NEW_LINE + DIV_LINE)

# rules
def rules():
  return print(RULES)

# start_game
def start_game(engage):
  engage = str(input(ENGAGE).lower())
  return engage

# pull_lever
def pull_lever():
  return print(NEW_LINE + DIV_LINE + NEW_LINE + LEVER + NEW_LINE)

# draw_output
def draw_output(slot_1, slot_2, slot_3):
  return print(DRAW.format(slot_machine[slot_1], slot_machine[slot_2], slot_machine[slot_3]))

# draw_income_output
def draw_income_output(draw_earnings):
  return print(DIV_LINE + NEW_LINE + EARNED.format(draw_earnings))

# total_earnings
def total_income_output(total_plays, total_earnings):
  return print(NEW_LINE + DIV_LINE + NEW_LINE + PLAY_SUMMARY.format(total_plays, total_earnings) + DIV_LINE)

# game_exit
def game_exit():
  return print(NEW_LINE + DIV_LINE + NEW_LINE + EXIT_MESSAGE)