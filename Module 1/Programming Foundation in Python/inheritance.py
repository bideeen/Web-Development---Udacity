class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print('Last name - {0}'.format(self.last_name))
        print('eye_color - {0}'.format(self.eye_color))

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print('Last name - {0}'.format(self.last_name))
        print('eye_color - {0}'.format(self.eye_color))
        print('number of toys - {0}'.format(str(self.number_of_toys)))


ope = Parent("Bello","blue")
# ope.show_info()
# print(ope.last_name)
ola = Child('olamide', 'yellow', 16)
ola.show_info()
# print(ola.number_of_toys)