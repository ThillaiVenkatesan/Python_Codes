"""class Snake:
     name = "python"
     def change_name(self, new_name):# note that
#the first argument is self
        self.name = new_name
# access the class
#attribute with the self keyword
# instantiate the class
snake = Snake()
# print the current object name
print(snake.name)
#python
# change the name using the change_name method
snake.change_name("anaconda")
print(snake.name)
#anaconda"""
class Snake:
    def __init__(self, name):
        self.name = name
    def change_name(self, new_name):
        self.name = new_name
python = Snake("python")
anaconda = Snake("anaconda")
