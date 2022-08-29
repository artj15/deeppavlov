from my_solution import knight_move


# %%


def main(desk_size: list[int, int]) -> list[list[int, int]]:
    width = desk_size[0]
    height = desk_size[1]
    board = [[0] * width for _ in range(height)]
    result = []
    moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    x = 0
    y = 0
    pos = 1
    knight_move(x, y, pos, board, result, moves, height, width)
    return result
