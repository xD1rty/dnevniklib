class DnevnikTokenError(Exception):
    def __init__(self, *args):
        if args[0] != None:
            self.msg = args[0]
        else:
            self.msg = None
    def __str__(self):
        if self.msg != None:
            return f"Token {self.msg} is broken, change it!"
        else:
            return "Token is broken, change it!"