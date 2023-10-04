import PySimpleGUI as sg

from table import Table


class Interface:

    def __init__(self):
        self.table = Table()

        self.output_line = ''

        self.font = ("Courier", 2)
        sg.theme('dark grey 9')

        self.window = sg.Window('User Window', self.get_layout(), size=(1400, 900), font=self.font)

    def show(self):
        while True:
            event, values = self.window.read()

            if event == 'BUTTON_ADD_USER':
                try:
                    self.table.add_user(values['INPUT_ADD_USER'].strip())
                except:
                    sg.popup_error(f'Имя пользователя задано неккоректно', font=self.font)
                    continue

            elif event == 'BUTTON_ADD_SYMBOL':
                try:
                    self.table.add_symbol(values['INPUT_ADD_SYMBOL'])
                except:
                    sg.popup_error(f'Символ задан неккоректно', font=self.font)
                    continue

            elif event == 'BUTTON_DELETE_USER':
                try:
                    self.table.delete_user(values['INPUT_DELETE_USER'].strip())
                except:
                    sg.popup_error(f'Пользователь не найден', font=self.font)
                    continue

            elif event == 'BUTTON_DELETE_SYMBOL':
                try:
                    self.table.delete_symbol(values['INPUT_DELETE_SYMBOL'].strip())
                except:
                    sg.popup_error(f'Символ не найден', font=self.font)
                    continue
            elif event == 'BUTTON_CHANGE_ACCESS':
                for username, access_symbols in self.table.users.items():
                    for symbol in self.table.symbols:
                        access = values[f'{username}_{symbol}'].strip()
                        if access == '1':
                            if not symbol in access_symbols:
                                access_symbols.append(symbol)
                        elif access == '0':
                            if symbol in access_symbols:
                                access_symbols.remove(symbol)
                        else:
                            sg.popup_error(f'Право доступа может быть "1" или "0". Право доступа задано неккоректно', font=self.font)
                            continue

            elif event == 'BUTTON_ENTER_LINE':
                username = values['DROP_USER'].strip()
                if not username in self.table.users:
                    sg.popup_error(f'Имя пользователя задано неккоректно', font=self.font)
                    continue

                access_symbols = self.table.users[username]

                result = ''
                for symbol in values['INPUT_CHECK_STR']:
                    if not symbol in self.table.symbols:
                        continue

                    if symbol in access_symbols:
                        result += symbol

                self.output_line = result

            elif event == sg.WIN_CLOSED:
                self.table.write()
                break

            self.update_win()

        self.window.close()

    def update_win(self):
        t_window = sg.Window('User Window', self.get_layout(), size=(1400, 900), font=self.font)
        self.window.close()
        self.window = t_window

    def get_layout(self):
        return [
            [sg.Frame('Access Matrix', self.get_matrix(), key='ACCESS_MATRIX')],
            [sg.Button('Update', key='BUTTON_CHANGE_ACCESS')],
            [sg.Button('Add user', key='BUTTON_ADD_USER'), sg.I(key='INPUT_ADD_USER')],
            [sg.Button('Add symbol', key='BUTTON_ADD_SYMBOL'), sg.I(key='INPUT_ADD_SYMBOL')],
            [sg.Button('Delete User', key='BUTTON_DELETE_USER'), sg.I(key='INPUT_DELETE_USER')],
            [sg.Button('Delete Symbol', key='BUTTON_DELETE_SYMBOL'), sg.I(key='INPUT_DELETE_SYMBOL')],
            [
                sg.Drop(values=tuple(self.table.users.keys()), size=(10, 1), font=self.font, key='DROP_USER'),
                sg.I(key='INPUT_CHECK_STR', size=(50, 1)),
            ],
            [
                sg.Button('Convert', key='BUTTON_ENTER_LINE'),
                sg.T(self.output_line, key='OUTPUT_CHECK_STR', size=(50, 1))
            ],
        ]

    def get_matrix(self):
        usernames = [sg.T(username, font=self.font, size=(7,1)) for username in self.table.users.keys()]
        symbols = [sg.T('', font=self.font, size=(7,1))] + [sg.T(symbol, font=self.font, size=(1,1)) for symbol in self.table.symbols]
        matrix = [
            [sg.I(elem, key=f'{username}_{symbol}', font=self.font, size=(1,1)) for elem, symbol in zip(row, self.table.symbols)]
            for row, username in zip(self.table.get_access_map(), self.table.users.keys())
        ]

        return [symbols] + [
            [username] + row for username, row in zip(usernames, matrix)
        ]
