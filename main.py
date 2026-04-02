from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line, InstructionGroup
from kivy.clock import Clock
import math

class GhostGalaxyWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.points_count = 40 # Fewer points for mobile RAM
        self.rings = 6
        self.target = [500, 500]
        self.phase = 0
        self.canvas_group = InstructionGroup()
        self.canvas.add(self.canvas_group)
        
        # Start the 60FPS loop
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def on_touch_move(self, touch):
        # On mobile, the "Hand" is your finger touch
        self.target = [touch.x, touch.y]

    def update(self, dt):
        self.canvas_group.clear()
        self.phase += 0.05
        
        for r in range(self.rings):
            points = []
            base_r = 40 + (r * 30)
            
            # Executive Cyan Color
            self.canvas_group.add(Color(0, 0.8, 1, 0.8))
            
            for i in range(self.points_count + 1):
                angle = (i / self.points_count) * (math.pi * 2)
                wave = math.sin(angle * 4 + self.phase + r) * 15
                
                x = self.target[0] + math.cos(angle) * (base_r + wave)
                y = self.target[1] + math.sin(angle) * (base_r + wave)
                points.extend([x, y])

            self.canvas_group.add(Line(points=points, width=1.1, close=True))

class GhostApp(App):
    def build(self):
        return GhostGalaxyWidget()

if __name__ == "__main__":
    GhostApp().run()