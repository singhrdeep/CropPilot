# _main.py
"""
Main for CropPilot
Author: Ramandeep Torotane
Date of Creation: April 14, 2025 
Purpose: CLI interface for the CropPilot program.
Phase: 2 (Data Integration)
"""

## import functions from other modules 
from crop_manager import create_crop, view_crops, delete_crop # creating, viewing and deleting crops
from data_manager import save_crops_to_file, load_crops_from_file # file saving and loading crops

## displays main menu options 
def menu_interface():
    
    print("\nCropPilot Command-Line Interface")
    print("1. Add a new crop")
    print("2. View all crops")
    print("3. Delete a crop")
    print("4. Save and exit") 

## main function that runs the program
def main():

    # load previously saved crops (or empty list file)
    crops = load_crops_from_file()

    # while-loop for menu 
    while True:
        menu_interface() # show user options
        choice = input("\nChoose an option (1-4): ").strip() # remove spaces from input 

        # if user chooses option 1
        if choice == "1":
            # add new crop 
            new_crop = create_crop() # call function from crop_manager 
            
            # add crop if input was not valid
            if new_crop:
                crops.append(new_crop)

        # if user chooses option 2
        elif choice == "2":
            # view all crops added so far by calling function
            view_crops(crops)

        # if user chooses option 3
        elif choice == "3":
            delete_crop(crops)

        # if user chooses option 4
        elif choice == "4":
            # save crops to file and exit program 
            save_crops_to_file(crops)
            print("Goodbye!")
            break # exit loop

        # if input not recognized
        else: 
            print("Invalid option.")

# gets called only if file is run directly
if __name__ == "__main__":
    main()