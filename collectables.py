# Catalogue for adding, modifying, and deleting collectables
import json

# This function opens "collectables.txt" in write mode and writes data_list to it in JSON format.
def save_data(data_list):
    file = open('collectables.txt', 'w')
    json.dump(data_list, file)
    file.close()

try:
    file = open('collectables.txt', 'r')
    data = json.load(file)
    file.close()
except:
    data = []

while True:
    print("\nCollectables Catalogue Admin Program")
    print("[a]dd, [v]iew, [q]uit")
    choice = input('> ').lower()

    if choice == 'a':
        add_collectable = {}

        print("\nCollectable Tag")
        add_collectable['tag'] = input('> ')

        print("\nCollectable Name")
        add_collectable['name'] = input('> ')

        print('\nCollectable Description')
        add_collectable['description'] = input('> ')

        print('\nCollectable Type')
        add_collectable['type'] = input('> ').lower()

        print('\nCollectable Level')
        add_collectable['level'] = input('> ')

        print('\nCollectable Value')
        add_collectable['value'] = input('> ')

        print('\nCollectable DMG Modifier (weapons only)')
        add_collectable['modifier'] = input('> ')

        print('\nCollectable Durability (integer value between 1 and 100)')
        add_collectable['durability'] = input('> ')

        data.append(add_collectable)
        save_data(data)
        print("Collectable added\n")
    
    elif choice == 'v':
        print("\nEnter Collectable Name:")
        scen_name = input('> ').lower()
        for item in data:
            if scen_name in item['name'].lower():
                print(item)
    
    elif choice == 'q':
        break

    else:
        print("Invalid choice")

exit()