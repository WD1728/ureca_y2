import numpy as np

class CircleObstacle:
    def __init__(self, center, radius):
        self.center = np.array(center)
        self.radius = radius

    def distance(self, q):
        return np.linalg.norm(q - self.center)

    def cost(self, q):
        d = self.distance(q)
        return max(0, self.radius - d)**2