# importing os for building directories
import os



# constant variables
MAIN = "gen"



def start():
    if not os.path.exists(MAIN):
        # Create a new directory because it does not exist
        os.makedirs(MAIN)