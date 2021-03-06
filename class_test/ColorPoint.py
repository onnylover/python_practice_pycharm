from class_test.Point import Point


class ColorPoint(Point):
    def __init__(self, color, x, y):
        super().__init__(x,y)
        self.color = color

    def draw(self):
        print(f"x={self.x} y={self.y} 에 {self.color}점을 그렸습니다.")

    #str 명시하면, 인쇄할때 str내에 있는 return 값을 인쇄하며, debugging 시에 주로 활용함
    def __str__(self):
        return f"ColorPoint({self.color},{self.x},{self.y})"