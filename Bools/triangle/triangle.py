def equilateral(sides):
    if sum(sides) != 0:
        if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
            return sides[0] == sides[1] and sides[0] == sides[2] and sides[1] == sides[2]
    return False


def isosceles(sides):
    if sum(sides) != 0:
        if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
            return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]
    return False


def scalene(sides):
    if sum(sides) != 0:
        if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
            return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
    return False