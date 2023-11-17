"""
A script to practice stuff
"""


class DataOperation:
    uri: str = 'ssh://password@username'
    perceptron_props: dict = {'encodes': [0x0110, 0x1010], 'type': 'linear'}

    def __init__(self, data: list):
        self.data = data

    def status(self):
        print(f'{self.uri} successfully connected')


op = DataOperation([1, 2, 3])
op.status()

# end of file
