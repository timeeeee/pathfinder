import pygame

def collideString(start1, end1, start2, end2):
    string = str(start1) + "->" + str(end1) + " intersects "
    string += str(start2) + "->" + str(end2)
    return string

def collideHorizontal(start1, end1, start2, end2):
    start1x, start1y = start1
    end1x, end1y = end1
    start2x, y = start2
    end2x, xy = end2

#    print "does {}->{} intersect with {}->{}?".format((start1x, start1y), (end1x, end1y), (start2x, y), (end2x, y))

    # If s is also horizontal, and the lines have different y values, we
    # know they don't intersect. If the lines have the same y values,
    # the problem is if they overlap in one dimension.
    if start1y == end1y:
#        print "  s is horizontal"
        if start1y == y:
#            print "    s y and obstacle y are the same"
            # overlap if both startx and starty are outside the line, on the same side
            if (start1x <= start2x and end1x <= start2x) or (start1x >= end2x and end1x >= end2x):
#                print collideString(start1, end1, start2, end2)
                return True
#            else: print "    ... but they don't overlap"
        return False
    else:
#        print "  s is not horizontal"        
        # Parametric equation for this line is s(t) =
        # <(endx - startx) * t + startx, (endy - starty) * t + starty>
    
        # For a horizontal line (x1, y) -> (x2, y)
        # where s intersects the line, (endx - startx) * t + startx = starty
        # so t = (y - starty) / (endy - starty)
    
        t = (y - start1y) / float(end1y - start1y)
        intersectionx = (end1x - start1x) * t + start1x

#        print "  t = {}".format(t)
#        print "  obstacle line x {}".format((start2x, end2x))
#        print "  intersectionx = {}".format(intersectionx)
#        print "  0 <= t <= 1 and intersection x on obstacle line?"
        
        # Lines intersect if t is on (0, 1), and the x part of s(t) is
        # between inflated.left, inflated.right
        if 0 <= t and t <= 1 and start2x <= intersectionx and intersectionx <= end2x:
#            print "  0 <= {} <= 1 and {} <= {} <= {}: intersect!".format(t, start2x, intersectionx, end2x)
            return True
    return False

def collideVertical(start1, end1, start2, end2):
    # Flip everything across y=x and call collideHorizontal :-D
    start1 = tuple(reversed(start1))
    end1 = tuple(reversed(end1))
    start2 = tuple(reversed(start2))
    end2 = tuple(reversed(end2))
    return collideHorizontal(start1, end1, start2, end2)
#    return collideHorizontal(*map(tuple, map(reversed, [start1, end1, start2, end2])))
    

class Obstacle(pygame.Rect):
    # Obstacle is subclass of Rect- keeps track of own location,
    # is able to draw itself, and return the vertices that will
    # need to be included in a graph

    # Space to keep clear of paths around the obstacle
    openBuffer = 3

    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), self)

    def getVertices(self):
        inflated = self.inflate(Obstacle.openBuffer + 1, Obstacle.openBuffer + 1)
        return [inflated.topleft,
                inflated.topright,
                inflated.bottomleft,
                inflated.bottomright]

    def collideLine(self, start, end):
        # Checks to see if a line from start tuple to finish tuple
        # collides with this rect. Assume that the line to test isn't
        # entirely in the obstacle, so just check if it intersects
        # any boundaries.

        inflated = self.inflate(Obstacle.openBuffer, Obstacle.openBuffer)

        if collideHorizontal(start, end, inflated.topleft, inflated.topright): return True
        if collideHorizontal(start, end, inflated.bottomleft, inflated.bottomright): return True
        if collideVertical(start, end, inflated.topleft, inflated.bottomleft): return True
        if collideVertical(start, end, inflated.topright, inflated.bottomright): return True
#        print "{}->{} doesn't collide with {}".format(start, end, self)
        return False

def test():
    o = Obstacle(100, 100, 50, 50)
    print o.collideLine((50, 140), (150, 40))

if __name__=="__main__": test()
