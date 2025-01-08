from os import system
from pynput.keyboard import Key, Listener

maze = [
  ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
  ["⬜️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️"],
  ["⬜️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️"],
  ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],
  ["🐭", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️"],
  ["⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "🚪"]
]

mickey_pos = [4, 0]
exit_door = [5, 5]

def draw_maze(maze: list):
    system("cls")
    for row in maze:
        print("".join(row))

def on_press(key: Key):
    global mickey_pos
    try:
        mickey_prev = mickey_pos.copy()
        mickey_pos = movements(key, mickey_pos)

        if not mickey_pos:
            return False

        maze[mickey_prev[0]][mickey_prev[1]] = "⬜️"
        maze[mickey_pos[0]][mickey_pos[1]] = "🐭"
        draw_maze(maze)

        if mickey_pos == exit_door:
            print("You Won!!")
            return False

    except AttributeError:
        print(f"special key pressed: {key}")

def on_release(key: Key):
    if key == Key.esc:
        return False

def move_up(current_pos: list) -> list:
    y_pos, x_pos = current_pos
    if y_pos > 0 and maze[y_pos - 1][x_pos] in ("⬜️", "🚪"):
        return [y_pos - 1, x_pos]
    return current_pos

def move_down(current_pos: list) -> list:
    y_pos, x_pos = current_pos
    if y_pos < len(maze) - 1 and maze[y_pos + 1][x_pos] in ("⬜️", "🚪"):
        return [y_pos + 1, x_pos]
    return current_pos

def move_left(current_pos: list) -> list:
    y_pos, x_pos = current_pos
    if x_pos > 0 and maze[y_pos][x_pos - 1] in ("⬜️", "🚪"):
        return [y_pos, x_pos - 1]
    return current_pos

def move_right(current_pos: list) -> list:
    y_pos, x_pos = current_pos
    if x_pos < len(maze[0]) - 1 and maze[y_pos][x_pos + 1] in ("⬜️", "🚪"):
        return [y_pos, x_pos + 1]
    return current_pos

def movements(pressed_key: Key, position: list) -> list:
    match pressed_key:
        case Key.up:
            return move_up(position)
        case Key.down:
            return move_down(position)
        case Key.left:
            return move_left(position)
        case Key.right:
            return move_right(position)
        case Key.esc:
            position.clear()
    return position

with Listener(on_press=on_press, on_release=on_release) as listener:
    draw_maze(maze)
    listener.join()
