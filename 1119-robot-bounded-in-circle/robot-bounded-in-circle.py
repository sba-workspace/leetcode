import math
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions=instructions*4
        x=0
        y=0
        direction=90
        for i in instructions:
            if i=="L":
                direction+=90
            elif i=="R":
                direction-=90
            else:
                rads=math.radians(direction)
                x+=math.cos(rads)
                y+=math.sin(rads)
        x=int(x)
        y=int(y)
        if x==0 and y==0:
            return True
        else:
            return False

        