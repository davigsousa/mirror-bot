class Setence:
    '''
    Setence Class, will transform the statement string into an object with
    each part of it in different atributes.
    '''
    def __init__(self, string: str):
        self.read_string(string)

    def read_string(self, string):
        parts = string.split('|&|')
        self.type: str = parts[0]
        self.pause: float = float(parts[1])
        self.action: str = parts[2]
        self.metadata: str = parts[3]
