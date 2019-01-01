class Settings():
    """a class to store all settings for Alien Invasion"""

    def __init__(self) -> None:
        """Initialize the game settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 0,0,0
        self.ship_speed_factor = 10
        self.bullet_width = 30
        self.bullet_height = 3
        self.bullet_color = 255,0,0
        self.bullet_speed_factor = 10
        self.star_width = 2
        self.star_height = 2
        self.star_color = 255,255,255
        self.star_density = 400
        self.asteroid_speed_factor = 5
        self.asteroid_density = 1