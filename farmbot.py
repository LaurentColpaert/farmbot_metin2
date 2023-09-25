import numpy as np
import pydirectinput
from time import time
from windowcapture import WindowCapture
import constants

class FarmBot:

    #properties
    botting = False
    wincap = None
    timer_action = time()


    def set_to_begin(self, values):
        print("Setting up values for the farm bot")
        #Retrieve window info
        #SPELLS
        self.spell = values["-SPELL-"]
        if self.spell:
            self.spell1 = values['-SPELL1-']
            self.spell1_time = int(values['-SPELL1_TIME-']) if self.spell1 == True else 0
            self.spell1_key = values['-SPELL1_KEY-']
            self.timer_1 = time()
            self.first_spell_casted1 = False

            self.spell2 = values['-SPELL2-']
            self.spell2_time = int(values['-SPELL2_TIME-'])  if self.spell2 == True else 0
            self.spell2_key = values['-SPELL2_KEY-']
            self.timer_2 = time()
            self.first_spell_casted2 = False

            self.spell3 = values['-SPELL3-']
            self.spell3_time = int(values['-SPELL3_TIME-'])  if self.spell3 == True else 0
            self.spell3_key = values['-SPELL3_KEY-']
            self.timer_3 = time()
            self.first_spell_casted3 = False

            self.spell4 = values['-SPELL4-']
            self.spell4_time = int(values['-SPELL4_TIME-'])  if self.spell4 == True else 0
            self.spell4_key = values['-SPELL4_KEY-']
            self.timer_4 = time()
            self.first_spell_casted4 = False

            self.spells_toplay = []
            if self.spell1:
                self.spells_toplay.append("1")
            if self.spell2:
                self.spells_toplay.append("2")
            if self.spell3:
                self.spells_toplay.append("3")
            if self.spell4:
                self.spells_toplay.append("4")

            self.last_spell = self.spells_toplay[-1]

            print(self.spells_toplay)

        #POTIONS
        self.poth = values['-POTH-']
        self.poth_time = values['-POTH_TIME-']
        self.poth_key = values['-POTH_KEY-']
        self.potm = values['-POTM-']
        self.potm_time = values['-POTM_TIME-']
        self.potm_key = values['-POTM_KEY-']

        #DROP
        self.drop = values['-DROP-']
        self.drop_key = values['-DROP_KEY-']

        self.wincap = WindowCapture(constants.GAME_NAME)
        self.timer_action = time()
        self.timer_pickup = time()
        

        mouse_x = int( self.wincap.offset_x + 200)
        mouse_y = int( self.wincap.offset_y + 200)
        pydirectinput.click(x=mouse_x, y=mouse_y, button='right')

    def runHack(self):
        if self.spell:
            if self.spells_toplay[0] == "1":
                if not self.first_spell_casted1 and time() - self.timer_action > 2:
                    self.first_spell_casted1 = True
                    pydirectinput.keyDown(self.spell1_key)
                    pydirectinput.keyUp(self.spell1_key)
                    self.timer_action = time()
                    self.timer_1 = time()
                    self.spells_toplay.append(self.spells_toplay.pop(0))
                    print("First spell 1")

                elif time() - self.timer_1 > self.spell1_time + 1 and time() - self.timer_action > 2:
                    pydirectinput.keyDown(self.spell1_key)
                    pydirectinput.keyUp(self.spell1_key)
                    self.timer_action = time()
                    self.timer_1 = time()
                    self.spells_toplay.append(self.spells_toplay.pop(0))
                    print(" spell 1")

            elif self.spells_toplay[0] == "2":
                if not self.first_spell_casted2 and time() - self.timer_action > 2:
                    self.first_spell_casted2 = True
                    pydirectinput.keyDown(self.spell2_key)
                    pydirectinput.keyUp(self.spell2_key)
                    self.timer_action = time()
                    self.timer_2 = time()
                    if self.last_spell == "2":
                        self.spells_toplay.append(self.spells_toplay.pop(0))
                        self.reorganize_spell_order()
                    else:
                        self.spells_toplay.append(self.spells_toplay.pop(0))
                    print("First spell 2")

                elif time() - self.timer_2 > self.spell2_time + 1 and time() - self.timer_action > 2:
                    pydirectinput.keyDown(self.spell2_key)
                    pydirectinput.keyUp(self.spell2_key)
                    self.timer_action = time()
                    self.timer_2 = time()
                    self.spells_toplay.append(self.spells_toplay.pop(0))
                    print(" spell 2")

            elif self.spells_toplay[0] == "3":
                if not self.first_spell_casted3 and time() - self.timer_action > 2:
                    self.first_spell_casted3 = True
                    pydirectinput.keyDown(self.spell3_key)
                    pydirectinput.keyUp(self.spell3_key)
                    self.timer_action = time()
                    self.timer_3 = time()
                    if self.last_spell == "3":
                        self.spells_toplay.append(self.spells_toplay.pop(0))
                        self.reorganize_spell_order()
                    else:
                        self.spells_toplay.append(self.spells_toplay.pop(0))
                    print("First spell 3")

                elif time() - self.timer_3 > self.spell3_time + 1 and time() - self.timer_action > 2:
                    pydirectinput.keyDown(self.spell3_key)
                    pydirectinput.keyUp(self.spell3_key)
                    self.timer_action = time()
                    self.timer_3 = time()
                    self.spells_toplay.append(self.spells_toplay.pop(0))
                    print(" spell 3")
            
            elif self.spells_toplay[0] == "4":
                if not self.first_spell_casted4 and time() - self.timer_action > 2:
                    self.first_spell_casted4 = True
                    pydirectinput.keyDown(self.spell4_key)
                    pydirectinput.keyUp(self.spell4_key)
                    self.timer_action = time()
                    self.timer_4 = time()
                    if self.last_spell == "4":
                        self.spells_toplay.append(self.spells_toplay.pop(0))
                        self.reorganize_spell_order()
                    else:
                        self.spells_toplay.append(self.spells_toplay.pop(0))
                    print("First spell 4")

                elif time() - self.timer_4 > self.spell4_time + 1 and time() - self.timer_action > 2:
                    pydirectinput.keyDown(self.spell4_key)
                    pydirectinput.keyUp(self.spell4_key)
                    self.timer_action = time()
                    self.timer_4 = time()
                    self.spells_toplay.append(self.spells_toplay.pop(0))
                    print(" spell 4")

        if self.drop and time() - self.timer_pickup > 1:
            pydirectinput.keyDown(self.drop_key)
            pydirectinput.keyUp(self.drop_key)
       
    def reorganize_spell_order(self):
        w = []
        for i in self.spells_toplay:
            if i == "1":
                w.append(self.spell1_time - (time() - self.timer_1))
            elif i == "2":
                w.append(self.spell2_time - (time() - self.timer_2))
            elif i == "3":
                w.append(self.spell3_time - (time() - self.timer_3))
            elif i == "4":
                w.append(self.spell4_time - (time() - self.timer_4))
        combined = list(zip(self.spells_toplay,w))

        sorted_combined = sorted(combined, key=lambda x: x[1])
        sorted_strings = [item[0] for item in sorted_combined]
        self.spells_toplay = sorted_strings