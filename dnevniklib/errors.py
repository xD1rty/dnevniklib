class DnevnikLibError(Exception):
    def __init__(self, *args: object) -> None:
        if args:
            self.msg = args[0]
        else:
            self.msg = None
    def __str__(self) -> str:
        if self.msg:
            return "{}".format(self.msg)
        else:
            return "Error"