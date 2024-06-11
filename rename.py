import json
from pathlib import Path
import os
import easygui as eg

with open("data.json", "r") as jsonFile:
    data = json.load(jsonFile)

template = """event.create('food_tech_name').displayName(food_tech_name).food(food => {
		food
    		.hunger(6)
    		.saturation(6)
//      		.effect('speed', 600, 0, 1)
//      		.removeEffect('poison')
//      		.alwaysEdible()//Like golden apples
//      		.fastToEat()//Like dried kelp
//      		.meat()//Dogs are willing to eat it
	})"""
counter = data["counter"]

def prepareTextures():
    global counter
    for path in Path('dirtimages').rglob('*.png'):
        os.rename(path, f'readyimages/rpg_resourse{counter}.png')
        counter+=1
        updateCounter()

def addItem():
    f = open("output.txt", "w")
    for path in Path('readyimages').rglob('*.png'):
        rs = f"event.create('{path.name[:len(path.name)-4]}').displayName(\"{path.name[:len(path.name)-4]}\")"
        os.rename(path, f"finishedimages/{path.name}")
        f.write("\t" + rs + "\n")
    f.close()

def addItemFood():
    f = open("outputFood.txt", "w")
    for path in Path('readyimages').rglob('*.png'):
        rs = template.replace("food_tech_name", f"food_{path.name[:len(path.name)-4]}")
        os.rename(path, f"finishedimages/{path.name}")
        f.write("\t" + rs + "\n")
    f.close()
def updateCounter():
    data["counter"] = counter
    with open("data.json", "w") as jsonFile:
        json.dump(data, jsonFile)


def main():
    global food
    msg = "Click the button to select category or action"
    title = "Simple GUI"
    button_list_settings = ["Items", "Food", "Close"]
    button_list = ["PrepareTextures", "AddItems", "Close"]
    
    while True:
        choice = eg.buttonbox(msg, title, choices=button_list_settings)
        
        if choice == "Items":
            item_choice = eg.buttonbox("Select an action for Item Adder", "Items adder", choices=button_list)
            if item_choice == "PrepareTextures":
                prepareTextures()
            elif item_choice == "AddItems":
                addItem()
            elif item_choice == "Close":
                break
        elif choice == "Food":
            food_choice = eg.buttonbox("Select an action for Food adder", "Food adder", choices=button_list)
            if food_choice == "PrepareTextures":
                prepareTextures()
            elif food_choice == "AddItems":
                addItemFood()
            elif food_choice == "Close":
                break
        elif choice == "Close":
            break

if __name__ == "__main__":
    main()