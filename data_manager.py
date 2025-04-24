# data_manager.py
"""
Data Manager Module for CropPilot
Author: Ramandeep Singh
Date of Creation: April 14, 2025 
Purpose: Manages the saving and loading of crop data and lists.
Phase: 2 (Data Integration)
"""

# import json for handling .json format
# import os to check file existence
import json
import os 

# where crop data will be stored
FILE_CROP = "data/crops.json"

## saves the list of crops to a JSON file, takes in a list of crop dictionaries
def save_crops_to_file(crops):
    
    # open and handle file with error-handling using try-except
    try:
        # open file in write mode
        with open(FILE_CROP, "w") as file:
            # convert list of crop dictionaries to JSON and write to file
            json.dump(crops, file, indent=4) # Indent=4 makes file readable
        # print confirmation message
        print("Crops saved successfully.")
    except Exception as e:
        # if there is any error, print message 
        print(f"Failed to save crops: {e}")

## loads crop from JSON file, and returns them as a list of dictionaries,
def load_crops_from_file():

    # check if file exists before opening 
    if not os.path.exists(FILE_CROP):
        print("No saved crops found. Creating empty list.")
        return [] # return empty list
    
    # open and handle file with error-handling using try-except
    try:
        # open file in read mode 
        with open(FILE_CROP, "r") as file:
            # load and return the list of crops from file 
            crops = json.load(file)
            print("Crops loaded successfully.")
            return crops 
    except Exception as e:
        # if there is any error, print message 
        print(f"Failed to save crops: {e}")
        return [] # return empty list
