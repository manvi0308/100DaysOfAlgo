''' Problem statement : Given a set of rectangular 3D boxes, create a stack of boxes which is as tall as possible.A box can be placed on top of another box 
if the dimensions of the 2D base of lower box are each stricly larger than those of 2D base of higher box. Multiple instances of same box can be used such 
that a box can be rotated to use any side as its base

Time complexity : O(n^2)
Space complexity : O(n)'''




# Data structure to store a box (L x W x H)
class Box:
    def __init__(self, length, width, height):
 
        # constraint: width is never more than length
        self.length = length
        self.width = width
        self.height = height
 
 
# Function to generate rotations of all the boxes
def createAllRotations(boxes):
 
    # stores all rotations of each box
    rotations = []
 
    # do for each box
    for box in boxes:
 
        # push the original box: L x W x H
        rotations.append(box)
 
        # push the first rotation: max(L, H) x min(L, H) x W
        rotations.append(Box(max(box.length, box.height),
                     min(box.length, box.height), box.width))
 
        # push the second rotation: max(W, H) x min(W, H) x L
        rotations.append(Box(max(box.width, box.height),
                    min(box.width, box.height), box.length))
 
    return rotations
 
 
# Create a stack of boxes which is as tall as possible
def maxHeight(boxes):
 
    # generate rotations of each box
    rotations = createAllRotations(boxes)
 
    # sort the boxes in descending order of area(L x W)
    rotations.sort(key=lambda x: x.length * x.width, reverse=True)
 
    # max_height[i] stores the maximum possible height when i'th box is on the top
    max_height = [0] * len(rotations)
 
    # fill max_height in bottom-up manner
    for i in range(len(rotations)):
        for j in range(i):
            # dimensions of the lower box are each strictly larger than those
            # of the higher box
            if (rotations[i].length < rotations[j].length and
                    rotations[i].width < rotations[j].width):
                max_height[i] = max(max_height[i], max_height[j])
 
        max_height[i] += rotations[i].height
 
    # return the maximum value in max_height
    return max(max_height)
 
 

