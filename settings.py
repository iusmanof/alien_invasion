class Settings():

    def __init__(self):
        # Blue sky
        self.bg_color = (115,215,255)
        self.screen_width = 1200
        self.screen_height = 800
        
        self.ship_speed = 10
        self.ship_limit = 3

        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = (156, 138, 86)
        self.bullet_allowed = 6

        self.alien_speed = 5.0
        self.fleet_drop_speed = 10
        self.fleet_direction = -1

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        self.alien_points = 50
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        # fleet_direction = 1 - right, -1 - left
        self.fleet_direction = 1

    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)