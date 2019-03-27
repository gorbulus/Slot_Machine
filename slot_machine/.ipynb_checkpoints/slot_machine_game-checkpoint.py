# slot_machine.py
# William Ponton
# 2.10.19

# Game functionality==================

# Import modules
import random
from random import randint
import slot_machine.data_structures as ds

# slot_seed
def slot_seed(slot_picks):  
  slot_list = list(range(1, 6))
  for n in slot_list:
    slot_choice = random.choice(slot_list)
    slot_picks += [slot_choice]
  return slot_picks

# def clear_slot_picks
def clear_slot_picks(slot_picks):
    del slot_picks[:]
    return slot_picks

# play_slot
def play_slot(DRAW_MAX, draw, slot_picks):
  for n in range(DRAW_MAX):
    slot_seed(slot_picks)
    draw.append(str(random.choice(slot_picks)))
  slot_picks = clear_slot_picks(slot_picks)
  return draw

# get_slot_1
def get_slot_1(draw, slot_1):
  slot_1 = int(draw[0])
  return slot_1

# get_slot_2
def get_slot_2(draw, slot_2):
  slot_2 = int(draw[1])
  return slot_2

# get_slot_3
def get_slot_3(draw, slot_3):
  slot_3 = int(draw[2])
  return slot_3

#create_draw
def create_draw(draw, slot_1, slot_2, slot_3):
  draw = [slot_1, slot_2, slot_3]
  return draw

# clear_draw
def clear_draw(draw):
    
  # clears the draw list for the next round
  del draw[:]
  return draw

# clear_draw_earnings
def clear_draw_earnings(draw_earnings):
    draw_earnings = 0
    return draw_earnings