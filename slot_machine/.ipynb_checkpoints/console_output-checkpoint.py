# console_output.py
# William Ponton
# 2.10.19

# Import modules
import slot_machine.output_literals as ol
import slot_machine.data_structures as ds

# Console output======================
# game_title
def game_title():
  return print(ol.DIV_LINE + ol.NEW_LINE + ol.WELCOME + ol.NEW_LINE + ol.DIV_LINE)

# rules
def rules():
  return print(ol.RULES)

# start_game
def start_game(engage):
  engage = str(input(ol.ENGAGE).lower())
  return engage

# pull_lever
def pull_lever():
  return print(ol.NEW_LINE + ol.DIV_LINE + ol.NEW_LINE + ol.LEVER + ol.NEW_LINE)

# draw_output
def draw_output(slot_1, slot_2, slot_3):
  return print(ol.DRAW.format(ds.slot_machine[slot_1], ds.slot_machine[slot_2], ds.slot_machine[slot_3]))

# draw_income_output
def draw_income_output(draw_earnings):
  return print(ol.DIV_LINE + ol.NEW_LINE + ol.EARNED.format(draw_earnings))

# total_earnings
def total_income_output(total_plays, total_earnings):
  return print(ol.NEW_LINE + ol.DIV_LINE + ol.NEW_LINE + ol.PLAY_SUMMARY.format(total_plays, total_earnings) + ol.DIV_LINE)

# game_exit
def game_exit():
  return print(ol.NEW_LINE + ol.DIV_LINE + ol.NEW_LINE + ol.EXIT_MESSAGE)