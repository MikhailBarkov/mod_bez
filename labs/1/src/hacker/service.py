import uuid
import os
import shutil
from time import sleep


class Service:

    def __init__(self, hacker_dir, share_dir):
        self.hacker_dir = hacker_dir
        self.share_dir = share_dir
        self.file_time = {}

    def update(self):
        new_files = [
            file for file in os.listdir(self.share_dir) if os.path.isfile(os.path.join(self.share_dir, file))
        ]
        new_times = [
            os.path.getmtime(os.path.join(self.share_dir, file)) for file in new_files
        ]

        for file, new_time in zip(new_files, new_times):
            if file in self.file_time:
                if not (self.file_time[file] < new_time):
                    continue

            self.file_time[file] = new_time

            shutil.copyfile(
                os.path.join(self.share_dir, file),
                os.path.join(self.hacker_dir, file + str(uuid.uuid4().hex))
            )

