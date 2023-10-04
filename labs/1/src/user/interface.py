import PySimpleGUI as sg

import os

from service import Service


class Interface:

    def __init__(self, user_dir, share_dir):
        self.user_dir = user_dir
        self.share_dir = share_dir

        self.service = Service(self.user_dir, self.share_dir)

        self.font = ("Courier", 20)

        sg.theme('dark grey 9')

        self.layout = [
            [
                sg.Text(
                    'Файлы в директории пользователя и в общей директории',
                    auto_size_text=True,
                    font=self.font
                )
            ],
            [
                sg.Multiline(size=(20,10), key='USER_DIR_FILES', font=self.font),
                sg.Multiline(size=(20,10), key='SHARE_DIR_FILES', font=self.font),
            ],
            [sg.Button('Добавить файл', key='BUTTON_ADD_FILE', font=self.font)],
            [
                sg.Text('Имя файла', auto_size_text=True, font=self.font),
                sg.In(key='IN_FILE_NAME', size=(15,1), font=self.font)
            ],
            [
                sg.Text('Содержание', auto_size_text=True, font=self.font),
                sg.In(key='IN_FILE_STR', size=(15,1), font=self.font)
            ],
            [
                sg.Button('Копировать файл', key='BUTTON_COPY_FILE', font=self.font),
                sg.In(key='COPY_FILE_NAME', size=(15,1), font=self.font)
            ],
        ]

        self.window = sg.Window('User Window', self.layout, size=(1000, 800), font=self.font)

    def show(self):
        while True:
            event, values = self.window.read()

            if event == 'BUTTON_ADD_FILE':
                try:
                    self.service.create_file(values['IN_FILE_NAME'], values['IN_FILE_STR'])
                except BaseException:
                    sg.popup_error(f'Имя файла задано неккоректно', font=self.font)

                self.update_folders()

            elif event == 'BUTTON_COPY_FILE':
                try:
                    self.service.share(values['COPY_FILE_NAME'])
                except BaseException as e:
                    sg.popup_error(f'Имя файла задано неккоректно', e, font=self.font)

                self.update_folders()

            elif event == sg.WIN_CLOSED:
                break

    def update_folders(self):
        self.window['USER_DIR_FILES'].update(', '.join(os.listdir(self.user_dir)))
        self.window['SHARE_DIR_FILES'].update(', '.join(os.listdir(self.share_dir)))
