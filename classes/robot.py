class Robot:

    # METHOD TO INITIALIZE THE ROBOT
    def __init__(self, name, friend, color, height):
        print("BUILDING A ROBOT")
        self.name = name
        self.friend = friend
        self.color = color
        self._height = height
        print("COMPLETED BUILDING ROBOT")

    # METHOD TO REPRESENT THE ROBOT INSTANCE
    def __repr__(self):
        return f"Robot(name={self.name}, friend={self.friend}, color={self.color}, height={self._height})"
    
    # EXAMPLE INSTANCE METHOD
    def walk(self):
        print("Robot is walking")
        print(self)

    # READER / GETTER
    @property
    def height(self):
        return self._height
    
    # WRITER / SETTER
    @height.setter
    def height(self, new_height):
        if isinstance(new_height, int) or isinstance(new_height, float):
            self._height = new_height
        else:
            raise TypeError("Height must be an integer or float")
    
    # EXAMPLE OF READ ONLY WRITER / SETTER
    # @height.setter
    # def height(self, new_height):
    #     raise TypeError("You may not change this property")