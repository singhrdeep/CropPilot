# crop_manager.py
"""
Crop Manager Module for CropPilot
Author: Ramandeep Singh
Date of Creation: April 14, 2025
Purpose: Functions for adding, removing, editing and displaying crops.
Phase: 2 (Data Integration)
"""

## core of CropPilot, used to create user for crop details, calculates profit (in USD or CAD), and returns a dictionary of data.
def create_crop():

    # print the section title 
    print("\nAdd New Crop:")
    print("-------------------")

    # ask user for currency preference 
    currency = input("Select currency (CAD or USD): ").upper() # convert to uppercase
    if currency not in ["CAD", "USD"]: # handle incorrect input
        print("Invalid currency, selecting CAD.") 
        currency = "CAD"
    
    # set symbol for display and exchange rate for conversion 
    symbol = "$" if currency == "CAD" else "US$"

    ## static Exchange Rates (Courtesy of Bank of Canada, as of April 14, 2025)
    USD_TO_CAD = 1.4359 
    CAD_TO_USD = 0.7095

    # ask user for crop name and category 
    name = input("Crop name: ") # example: "eggplants"
    category = input("Category: ") # example: "legumes"

    # enter data with error-handling using try-except
    try: 
        # prompt for numeric data to use for calculations
        cost = float(input(f"Cost to plant ({currency}): ")) # example: 50.00
        yield_kg = float(input("Expected yield: (kg): ")) # example: 100.0 
        price_kg = float(input(f"Market price per kg ({currency}): ")) # example: 2.50
    except ValueError:
        # print an error message
        print("Invalid input, please enter numeric values.") 
        return None
    
    ## since internal calculations are done via CAD, convert values (if in USD) into CAD
    if currency == "USD":
        cost *= USD_TO_CAD 
        price_kg *= USD_TO_CAD 

    # calculations 
    revenue = yield_kg * price_kg # calculate revenue 
    profit = revenue - cost # calculate cost 

    # return a dictionary with crop info
    # all price figures formatted to 2 decimal points
    crop = {
        "name": name, # crop name
        "category": category, # crop type/category 
        "cost": round(cost, 2), # total planting cost 
        "yield_kg": yield_kg, # expected harvest weight in kg
        "price_kg": round(price_kg, 2), # market price per kg
        "revenue": round(revenue, 2), # total expected revenue 
        "profit": round(profit, 2), # total expected profit
        "currency": "CAD" # all internal values stored in CAD
    }

    # show confirmation message 
    print(f"Crop '{name}' added.")
    print(f"Estimated profit: {symbol}{profit:.2f} (internally stored as CAD)")

    # return dictionary
    return crop


## allows the user to delete a crop by selecting its number from the list
def delete_crop(crops):

    # check if there are any crops to delete 
    if not crops:
        print("\nNo crops to delete.")
        return 
    
    print("\nDelete a Crop:")
    print("-------------------")

    # enumerate each crop in the list 
    for i, crop in enumerate(crops, start=1):
        name = crop["name"] # crop name
        category = crop["category"] # crop category 
        print(f"{i}. {name} ({category})")  # display crop entry

    try: 
        # prompt user to enter information with error-handling using try-except
        choice = int(input("\nEnter the number of the crop to delete: ")) 
        
        # ensure number is within range 
        if 1 <= choice <= len(crops):
            # pop returns and removes the item
            deleted_crop = crops.pop(choice - 1)  
            # print deleted crop name and category
            print(f"Deleted: {deleted_crop['name']} ({deleted_crop['category']})")

        else: 
            # if user typed in wrong number
            print("Invalid number, please choose a valid crop number.")
    
    except ValueError:
        # if user typed in something the program can't recognize 
        print("Please enter a valid number.")


## displays all crops the user has added so far
def view_crops(crops):

    # if list is empty, notify user
    if not crops:
        print("No crops to display.")
        return
    
    # print each crop in list with profit 
    print("Current Crops:\n")
    print("-------------------")

    # loop through all crops and print their details 
    for i, crop in enumerate(crops, start=1):
        # import values from each crop dictionary
        name = crop["name"]
        category = crop["category"]
        cost = crop["cost"]
        revenue = crop["revenue"]
        profit = crop["profit"]
        currency = crop["currency"]

        # set proper symbol based on currency type 
        symbol = "$" if currency == "CAD" else "US$"

        # print each crop, formatted
        print(f"{i}. {name} ({category})")
        print(f"   Cost:     {symbol}{cost:.2f}")
        print(f"   Revenue:  {symbol}{revenue:.2f}")
        print(f"   Profit:   {symbol}{profit:.2f}")
        print("-" * 35)  # Separator 
