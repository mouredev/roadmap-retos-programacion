module Maze = struct
  type t =
    { mutable mouse_pos : int * int
    ; exit_pos : int * int
    ; walls : int array array
    ; width : int
    ; height : int
    }

  let create mouse_pos exit_pos str =
    let walls =
      Core.String.split_lines str
      |> List.map (fun line ->
        Core.String.to_array line
        |> Array.map (function
          | ' ' -> 0
          | _ -> 1))
      |> Array.of_list
    in
    let rows, cols = Array.length walls, Array.length walls.(0) in
    { mouse_pos; exit_pos; walls; width = cols; height = rows }
  ;;
end

module App = struct
  open Curses

  type dir =
    | Up
    | Right
    | Down
    | Left

  let ui_str = Stdio.In_channel.read_all "./resources/mickey-ui.txt"
  let maze_str = Stdio.In_channel.read_all "./resources/mickey-maze.txt"
  let maze = Maze.create (1, 1) (90, 18) maze_str

  let init_curses () =
    initscr () |> ignore;
    cbreak () |> ignore;
    start_color () |> ignore;
    noecho () |> ignore;
    keypad (stdscr ()) true |> ignore;
    curs_set 0 |> ignore;
    init_pair 1 Color.white Color.blue |> ignore;
    init_pair 2 Color.white Color.red |> ignore
  ;;

  let draw_entities () =
    mvaddstr 0 0 ui_str |> ignore;
    mvaddstr 5 0 maze_str |> ignore;
    let mouse_x, mouse_y = maze.mouse_pos in
    let exit_x, exit_y = maze.exit_pos in
    attron A.bold |> ignore;
    attron (A.color_pair 1) |> ignore;
    mvaddch (mouse_y + 5) mouse_x (int_of_char 'M') |> ignore;
    attroff (A.color_pair 1) |> ignore;
    attron (A.color_pair 2) |> ignore;
    mvaddch (exit_y + 5) exit_x (int_of_char 'E') |> ignore;
    attroff (A.color_pair 2) |> ignore;
    attroff A.bold |> ignore;
    refresh () |> ignore
  ;;

  let stop () =
    clear ();
    addstr "Goodbye" |> ignore;
    refresh () |> ignore;
    Thread.delay 1.0;
    endwin ();
    exit 0
  ;;

  let move_mouse dir =
    let new_x, new_y =
      let x, y = maze.mouse_pos in
      match dir with
      | Up -> x, y - 1
      | Right -> x + 1, y
      | Down -> x, y + 1
      | Left -> x - 1, y
    in
    if (new_x, new_y) = maze.exit_pos
    then stop ()
    else if (new_x >= 0 && new_x < maze.width)
            && new_y >= 0
            && new_y < maze.height
            && maze.walls.(new_y).(new_x) <> 1
    then maze.mouse_pos <- new_x, new_y
    else ()
  ;;

  let rec loop () =
    clear ();
    draw_entities ();
    begin
      match getch () with
      | 27 -> stop ()
      | 0o402 -> move_mouse Down
      | 0o403 -> move_mouse Up
      | 0o404 -> move_mouse Left
      | 0o405 -> move_mouse Right
      | _ -> ()
    end;
    loop ()
  ;;

  let start () =
    init_curses ();
    loop ()
  ;;
end
;;

App.start ()
