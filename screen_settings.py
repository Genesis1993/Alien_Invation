class Settings():
    """class to store all the settings of the game"""
    def __init__(self):
        """initialize the game settings"""
        #screen settings
        self.screen_with = 1200
        self.screen_height = 600
        self.backgroundcolor = (0 , 0 , 0)

        #speed of the ship
        self.ship_speed_factor = 1.5

        #Bullet settings
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,200,0)

