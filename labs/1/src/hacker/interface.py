import PySimpleGUI as sg

import os
from time import sleep

from service import Service


class Interface:

    def __init__(self, hacker_dir, share_dir):
        self.hacker_dir = hacker_dir
        self.share_dir = share_dir

        self.service = Service(self.hacker_dir, self.share_dir)

        self.font = ("Courier", 20)

        sg.theme('dark grey 9')

        layout = [
            [sg.Text('Файлы в директории хакера', auto_size_text=True, font=self.font)],
            [sg.Output(size=(20,10), key='HACKER_DIR', font=self.font)],
        ]

        self.window = sg.Window(
            'Hacker Window', layout, size=(500, 500),
        )

    def show(self):
        while True:
            event, values = self.window.read(timeout=500, close=False)

            self.service.update()
            self.window['HACKER_DIR'].update(', '.join(os.listdir(self.hacker_dir)))

            if event == sg.WIN_CLOSED:
                break
