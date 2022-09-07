# Catalogue for adding, modifying, and deleting scenarios

import json

# This function opens "scenarios.txt" in write mode and writes data_list to it in JSON format.
def save_data(data_list):
    file = open('scenarios.txt', 'w')
    json.dump(data_list, file)
    file.close()

try:
    file = open('scenarios.txt', 'r')
    data = json.load(file)
    file.close()
except:
    data = []

while True:
    print("\nScenario Catalogue Admin Program")
    print("[a]dd, [v]iew, [q]uit")
    choice = input('> ').lower()

    if choice == 'a':
        add_scenario = {}

        print("\nScenario Name")
        add_scenario['name'] = input('> ').lower()

        print('\nType scenario details')
        text = input('> ')
        add_scenario['text'] = text.replace('\\n', '\n')

        print('\nEntry words (words used that enter this senario)')
        print('Type words and press Enter to add. When finished, just press Enter')
        entry_words = []
        while True:
            word = input('> ').lower()
            if word != "":
                entry_words.append(word)
                print('Entry word added')
            else:
                break
        add_scenario['entry words'] = entry_words
        print('All entry words added')

        print('\nExit words (words that trigger another scenario)')
        print('Type words and press Enter to add. When finished, just press Enter')
        exit_words = []
        while True:
            word = input('> ').lower()
            if word != "":
                exit_words.append(word)
                print('Exit word added')
            else:
                break
        add_scenario['exit words'] = exit_words
        print('All exit words added')

        print('\nWeapons (items that can be found in scenario)')
        print('Type items and press Enter to add. When finished, just press Enter')
        items = []
        while True:
            word = input('> ').lower()
            if word != "":
                items.append(word)
                print('Weapon added')
            else:
                break
        add_scenario['weapons'] = items
        print('All weapons added')

        print('\nArmour (items that can be found in scenario)')
        print('Type items and press Enter to add. When finished, just press Enter')
        items = []
        while True:
            word = input('> ').lower()
            if word != "":
                items.append(word)
                print('Armour added')
            else:
                break
        add_scenario['armour'] = items
        print('All armour added')

        data.append(add_scenario)
        save_data(data)
        print("Scenario added\n")

        print('\nItems (items that can be found in scenario)')
        print('Type items and press Enter to add. When finished, just press Enter')
        items = []
        while True:
            word = input('> ').lower()
            if word != "":
                items.append(word)
                print('Item added')
            else:
                break
        add_scenario['items'] = items
        print('All items added')
    
    elif choice == 'v':
        print("\nEnter Scenario Name:")
        scen_name = input('> ').lower()
        for item in data:
            if scen_name in item['name']:
                print(item)
    
    elif choice == 'q':
        break

    else:
        print("Invalid choice")

exit()