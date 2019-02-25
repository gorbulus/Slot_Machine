# statistical_analysis.py
# William Ponton
# 2.24.19
# slot_machine game statistical analysis and visualizations.

'''
Adding graphical stats based on user game play data.
1. Frequency of each item (Cherries, Oranges, Plums, Melons, Bell Peppers).
2. Frequency of win category (2 of a kind, 3 of a kind, all Bells).
3. Winnings/turn exactly (for n user turns, graph each turn result)
4. Average draw/dollar (Scatterplot and line of best fit (linear regression)).
'''

# Import modules
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import slot_machine.data_structures as ds

#Functions

# item_frequency - bar graph of item counts overall per game
def item_frequency(item_count, draw):
    for item in draw:
        item_count += item
    return item_count

# win_type_frequency - bar graph of Win Types overall per game
def win_type_frequency():
    pass

# wins_per_turn - line plot of each turn's results per game
def wins_per_turn():
    pass

# draw_average - scatterplot and linear regression of the entire game outcome
def draw_average():
    pass


