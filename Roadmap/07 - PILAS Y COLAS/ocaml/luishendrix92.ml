open Printf

(*/------------------------------------------------------------------------\
  |                                                                        |
  |                          Stack Data Structure                          |
  |                                                                        |
  |  A {e stack} is a {b LIFO} data structure that contains      <Top>     |
  |  elements that are added one on top of the other like,      ╔═════╗    |
  |  for example, in a stack of dirty plates at a restaurant. ┌─║  3  ║    |
  |  LIFO means {e Last In First Out}; the latest item put    │ ╠═════╣    |
  |  into the stack is also the first one taken out of it.    └>║  2  ║─┐  |
  |  Bascially, adding and taking from the top is a O(1)        ╠═════║ │  |
  |  operation (constant time), which reminds us of a singly  ┌─║  1  ║<┘  |
  |  linked list, and as a matter of fact, it's implemented   │ ╠═════╣    |
  |  pretty much in the same way or using one as its backend. └>║  E  ║    |
  |                                                             ╚═════╝    |
  |  Stacks are useful in areas like recursion optimization,    <Bottom>   |
  |  low level function writting, reversing of collections,                |
  |  lexical evaluation of tokens (I.E reverse polish notation), the       |
  |  memento pattern for undo/redo operations, backtracking, and more!     |
  |                                                                        |
  |  In the module signature below you can see the most common interface   |
  |  for stacks. Each function signature ([val <identifier> : type]) has   |
  |  a comment describing what the opertion does among other details.      |
  |                                                                        |
  |  NOTE: In the diagram, the bottom cell [E] represents the empty node   |
  |  often associated to linked lists; it represents an empty structure    |
  |  and serves as a signal to stop recursion or iteration.                |
  |                                                                        |
  \------------------------------------------------------------------------/*)

(** Last-In-First-Out data structure with constant access and insertion
    time on the front side. This module performs in-place modification. *)
module type LIFO = sig
  (** The type of stack containing elements of type ['a]. *)
  type 'a t

  (** [create ()] returns a {b mutable} empty stack. *)
  val create : unit -> 'a t

  (** [push elt s] adds [elt] to the top of a stack [s]. *)
  val push : 'a -> 'a t -> unit

  (** [pop s] removes and returns the topmost element of a stack [s].
      If the stack is empty, returns [None], otherwise, [Some] element. *)
  val pop : 'a t -> 'a option

  (** [peek s] returns the topmost element of [s] without removing it.
      If the stack is empty, returns [None], otherwise, [Some] element. *)
  val peek : 'a t -> 'a option

  (** [size s] returns the amount of elements in a stack [s]. *)
  val size : 'a t -> int

  (** [is_empty s] is [true] when [size s = 0], and [false] otherwise. *)
  val is_empty : 'a t -> bool

  (** [iter s ~f] calls a function [f] of all elements of a stack [s]. *)
  val iter : f:('a -> unit) -> 'a t -> unit

  (** [clear s] removes all elements from a stack [s], making it empty. *)
  val clear : 'a t -> unit
end

(*/------------------------------------------------------------------------\
  |                                                                        |
  |                          Queue Data Structure                          |
  |                                                                        |
  |  A queue is a FIFO data structure that can perform insertion on the    | 
  |  back and access/deletion on the front, all in constant time [O(1)].   |
  |  {b FIFO} stands for {e First In First Out] and it tells us that       |
  |  when we add elements to the collection, they are added behind the     |
  |  latest one (the {e rear}) and when it's time to process the elements  |
  |  in it, a {e dequeue} operation is performed which removes the first   |
  |  element that was inserted (and then the second, and so on).           |
  |                                                                        |
  |  You can find queues being used in graph-related algorithms such as    |
  |  Breadth-First search for shortest paths, as a simple solution for     |
  |  resource pooling, in distributed software (like RabbitMQ), server     |
  |  request processing, task scheduling, event handling, printers, and    |
  |  much more! There are many implementations here is a rough diagram:    |
  |                                                                        |
  |              <Front>                     <Rear>                        |
  |              ╔═══╗  ╔═══╗  ╔═══╗  ╔═══╗  ╔═══╗  ╔═══════╗              |
  |              ║ 1 ║->║ 2 ║->║ 3 ║->║ 4 ║->║ 5 ║->║ Empty ║              |
  |              ╚═══╝  ╚═══╝  ╚═══╝  ╚═══╝  ╚═══╝  ╚═══════╝              |
  |              First (Dequeue)             Last (Enqueue)                |
  |                                                                        |
  |  In the module signature below you can see the most common interface   |
  |  for queues. Each function signature ([val <identifier> : type]) has   |
  |  a comment describing what the opertion does among other details.      |
  |    As a quick note, [iter] is just an OCaml convention for [forEach]   |
  |  in other programming languages. For simplicity's sake I left out      |
  |  other useful operations such as [map], [filter], [fold], [is_full],   |
  |  [of_list], [of_array], [singleton], [bind], [take_n], [add_n], etc.   |
  |                                                                        |
  \------------------------------------------------------------------------/*)

(** First-In-First-Out data structure with constant access time at the front,
    and constant insertion time at the rear. Performs in-place modification. *)
module type FIFO = sig
  (** The type of queue containing elements of type ['a]. *)
  type 'a t

  (** [create ()] returns a {b mutable} empty queue. *)
  val create : unit -> 'a t

  (** [enqueue elt q] adds [elt] to the front of queue [q]. *)
  val enqueue : 'a -> 'a t -> unit

  (** [dequeue q] removes the first element at the front of queue [q] and
      returns it. The retured value is wrapped in an [option] type. *)
  val dequeue : 'a t -> 'a option

  (** [front q] returns the first element at the front of queue [q]. The
      returned value is wrapped in an [option] type. *)
  val front : 'a t -> 'a option

  (** [size q] is the current length of the queue [q]. *)
  val size : 'a t -> int

  (** [is_empty q] is [true] if [size q = 0], otherwise it's [false]. *)
  val is_empty : 'a t -> bool

  (** [iter ~f q] calls a consumer function [f] on all elements of [q]. *)
  val iter : f:('a -> unit) -> 'a t -> unit

  (** [clear q] empties a queue [q] by removing all its elements. *)
  val clear : 'a t -> unit
end

(*/------------------------------------------------------------------------\
  |                                                                        |
  |                         Stack Implementations                          |
  |                                                                        |
  |  TODO: Fill this section during a future review.                       |
  |                                                                        |
  \------------------------------------------------------------------------/*)

module Stack : LIFO = struct
  (* I could have also used my own definition of a linked list:
     [type 'a t = | Empty | Node of ('a * 'a t)].

     Similar to the standard library: [Nil | Cons of ('a * 'a t)].
     If I were to create a single element stack: [Node (5, Empty)]...
     Or push 6 and 7 to that stack: [Node (7, Node (6, Node (5, Empty)))]...
     Or pop from it by returning the value, and the updated stack:
     [let pop = function | Node (h, tl) -> Some (h, tl) | Empty -> None]. *)
  type 'a t =
    { mutable length : int
    ; mutable items : 'a list
    }

  let create () = { length = 0; items = [] }

  let push elt s =
    s.items <- elt :: s.items;
    s.length <- s.length + 1
  ;;

  let pop s =
    match s.items with
    | item :: rest ->
      s.items <- rest;
      s.length <- s.length - 1;
      Some item
    | [] -> None
  ;;

  let peek s =
    match s.items with
    | item :: _ -> Some item
    | [] -> None
  ;;

  let clear s =
    s.items <- [];
    s.length <- 0
  ;;

  let size s = s.length
  let is_empty s = s.length = 0
  let iter ~f s = List.iter f s.items
end
;;

(* Just because the code typechecks doesn't mean it will work 100% as intended.
   That's why I have to make sure my stack (and queue) works by creating a few
   {e assertions} that will throw an exception if they're [false]. *)
let test_stack = Stack.create () in
let f_exec_count = ref 0 in
let iteration_values : int list ref = ref [] in
let open Stack in
begin
  (* A newly created stack:

     - Must be empty by default.
     - Must return [None] if peeked and popped at.
     - Must have a size of 0.
     - Must not be iterated with a function [f]. *)
  assert (is_empty test_stack);
  assert (peek test_stack = None);
  assert (pop test_stack = None);
  assert (size test_stack = 0);
  iter ~f:(fun _ -> incr f_exec_count) test_stack;
  assert (!f_exec_count = 0);
  (* After pushing one element, the stack:

     - Must not be empty.
     - Must return [Some 'a] if peeked at.
     - Must have a size of 1. *)
  push 1 test_stack;
  assert (is_empty test_stack = false);
  assert (peek test_stack = Some 1);
  assert (size test_stack = 1);
  (* After pushing nine more elements, the stack:

     - Must return the last insertion if peeked at.
     - Must iterate its elements in order of last to firt.
     - Must have a size of 10. *)
  for i = 2 to 10 do
    push i test_stack
  done;
  assert (peek test_stack = Some 10);
  iter ~f:(fun n -> iteration_values := n :: !iteration_values) test_stack;
  assert (!iteration_values = [ 1; 2; 3; 4; 5; 6; 7; 8; 9; 10 ]);
  assert (size test_stack = 10);
  (* After popping once from it, the stack:

     - Must have returned and deleted the topmost element.
     - Must now have a size of 9.
     - Peeking at it returns the second to last inserted element. *)
  let popped = pop test_stack in
  assert (popped = Some 10);
  assert (size test_stack = 9);
  assert (peek test_stack = Some 9);
  (* After popping nine times from it, the stack:

     - Must have returned the popped elements in order.
     - Must now be empty and have size of 0. *)
  let popped_list =
    Seq.(
      init 9 Int.succ
      |> fold_left (fun acc _ -> (pop test_stack |> Option.get) :: acc) [])
  in
  assert (popped_list = [ 1; 2; 3; 4; 5; 6; 7; 8; 9 ]);
  assert (is_empty test_stack && size test_stack = 0)
end

(*/------------------------------------------------------------------------\
  |                                                                        |
  |                         Queue Implementations                          |
  |                                                                        |
  |  TODO: Fill this section during a future review.                       |
  |                                                                        |
  \------------------------------------------------------------------------/*)

module Queue : FIFO = struct
  type 'a node =
    | Empty
    | Node of
        { value : 'a
        ; mutable next : 'a node
        }

  type 'a t =
    { mutable length : int
    ; mutable front : 'a node
    ; mutable rear : 'a node
    }

  let create () = { length = 0; front = Empty; rear = Empty }

  let enqueue elt q =
    let to_insert = Node { value = elt; next = Empty } in
    (* TODO: Replace with an if statement and is_empty. *)
    (match q.rear with
     | Empty -> q.front <- to_insert
     | Node last -> last.next <- to_insert);
    q.rear <- to_insert;
    q.length <- q.length + 1
  ;;

  let clear q =
    begin
      q.length <- 0;
      q.front <- Empty;
      q.rear <- Empty
    end
  ;;

  let dequeue q =
    match q.front with
    | Empty -> None
    | Node { value; next } ->
      if next = Empty
      then clear q
      else (
        q.length <- q.length - 1;
        q.front <- next);
      Some value
  ;;

  let front q =
    match q.front with
    | Empty -> None
    | Node first -> Some first.value
  ;;

  let iter ~f q =
    let rec aux f = function
      | Empty -> ()
      | Node { value; next } ->
        f value;
        aux f next
    in
    aux f q.front
  ;;

  let size q = q.length
  let is_empty q = size q = 0
end
;;

let test_queue = Queue.create () in
let f_exec_count = ref 0 in
let iteration_values : int list ref = ref [] in
let open Queue in
begin
  (* A newly created queue:

     - Must be empty by default.
     - Must return [None] if peeked and dequeued.
     - Must have a size of 0.
     - Must not be iterated with a function [f]. *)
  assert (is_empty test_queue);
  assert (front test_queue = None);
  assert (dequeue test_queue = None);
  assert (size test_queue = 0);
  iter ~f:(fun _ -> incr f_exec_count) test_queue;
  assert (!f_exec_count = 0);
  (* After enqueueing one element, the queue:

     - Must not be empty.
     - Must return [Some 'a] if peeked at.
     - Must have a size of 1. *)
  enqueue 1 test_queue;
  assert (is_empty test_queue = false);
  assert (front test_queue = Some 1);
  assert (size test_queue = 1);
  (* After enqueueing nine more elements, the queue:

     - Must return the first insertion (1) if peeked at.
     - Must iterate its elements in order of first to last.
     - Must have a size of 10. *)
  for i = 2 to 10 do
    enqueue i test_queue
  done;
  assert (front test_queue = Some 1);
  iter ~f:(fun n -> iteration_values := n :: !iteration_values) test_queue;
  assert (!iteration_values = [ 10; 9; 8; 7; 6; 5; 4; 3; 2; 1 ]);
  assert (size test_queue = 10);
  (* After dequeueing once, the queue:

     - Must have returned and deleted the first element.
     - Must now have a size of 9.
     - Peeking it returns the second element (2). *)
  let dequeued = dequeue test_queue in
  assert (dequeued = Some 1);
  assert (size test_queue = 9);
  assert (front test_queue = Some 2);
  (* After dequeueint nine times, the queue:

     - Must have returned the dequeued elements in order.
     - Must now be empty and have size of 0. *)
  let dequeue_list =
    Seq.(
      init 9 Int.succ
      |> fold_left (fun acc _ -> (dequeue test_queue |> Option.get) :: acc) [])
  in
  assert (dequeue_list = [ 10; 9; 8; 7; 6; 5; 4; 3; 2 ]);
  assert (is_empty test_queue && size test_queue = 0)
end

(*/------------------------------------------------------------------------\
  |                                                                        |
  |                     DIFICULTAD EXTRA (Opcional)                        |
  |                                                                        |
  |  - Utilizando la implementación de pila y cadenas de texto, simula     |
  |    el mecanismo adelante/atrás de un navegador web. Crea un programa   |
  |    en el que puedas navegar a una página o indicarle que te quieres    |
  |    desplazar adelante o atrás, mostrando en cada caso el nombre de     |
  |    la web. Las palabras "adelante", "atras" desencadenan esta acción,  |
  |    el resto se interpreta como el nombre de una nueva web.             |
  |                                                                        |
  |  - Utilizando la implementación de cola y cadenas de texto, simula el  |
  |    mecanismo de una impresora compartida que recibe documentos y los   |
  |    imprime cuando así se le indica. La palabra "imprimir" imprime un   |
  |    elemento de la cola, el resto de palabras se interpretan como       |
  |    nombres de documentos.                                              |
  |                                                                        |
  \------------------------------------------------------------------------/*)

module BrowserExample = struct
  type website = string * string (* title , url *)

  type history =
    { past : website Stack.t
    ; mutable present : website
    ; future : website Stack.t
    }

  type action =
    | BrowseTo of website
    | GoForward
    | GoBack

  let display_history { past; present = title, url; future } =
    print_endline
      "----------------------------------------------------------------";
    printf "MoureFox> Now browsing [%s] (URL: %s)\n" title url;
    printf
      "└───────> Web Browsing History: %d [◀] - [▶] %d\n\n"
      (Stack.size past)
      (Stack.size future)
  ;;

  (* TODO: Find a way to make this function's code less DRY. *)
  let dispatch h action =
    begin
      match action with
      | BrowseTo web ->
        Stack.push h.present h.past;
        printf "MoureFox> Added [%s] to the past stack.\n" (fst h.present);
        h.present <- web
      | GoForward ->
        Stack.push h.present h.past;
        printf "MoureFox> Added [%s] to the past stack.\n" (fst h.present);
        (match Stack.pop h.future with
         | Some web ->
           printf "MoureFox> Removed [%s] from the future stack.\n" (fst web);
           h.present <- web
         | None -> print_endline "The future stack is empty, can't go forward.")
      | GoBack ->
        Stack.push h.present h.future;
        printf "MoureFox> Added [%s] to the future stack.\n" (fst h.present);
        (match Stack.pop h.past with
         | Some web ->
           printf "MoureFox> Removed [%s] from the past stack.\n" (fst web);
           h.present <- web
         | None -> print_endline "The past stack is empty, can't go back.")
    end;
    display_history h
  ;;

  let run () =
    let browser_history =
      { past = Stack.create ()
      ; present = "New Tab", "chrome://newtab"
      ; future = Stack.create ()
      }
    in
    begin
      print_endline
        "Mr. Moure is done with today's work. Time for some web browsing!";
      print_endline "He sits on his chair and opens a very dumb web browser...";
      display_history browser_history;
      print_endline "He first clicks on a bookmark that looks like a letter X.";
      dispatch browser_history
      @@ BrowseTo ("Inicio / X", "https://twitter.com/home");
      print_endline
        "A random link in a tweet catches his attention and cliks on it.";
      dispatch browser_history @@ BrowseTo ("Project IDX", "https://idx.dev/");
      print_endline
        "He is so impressed with it, his Discord must know about it too!";
      dispatch browser_history
      @@ BrowseTo
           ( "Discord | MoureDev"
           , "https://discord.com/channels/729672926432985098" );
      print_endline
        "And so do his Twitter followers; he clicks on 'Go Back' twice.";
      dispatch browser_history GoBack;
      dispatch browser_history GoBack;
      print_endline
        "Lastly, a click to 'Go Forward' to go back to IDX and call it a day.";
      dispatch browser_history GoForward
    end
  ;;
end
;;

BrowserExample.run ()
(* Output of the example scenario:

   Mr. Moure is done with today's work. Time for some web browsing!
   He sits on his chair and opens a very dumb web browser...
   ----------------------------------------------------------------
   MoureFox> Now browsing [New Tab] (URL: N/A)
   └───────> Web Browsing History: 0 [◀] - [▶] 0

   He first clicks on a bookmark that looks like a letter X.
   MoureFox> Added [New Tab] to the past stack.
   ----------------------------------------------------------------
   MoureFox> Now browsing [Inicio / X] (URL: https://twitter.com/home)
   └───────> Web Browsing History: 1 [◀] - [▶] 0

   A random link in a tweet catches his attention and cliks on it.
   MoureFox> Added [Inicio / X] to the past stack.
   ----------------------------------------------------------------
   MoureFox> Now browsing [Project IDX] (URL: https://idx.dev/)
   └───────> Web Browsing History: 2 [◀] - [▶] 0

   He is so impressed with it, his Discord must know about it too!
   MoureFox> Added [Project IDX] to the past stack.
   ----------------------------------------------------------------
   MoureFox> Now browsing [Discord | MoureDev] (URL: https://discord.com/channels/729672926432985098)
   └───────> Web Browsing History: 3 [◀] - [▶] 0

   And so do his Twitter followers; he clicks on 'Go Back' twice.
   MoureFox> Added [Discord | MoureDev] to the future stack.
   MoureFox> Removed [Project IDX] from the past stack.
   ----------------------------------------------------------------
   MoureFox> Now browsing [Project IDX] (URL: https://idx.dev/)
   └───────> Web Browsing History: 2 [◀] - [▶] 1

   MoureFox> Added [Project IDX] to the future stack.
   MoureFox> Removed [Inicio / X] from the past stack.
   ----------------------------------------------------------------
   MoureFox> Now browsing [Inicio / X] (URL: https://twitter.com/home)
   └───────> Web Browsing History: 1 [◀] - [▶] 2

   Lastly, a click to 'Go Forward' to go back to IDX and call it a day.
   MoureFox> Added [Inicio / X] to the past stack.
   MoureFox> Removed [Project IDX] from the future stack.
   ----------------------------------------------------------------
   MoureFox> Now browsing [Project IDX] (URL: https://idx.dev/)
   └───────> Web Browsing History: 2 [◀] - [▶] 1
*)

(* TODO: Complete the printer exercise. *)
