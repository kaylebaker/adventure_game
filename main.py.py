# Main GUI application for adventure game

import tkinter as tk
from tkinter import ttk
import json

class MainApplication(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)
        master.title("Adventure Game")
        master.geometry("800x600")
        master.resizable(False, False)

        # Game variables that are modified via funtions
        self.max_hp = 10
        self.current_scenario = "intro"
        self.item_list = []

        # Call functions to render and start game
        self.create_frames()
        self.create_stats()
        self.create_inventory()
        self.initialise_game()
        

#-------------------------------------------------FUNCTIONS DEFINED BELOW-------------------------------------------------#

    def create_frames(self):
        self.left_frame = tk.Frame(self.master)
        self.left_frame.pack(side = 'left', ipadx=5)
        self.right_frame = tk.Frame(self.master)
        self.right_frame.pack(side = 'left', padx = 10)
        self.text_box = tk.Text(self.right_frame, width = 75, height = 30, wrap = 'word')
        self.text_box.pack()
        self.action_lbl = tk.Label(self.right_frame, text = 'Type your actions here:')
        self.action_lbl.pack(pady = (10, 0))
        self.action_box = tk.Entry(self.right_frame)
        self.action_box.bind('<Return>', self.on_enter)
        self.action_box.pack(fill = 'x')
    
    def create_stats(self):
        self.lvl = tk.IntVar()
        self.lvl.set(1)
        self.xp = tk.IntVar()
        self.xp.set(0)
        self.gp = tk.IntVar()
        self.gp.set(0)
        self.strth = tk.IntVar()
        self.strth.set(1)
        self.ac = tk.IntVar()
        self.ac.set(0)
        self.mod= tk.IntVar()
        self.mod.set(0)

        self.lvl_label = tk.Label(self.left_frame, text = 'Level').pack(pady = 5)
        self.lvl_txt = tk.Label(self.left_frame, textvariable = self.lvl, width = 4, height = 1, relief = 'sunken', bg = 'white').pack(pady = 0)
        self.xp_label = tk.Label(self.left_frame, text = 'XP').pack(pady = 5)
        self.xp_txt = tk.Label(self.left_frame, textvariable = self.xp, width = 4, height = 1, relief = 'sunken', bg = 'white').pack(pady = 0)
        self.gp_label = tk.Label(self.left_frame, text = 'Gold').pack(pady = 5)
        self.gp_txt = tk.Label(self.left_frame, textvariable = self.gp, width = 4, height = 1, relief = 'sunken', bg = 'white').pack(pady = 0)
        self.str_label = tk.Label(self.left_frame, text = 'STR').pack(pady = 5)
        self.str_txt = tk.Label(self.left_frame, textvariable = self.strth, width = 4, height = 1, relief = 'sunken', bg = 'white').pack(pady = 0)
        self.ac_label = tk.Label(self.left_frame, text = 'AC').pack(pady = 5)
        self.ac_txt = tk.Label(self.left_frame, textvariable = self.ac, width = 4, height = 1, relief = 'sunken', bg = 'white').pack(pady = 0)
        self.mod_label = tk.Label(self.left_frame, text = 'DMG Modifier').pack(pady = 5)
        self.mod_txt = tk.Label(self.left_frame, textvariable = self.mod, width = 4, height = 1, relief = 'sunken', bg = 'white').pack(pady = 0)

    #Stat setters - used to modify stats display
    def set_level(self, new_level):
        self.lvl.set(new_level)
    def set_xp(self, new_xp):
        self.xp.set(new_xp)
    def set_gold(self, new_gold):
        self.gp.set(new_gold)
    def set_strength(self, new_strength):
        self.strth.set(new_strength)
    def set_ac(self, new_ac):
        self.ac.set(new_ac)
    def set_modifier(self, new_modifier):
        self.mod.set(new_modifier)

    # Changes the current HP based on the max HP defined above
    def set_hp(self, current_hp):
        new_hp = str(current_hp) + " / " + str(self.max_hp)
        self.hp.set('HP ' + new_hp)
            

    def create_inventory(self):
        self.hp = tk.StringVar()
        self.equipped_weapon = tk.StringVar()
        self.equipped_armour = tk.StringVar()
        
        self.hp_lbl = tk.Label(self.left_frame, textvariable = self.hp, font = ('Arial', 10), fg = 'red').pack(pady = (10, 0))
        self.weapon_lbl = tk.Label(self.left_frame, text = 'Equipped Weapon: ').pack(pady = (15, 0))
        self.weapon_txt = tk.Label(self.left_frame, textvariable = self.equipped_weapon, width = 20, relief = 'sunken', bg = 'white').pack()
        self.armour_lbl = tk.Label(self.left_frame, text = 'Equipped Armour: ').pack()
        self.armour_txt = tk.Label(self.left_frame, textvariable = self.equipped_armour, width = 20, relief = 'sunken', bg = 'white').pack()
        self.inventory_lbl = tk.Label(self.left_frame, text = 'ITEM').pack(pady = (15, 0))
        self.item = ttk.Combobox(self.left_frame, values = self.item_list, width = 20, state = 'readonly')
        self.item.pack()
        self.use_btn = tk.Button(self.left_frame, text = 'Use Item').pack(pady = (5, 0))

    # Function used to add text to the bottom of the output window
    def append_text(self, string):
        self.text_box.configure(state = 'normal')
        text = "\n\n" + string
        self.text_box.insert('end', text)
        self.text_box.configure(state = 'disabled')

    # Function used to return list of scenarios from scenario.txt file
    def get_scenarios(self):
        file = open('scenarios.txt', 'r')
        data = json.load(file)
        file.close()
        return data

    # Funtion used to return a list of collectables from collectables.txt
    def get_collectables(self):
        file = open('collectables.txt', 'r')
        data = json.load(file)
        file.close()
        return data

    # Funtion used to return a list of enemies from enemies.txt
    def get_enemies(self):
        file = open('enemies.txt', 'r')
        data = json.load(file)
        file.close()
        return data

    # Function used to return index of scenario in list based on scenario name
    def get_scenario_index(self, name):
        data = self.get_scenarios()
        for index, item in enumerate(data):
            if name in item['name']:
                return index

    # Function used to return index of collectable in list based on collectable tag
    def get_collectable_index(self, tag):
        data = self.get_collectables()
        for index, item in enumerate(data):
            if tag.lower() in item['tag']:
                return index

    # Function used to return index of collectable in list based on collectable tag
    def get_enemy_index(self, tag):
        data = self.get_enemies()
        for index, item in enumerate(data):
            if tag.lower() in item['tag']:
                return index

    # Function used to overwrite the current scenario with scenario
    # that is held by variable 'self.current_scenario'
    def set_scenario(self):
        scenario_index = self.get_scenario_index(self.current_scenario)
        data = self.get_scenarios()
        scenario = data[scenario_index]['text']
        self.text_box.configure(state = 'normal')
        self.text_box.delete(1.0, 'end')
        self.text_box.insert(1.0, scenario)
        self.text_box.configure(state = 'disabled')

    def first_word(self, string):
        space_index = string.find(" ")
        first_word = string[:space_index]
        return first_word

    def end_phrase(self, string):
        space_index = string.find(" ")
        end_phrase = string[space_index + 1:]
        return end_phrase

    def add_item(self, item_name):
        self.item_list.append(item_name)
        text = item_name + " added to inventory!"
        self.append_text(text)

    def use_item(self):
         pass

    def equip_weapon(self, weapon_tag):
        data = self.get_collectables()
        item = self.get_collectable_index(weapon_tag)
        if data[item]['type'] == 'weapon':
            self.equipped_weapon.set(data[item]['name'])
            self.set_modifier('+' + data[item]['modifier'])
            equipped = data[item]['name'] + " equipped"
            self.append_text(equipped)
        else:
            text = data[item]['name'] + " cannot be used as a weapon"
            self.append_text(text)

    def equip_armour(self, armour_tag):
        data = self.get_collectables()
        item = self.get_collectable_index(armour_tag)
        self.equipped_armour.set(data[item]['name'])
        self.set_ac(data[item]['armour class'])
        equipped = data[item]['name'] + " equipped"
        self.append_text(equipped)

    def initialise_game(self):
        self.set_hp(10)
        self.set_scenario()

    # Function that triggers scene changes and interactions based on user input    
    def on_enter(self, text):
        text = self.action_box.get()
        self.action_box.delete(0, 'end')
        current_index = self.get_scenario_index(self.current_scenario)
        data = self.get_scenarios()

        # Controls collection of items in the scenario based on [items], [weapons], [armour]
        if self.first_word(text) == 'collect':
            try:
                if self.end_phrase(text) in data[current_index]['weapons']:
                    self.equip_weapon(self.end_phrase(text.lower()))
                elif self.end_phrase(text) in data[current_index]['armour']:
                    self.equip_armour(self.end_phrase(text.lower()))
                elif self.end_phrase(text) in data[current_index]['items']:
                    self.add_item(self.end_phrase(text.lower()))
            except:
                uncollected = self.end_phrase(text) + " cannot be collected"
                self.append_text(uncollected)
        
        # Controls progression of story based on 'entry' and 'exit' words
        elif text in data[current_index]['exit words']:
            for scenario in data:
                if text in scenario['entry words']:
                    scenario_index = self.get_scenario_index(scenario['name'])
                    self.current_scenario = data[scenario_index]['name']
                    self.set_scenario()

#-------------------------------------------------END OF FUNCTIONS-------------------------------------------------#

if __name__ == '__main__':
    master = tk.Tk()
    main_app = MainApplication(master)
    master.mainloop()