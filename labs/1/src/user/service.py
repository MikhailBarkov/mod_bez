import shutil


class Service:

    def __init__(self, user_dir, share_dir):
        self.user_dir = user_dir
        self.share_dir = share_dir

    def create_file(self, filename, line):
        with open(self.user_dir + filename, 'w') as wf:
            wf.write(line)

    def share(self, filename):
        shutil.copyfile(self.user_dir + filename, self.share_dir + filename)
