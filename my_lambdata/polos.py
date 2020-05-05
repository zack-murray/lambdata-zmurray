# my_lambdata/polos.py

# Polo Class!
# attributes / properties (Nouns): size, style, color, texture, price
# method (Verbs): wash, fold, pop collar

class Polo():
    def __init__(self, size, color):
        self.size = size 
        self.color = color
    
    @property
    def full_name(self):
        return f"{self.size} {self.color}"

    def wash(self):
        print(f"Washing the {self.size} {self.color} polo!")

    @staticmethod
    def fold():
        print("Folding the polo!")

if __name__ == "__main__":
    # TODO: initialize a small blu epolo and a large yellow polo

    #df = Dataframe(_________)
    #df.columns
    #df.head()

    p1 = Polo(size="Small", color="Blue")
    print(p1.size, p1.color)
    print(p1.full_name)
    p1.wash()

    p2 = Polo(size="Large", color="Yellow")
    print(p2.size, p2.color)
    print(p2.full_name)
    p2.fold()