# Dungeon Map Generation
import numpy as np

# arr_m = np.arange(12).reshape(4, 3)
#  [[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]
#   [ 9 10 11]] What the dungeon map looks like. 
#  Each indices in the nested list is a room. Transitioning from one nested list to another is a door.
#  Obviously, transitioning from one indices to another is a door. 
#  For example, there is a door between room 0 and room 3 etc.
#  Player starts from index 0, exit is the max or highest value index, like arr_m[4][2]
#  Using zip would allow us to find the max integer

# max_arr_m = list(map(max, zip(*arr_m))) # this will give the list that has the biggest integer
# print(max_arr_m)
# print(max(max_arr_m))

dungeon_map_start = [0, 1, 2]
dungeon_map_second = np.arange(12).reshape(4, 3)
dungeon_map_final = np.arange(6)