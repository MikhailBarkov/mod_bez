from json import load, dump


class Table:

    def __init__(self):
        self.users, self.symbols = self.read()

    def read(self):
        with open('data/access.json', 'r') as rf:
            data = load(rf)
        return data['users'], data['symbols']

    def write(self):
        with open('data/access.json', 'w') as wf:
            dump({'users': self.users, 'symbols': self.symbols}, wf)

    def get_access_map(self):
        return [
            [str(int(symbol in symbols)) for symbol in self.symbols]
            for username, symbols in self.users.items()
        ]

    def add_user(self, username):
        if not username or len(username) < 1 or username in self.users:
            raise ValueError('Bad username')

        self.users[username] = []

    def add_symbol(self, symbol):
        if len(symbol) != 1 or symbol in self.symbols:
            raise ValueError('Bad symbol')

        self.symbols.append(symbol)

    def delete_user(self, username):
        if not username in self.users:
            raise ValueError('User not found')

        self.users.pop(username)

    def delete_symbol(self, symbol):
        if not symbol in self.symbols:
            raise ValueError('Symbol not found')

        self.symbols.remove(symbol)
