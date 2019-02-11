# game_outcome.py
# William Ponton
# 2.10.19

# Game calculations===================

#draw_income
def draw_income(slot_1, slot_2, slot_3, draw_earnings):
  # Two of a kind = $5.00
  if ((slot_1 == slot_2) or (slot_1 == slot_3)):
    draw_earnings += 5
    # Three of a kind = $10.00
    if ((slot_1 == slot_2) and (slot_1 == slot_3)):
      draw_earnings += 5
      # All Bell Peppers = $50.00
      if ((slot_1 == 5) and (slot_2 == 5) and (slot_3 == 5)):
        draw_earnings += 40
  return draw_earnings

# clear_draw_earnings
def clear_draw_earnings(draw_earnings):
  draw_earnings = 0
  return draw_earnings

# total_income
def total_income(total_earnings, draw_earnings):
  total_earnings += draw_earnings
  return total_earnings