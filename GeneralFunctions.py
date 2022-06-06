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