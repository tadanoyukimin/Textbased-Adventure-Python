import random

"""story.py uses the random module to randomly assign a description
to a room when the player uses the Examine option from the menu.
To prevent actual random room descriptions from appearing all the time
the player can only examine each room once, unless the room has a fixed description
like the boss room. It is possible that there are lookalikes in the room although making 
room descriptions unique by popping them once they have been selected (urn) is possible to do.
"""

room_description_list = [
    "Broken pieces of the wall can be found lying on the floor, along with cobwebs that populate themselves throughout the room.",
    "There are scattered skeleton debris around the room.",
    "The room is filled with a weird liquid, possibly from a slime.",
]
boss_room_description = [
    "There is a sense of dread in the air..."
]
def random_room_description():
    random_num = random.randint(0, len(room_description_list))
    return room_description_list[random_num]
