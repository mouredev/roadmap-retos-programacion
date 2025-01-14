(******************************************************************************)
(*                                                                            *)
(*                                  Logging                                   *)
(*                                                                            *)
(*  Logging is a practise where the developers of an application display      *)
(*  information about what's going on at runtime to an output channel, which  *)
(*  can be either the standard output channel (aka, the console window), or   *)
(*  a file writter so that we can create and manage log files that can be     *)
(*  used by both developers and users alike to debug a particular problem.    *)
(*                                                                            *)
(*  Logging libraries exist in every language and they all have some things   *)
(*  in common, especially the important concept of a {b level}. A level is    *)
(*  a tier of severity for a message displayed on the channel. For example,   *)
(*  a user can be concerned only with log messages written by the developer   *)
(*  for the end user (also known as "application level"); or maybe it's set   *)
(*  to {e debug} which will display messages intended for displaying the      *)
(*  flow of data structures in a readable manner, which should not be shown   *)
(*  to the end user. That's why loggers have a function to set this level.    *)
(*                                                                            *)
(******************************************************************************)

let stamp_tag : Mtime.span Logs.Tag.def =
  Logs.Tag.def "stamp" ~doc:"Relative monotonic time stamp" Mtime.Span.pp
;;

let stamp c = Logs.Tag.(empty |> add stamp_tag (Mtime_clock.count c))

let log_levels () =
  Logs.app (fun m -> m "This message is only shown at the Logs.App level.");
  (* This message won't be displayed! I set the level to Logs.Info, which is
     one level above Debug. To show it I'd have to change it to Logs.Debug. *)
  Logs.debug (fun m -> m "Only shown during Logs.Debug, ideal for development.");
  Logs.info (fun m -> m "Normal message with information about the processes.");
  Logs.warn (fun m -> m "The ozone layer is in danger :(");
  Logs.err (fun m -> m "Error reporting, recoverable or caught");
  Logs.info (fun m ->
    m "Message with a custom header called 'DONUT'..." ?header:(Some "DONUT"))
;;

(* DIFICULTAD EXTRA (opcional):
   ============================
   Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
   y listar dichas tareas.
   - Añadir: recibe nombre y descripción.
   - Eliminar: por nombre de la tarea.

   Implementa diferentes mensajes de log que muestren información según la
   tarea ejecutada (a tu elección).
   Utiliza el log para visualizar el tiempo de ejecución de cada tarea. *)
module TaskRepository = struct
  type task =
    { name : string
    ; description : string
    }
  [@@deriving show { with_path = false }]

  let tasks : (string, task) Hashtbl.t =
    Logs.info (fun m -> m "TaskRepository hash table initialized");
    Hashtbl.create 100
  ;;

  let add task =
    if Hashtbl.mem tasks task.name
    then
      Logs.warn (fun m ->
        m "Task [%s] already exists so it will be replaced." task.name);
    Hashtbl.replace tasks task.name task;
    Logs.info (fun m -> m "Task [%s] added to the repository." (show_task task))
  ;;

  let remove_by_name name =
    if not (Hashtbl.mem tasks name)
    then
      Logs.err (fun m ->
        m "Task [%s] doesn't exist, therefore it can't be deleted." name)
    else begin
      let task = Hashtbl.find tasks name in
      Hashtbl.remove tasks name;
      Logs.info (fun m -> m "Task %s successfully deleted." (show_task task))
    end
  ;;

  let print_all () =
    Logs.app (fun m -> m "List of pending tasks:");
    Hashtbl.iter
      (fun _ { name; description } ->
        Logs.app (fun m -> m "- %s (#%s)" description name))
      tasks
  ;;
end

let extra_exercise () =
  let c = Mtime_clock.counter () in
  Logs.info (fun m ->
    m "======> Starting 4-task insertion for time measuring...");
  TaskRepository.add
    { name = "milk"; description = "Buy milk at the grocery store" };
  TaskRepository.add
    { name = "exercise"; description = "Have some abdominal exercise b4 sleep" };
  TaskRepository.add
    { name = "email"; description = "Send an email to my parents down south" };
  TaskRepository.add
    { name = "milk"; description = "Borrow milk from grandma instead" };
  (* Adding a tag with the [stamp] function (using the [c] clock counter will
     cause the 2nd header of this particualr log line to display the elapsed
     time (in microseconds) since the task started (counter created)!

     NOTE: On average, inserting these 4 tasks took 40 microseconds. *)
  Logs.info (fun m -> m "...Finished 4-task insertion <======" ~tags:(stamp c));
  TaskRepository.add { name = "delete"; description = "Please delete this!" };
  TaskRepository.remove_by_name "delete";
  TaskRepository.remove_by_name "ghost";
  TaskRepository.print_all ()
;;

(* Boilerplate code for a custom reporter with a timestamp tag
   ----------------------------------------------------------------------------
   This function is a custom reporter that looks through the set of tags and
   extracts the specific one that handles the elapsed span of time since a
   given stimestamp [c] (Monotonic clock tick counter). *)
let reporter ppf =
  let report _src level ~over k msgf =
    let k _ =
      over ();
      k ()
    in
    let with_stamp h tags k ppf fmt =
      let dt =
        Option.(
          bind tags (Logs.Tag.find stamp_tag)
          |> map (fun s -> Mtime.Span.to_float_ns s /. 1_000.0)
          |> map (fun dt -> Printf.sprintf "[%0+4.0fus]" dt)
          |> value ~default:"")
      in
      Format.kfprintf
        k
        ppf
        ("%a%s @[" ^^ fmt ^^ "@]@.")
        Logs.pp_header
        (level, h)
        dt
    in
    msgf @@ fun ?header ?tags fmt -> with_stamp header tags k ppf fmt
  in
  { Logs.report }
;;

let _ =
  Logs.set_reporter (reporter Format.std_formatter);
  Logs.set_level (Some Logs.Info);
  log_levels ();
  print_newline ();
  extra_exercise ();
  ()
;;
