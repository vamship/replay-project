from magik import Sprite

class Winner(Sprite):
    def __init__(self, x = 0, y=0):
        super().__init__(x,y)
        
    def update(self, input_data):
        pass
        
            


    def draw(self, display_data):
        display_data.set_pixel(self.x, self.y, (255, 255, 255))
        display_data.set_pixel(self.x, self.y+1, (255, 255, 255))
        display_data.set_pixel(self.x, self.y+2, (255, 255, 255))
        display_data.set_pixel(self.x-1, self.y+3, (255, 255, 255))
        display_data.set_pixel(self.x+1, self.y+3, (255, 255, 255,))
        display_data.set_pixel(self.x+2, self.y+3, (255,255,255))
        display_data.set_pixel(self.x+2, self.y+2, (255,255,255))
        display_data.set_pixel(self.x+2, self.y+1, (255,255,255))
        display_data.set_pixel(self.x+2, self.y, (255,255,255))
        display_data.set_pixel(self.x+3, self.y, (255,255,255))
        display_data.set_pixel(self.x+4, self.y, (255,255,255))
        display_data.set_pixel(self.x+4, self.y+1, (255,255,255))
        display_data.set_pixel(self.x+4, self.y+2, (255,255,255))
        display_data.set_pixel(self.x+4, self.y+3, (255,255,255))
        display_data.set_pixel(self.x+3, self.y+3, (25,255,255))
        # display_data.set_pixel(self.x+2, self.y+3, (255,255,255))
        # display_data.set_pixel(self.x+5, self.y+3, (255,255,255))
        # display_data.set_pixel(self.x+5, self.y+2, (255,255.255))
        # display_data.set_pixel(self.x+4, self.y+3, (255, 255, 255))
        
        

