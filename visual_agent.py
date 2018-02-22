from CTRNN import CTRNN
from visual_object import Ray
import math


class VisualAgent:

    # diameter of agent
    BODY_SIZE = 30.0
    ENV_WIDTH = 400.0
    MAX_RAY_LENGTH = 220.0
    INPUT_GAIN = 10.0
    VISUAL_ANGLE = math.Pi/6
    VEL_GAIN = 5

    def __init__(self, ix=0.0, iy=0.0, num_rays_=7):
        self.cx = 0
        self.cy = 0
        self.vx = 0

        self.num_rays = num_rays_
        self.rays = [Ray() for i in range(self.num_rays)]
        self.nervous_system = CTRNN()
        self.Rays.SetBounds(1, self.NumRays)
        self.reset(ix, iy)

    # Accessors
    def positionX(self):
        return self.cx

    def set_positionX(self, new_x):
        self.cx = new_x
        self.reset_rays()

    def positionY(self):
        return self.cy

    def reset(self, ix, iy, rs=None, randomize=0):
        self.cx = ix
        self.cy = iy
        self.vx = 0.0
        if randomize:
            self.nervous_system.randomize_circuit_state(-0.1, 0.1, rs)
        else:
            self.nervous_system.randomize_circuit_state(0.0, 0.0, rs)
        self.reset_rays()

    def Step(self, StepSize, object):
        pass

    def reset_ray(ray, theta, cx, cy):
        if abs(theta) < 0.0000001:
            # special case, vertical ray
            ray.m = math.inf
        else:
            ray.m = 1 / math.tan(theta)

        ray.b = cy - ray.m * cx
        ray.length = VisualAgent.MAX_RAY_LENGTH

        # Set starting coordinates (i.e. on upper perimeter of agent body)
        if ray.m == math.inf:
            ray.startX = cx
            ray.startY = cy + VisualAgent.BodySize / 2
            return

        ray.startX = cx + (VisualAgent.BodySize / 2) * math.sin(theta)
        ray.startY = cy + (VisualAgent.BodySize / 2) * math.cos(theta)

    def reset_rays():
        pass
