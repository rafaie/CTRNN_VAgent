from CTRNN import CTRNN
from visual_object import Ray, Line, Circle
import math


class VisualAgent:

    # diameter of agent
    BODY_SIZE = 30.0
    ENV_WIDTH = 400.0
    MAX_RAY_LENGTH = 220.0
    INPUT_GAIN = 10.0
    VISUAL_ANGLE = math.Pi/6
    VEL_GAIN = 5

    def __init__(self, ix=0.0, iy=0.0, NumRays_=7):
        self.cx = 0
        self.cy = 0
        self.vx = 0

        # TVector<Ray> Rays;
        self.nervous_system = CTRNN()
        self.NumRays = NumRays_
        self.Rays.SetBounds(1, self.NumRays)
        self.reset(ix, iy)

    # Accessors
    def positionX(self):
        return self.cx

    def set_positionX(self, new_x):
        pass

    def positionY(self):
        return self.cy

    def reset(self, ix, iy, rs=None, randomize=0):
        pass

    def Step(self, StepSize, object):
        pass

    def reset_rays():
        pass
