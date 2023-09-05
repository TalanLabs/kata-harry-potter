class Book:
    def __init__(self, price: int, volume: int):
        self.price = price
        self.volume = volume

    def __repr__(self):
        return "%s, %s" % (self.price, self.volume)

