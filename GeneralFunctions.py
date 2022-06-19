def returnpositive(value):

    if type(value) != int:
        if type(value) != float:
            raise Exception("Value is not a number")

    if value < 0:
        return value * -1
    if value > 0:
        return value
    if value == 0:
        return value

# generates the array for the positions of the entity's
def generaterandomarray():
    poslist = []
    x = 0
    y = 0
    for i in range(9):
        for j in range(9):
            coordinate = {
                "x": x,
                "y": y
            }
            poslist.append(coordinate)
            x += 80
        y += 80
        x = 0
    return poslist

def getgridposition(position):
    x = int(position["x"]/80)
    y = int(position["y"]/80)
    print("position x: " + str(position["x"]) + " returns " + str(x))
    print("position y: " + str(position["y"]) + " returns " + str(y))

    xypos = {
        "x": x,
        "y": y
    }
    return xypos

