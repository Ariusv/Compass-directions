def direction(facing, turn):
    degree = 45
    compass_points = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    try:
        start_index = compass_points.index(facing)
    except ValueError:
        return 'Not correct direction'

    try:
        turns = turn // degree
    except TypeError:
        return 'Not correct turn'

    target_index = (start_index + turns) % len(compass_points)

    return compass_points[target_index]
