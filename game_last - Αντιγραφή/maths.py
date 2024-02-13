# maths for the game logic

def linear_interp(x, a, b, A, B):
    if a == b:
        return A  # Avoid division by zero

    # Calculate the linearly interpolated value
    return A + (x - a) * (B - A) / (b - a)

def map_state_from_points(map, pos):
    return map.collisions[int(pos[1])][int(pos[0])]