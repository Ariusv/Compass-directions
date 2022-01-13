def direction(facing, turn):
    degree = 45
    compass_points = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    start_index = compass_points.index(facing)

    turns = turn // degree
    target_index = (start_index + turns) % len(compass_points)

    return compass_points[target_index]
