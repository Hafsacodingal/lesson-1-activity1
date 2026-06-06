class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def introduce(self):
        print("Hello! I am", self.name)
        print("My color is", self.color)
        print("I can help you!")

my_robot = Robot("Robo1", "Blue")
my_robot.introduce()