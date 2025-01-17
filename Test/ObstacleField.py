from Point import Point

class ObstacleField:
    def __init__(self, heightInches, widthInches, entranceWidth, entranceOffset, exitWidth, exitOffset, occupiedPoints):
        self.heightInches_ = heightInches
        self.widthInches_ = widthInches
        self.entranceWidth_ = entranceWidth
        self.entranceOffset = entranceOffset
        self.exitWidth_ = exitWidth
        self.exitOffset_ = exitOffset

        # if the occupied points list is empty 
        assert type(occupiedPoints) is list, "occupiedPoints argument is not a list. Send an empty list if necessary."
        if len(occupiedPoints) != 0:
            self.isPopulated = True
            self.occupiedPoints_ = occupiedPoints
        else:
            self.isPopulated = False
            self.occupiedPoints_ = []

    def checkPointOccupied(self):
        # return true if the point is not occupied
        

    def toString(self):
        # Print out each coordinate in nested for loops
        rowString = ''
        # For the y axis
        for y in range(self.heightInches_ + 2): # Note, the + 2 here is for the boundaries
            
            # For the x axis
            for x in range(self.widthInches_ + 2): # Note, the + 2 here is for the boundaries

                if y == 0 or y == self.heightInches_ + 1: # If at the top or bottom row
                    rowString += 'x'
                else:
                    # Check to see if we are at the start or the end of the row
                    edgeColumnFlag = 0
                    if x == 0 or x == self.widthInches_ + 1:
                        edgeColumnFlag = 1

                        # Now we need to check to see if we are at the entrance or exit, and leave those clear
                        # Choose to look for either the entrance or exit
                        #if(y == 0):
                            # exit
                        #    if y == (exitOffset + 1): # The plus 1 is because this is an offset from the top wall

                        #else:
                            # entrance


                        # if not entrance or exit
                        rowString += 'x'

                    # Check each point in occupiedPoints
                    pointIsOccupiedFlag = 0
                    for point in self.occupiedPoints_:
                        if point.xVal_ == x and point.yVal_ == y:
                            # the point is occupied
                            rowString += 'x'
                            pointIsOccupiedFlag = 1

                    if not pointIsOccupiedFlag and not edgeColumnFlag: # if point is not occupied
                        rowString += ' '
            
            print(rowString)
            rowString = ''



if __name__ == "__main__":
    testField = ObstacleField(72, 96, 1, 0, 1, 0, [Point(3,3), Point(3,4)])
    testField.toString()
