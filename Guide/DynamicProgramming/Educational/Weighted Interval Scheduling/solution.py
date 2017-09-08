class Request(object):
    """
    Simple object to represent a request with a:
        start time s
        weight or value v
        finish time f
    """
    def __init__(self, start, value, finish):
        self.start = start
        self.value = value
        self.finish = finish


