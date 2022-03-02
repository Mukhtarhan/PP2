import math

if __name__=="__main__":

    num_sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side: "))

    def polygon_area(n_sides, length):
        area = (n_sides * (length ** 2)) / (4 * math.tan((math.pi) / n_sides))
        print(area)

    polygon_area(num_sides, side_length)
