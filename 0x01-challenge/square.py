#!/usr/bin/python3

class Square():
    
    
    def __init__(self, side_length):
        self.width = side_length

    def area(self):
        """ Area of the square """
        return self.width ** 2

    def perimeter(self):
        """ Calculate the perimeter of the square """
        return self.width * 4

    def __str__(self):
        return f"Square with side length {self.width}"

if __name__ == "__main__":

    s = Square(side_length=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
