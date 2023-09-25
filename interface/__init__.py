import PySimpleGUI as sg

class PyWindow:

    window = None

    def __init__(self):
        sg.theme('Dark Red')
        self.create_window()

    def farm_tab(self):
        return [[sg.Text('Settings for the farming')],
                [sg.Frame('Spells', [
                    [sg.Checkbox('Do you want to activate the spells ?', key='-SPELL-',default=True)],
                    [sg.Frame('',[
                    [sg.Checkbox('Spell 1 (cooldown | key )', key='-SPELL1-'), sg.InputText(size=(5,10), key='-SPELL1_TIME-',default_text="100"), sg.InputText(size=(5,10), key='-SPELL1_KEY-', default_text="0")],
                    [sg.Checkbox('Spell 2 (cooldown | key )', key='-SPELL2-'), sg.InputText(size=(5,10), key='-SPELL2_TIME-',default_text="72"), sg.InputText(size=(5,10), key='-SPELL2_KEY-', default_text="9")],
                    [sg.Checkbox('Spell 3 (cooldown | key )', key='-SPELL3-'), sg.InputText(size=(5,10), key='-SPELL3_TIME-',default_text="100"), sg.InputText(size=(5,10), key='-SPELL3_KEY-', default_text="8")],
                    [sg.Checkbox('Spell 4 (cooldown | key )', key='-SPELL4-'), sg.InputText(size=(5,10), key='-SPELL4_TIME-'), sg.InputText(size=(5,10), key='-SPELL4_KEY-')],
                    ])]])],
                [sg.Frame('Potions (not working yet)', [
                    [sg.Checkbox('Health potion (cooldown | key )', key='-POTH-'), sg.InputText(size=(5,10), key='-POTH_TIME-'), sg.InputText(size=(5,10), key='-POTH_KEY-')],
                    [sg.Checkbox('Mana potion (cooldown | key )', key='-POTM-'), sg.InputText(size=(5,10), key='-POTM_TIME-'), sg.InputText(size=(5,10), key='-POTM_KEY-')],
                    ])],
                [sg.Frame('Item', [
                    [sg.Checkbox('Auto collect items (key)', key='-DROP-'), sg.InputText(size=(5,10), key='-DROP_KEY-', default_text="y")],
                    ])],
                [sg.Button('START', key='-FARMSTART-')]]
   

    def create_tabs(self):


        tab4_layout = self.farm_tab()

    
        tab_4 = sg.Tab('FARM', tab4_layout, font='Courier 15', key='-TAB4-')

        tab_group_layout = [[tab_4]]

        return tab_group_layout

    def create_window_layout(self):

        tab_group_layout = self.create_tabs()

        return [[sg.TabGroup(tab_group_layout,
                 enable_events=True,
                 key='-TABGROUP-')]]

    def create_window(self):

        layout = self.create_window_layout()

        self.window = sg.Window('Metin2 - FARMBOT', layout, no_titlebar=False)
