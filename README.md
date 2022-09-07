# Adventure Game
A text-based adventure game with RPG elements

A text-based adventure game in the spirit of old text-based games like Zork, except with added RPG features such as Hit Points (HP), Armour Class (AC), weapons and items, experience (XP), and gold

Still in early concept and development

The goal is to produce a classical text-based adventure game that takes input such as "follow" or "go north" to advance in the game, but with an added combat element that includes the use of the aforementioned RPG elements

Scenario transistions work using "exit words" and "entry words". Each scenario has a list of "exit words" and "entry words". When exit word is typed, GUI displays the next scenario that has the matching phrase in its "entry words" list.

A separate CLI script is used to add and remove scenarios. A GUI version is desired, but not critical at this stage
