class Settings():

    def __init__(self):
        # Blue sky
        self.bg_color = (115,215,255)
        self.screen_width = 1200
        self.screen_height = 800
        
        self.ship_speed = 2

        self.bullet_speed = 5
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (156, 138, 86)
        self.bullet_allowed = 3

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = -1