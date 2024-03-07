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
  |  The most common implementation of a stack is a singly-linked list.    |
  |  As a quick reminder: a SLL is a data structure formed with nodes      |
  |  that hold a value and point to the next node which can calso be       |
  |  a null terminator to signal that the end of the list was reached.     |
  |    In imperative languages we can just create a [struct] that lives    |
  |  in a random place in memory and points to another node or [null] by   |
  |  reference; or they are implemented with an array which is a mutable   |
  |  and sequential (in RAM) data structure with finite size.              |
  |  Now, in functional programming languages that are able to define      |
  |  variant types such as Haskell, OCaml, Rust, etc; the type can be      |
  |  defined as a recursive parameterized variant similar to that of a     |
  |  singly linked list but with limited operations and semantics.         |
  |                                                                        |
  |  Using an [Array] as the underlying type introduces a new concern:     |
  |  dealing with the finite nature of it. We can just leave the stack     |
  |  finite and throw an exception (or return an [Error] result) when      |
  |  the client tries to push elements into a full stack. Or we could      |
  |  implement a similar mechanism to the [ArrayList] type in {e Java}     |
  |  which automatically replaces the original array with a new one of     |
  |  greater length and all the elements of the original copied.           |
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
  |  Queues are a little bit harder to implement because inserting at the  |
  |  rear of a collection needs to be a constant time operation just as    |
  |  removing and accessing the front of it. There are 2 main ways of      |
  |  doing it and the first one is to have either 2 lists or a list and a  |
  |  reference to the last node. Having 2 lists achieves immutability      |
  |  at the cost of having to reverse the rear every time an element is    |
  |  {e dequeued}; and having a list as the front along with a reference   |
  |  to its last element as the rear achieves constant time operations at  |
  |  the very small cost of having to manage pointers and memory in low    |
  |  level languages, and having to update references in high level        |
  |  imperative languages. Thankfully, OCaml provides mutable record       |
  |  fields which allow us to implement queues the imperative way.         |
  |                                                                        |
  |  Using arrays, just like with stacks, makes things a bit easier but    |
  |  we still have to solve the limited length problem and in order not    |
  |  to waste blocks, we need to implement it as a {b circular array}.     |
  |                                                                        |
  |            ┌────R───────────F───────────────────┐                      |
  |            │  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗ │  F=Front             |
  |            └─>║ 9 ║   ║   ║ 4 ║ 5 ║ 6 ║ 7 ║ 8 ║─┘  R=Rear              |
  |               ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝                        |
  |                 0   1   2   3   4   5   6   7                          |
  |                                                                        |
  |               i=0               As the diagram illustrates, there is   |
  |              ┌───┐              really nothing circular about the      |
  |        i=7   │ 9 │   i=1        array's shape. The name comes from     |
  |       ┌───┐  └───┘  ┌───┐       the use of the {e modulo} operator     |
  |       │ 8 │         │   │       to compute the index of the next       |
  |   i=6 └───┘         └───┘ i=2   block to enqueue an element into.      |
  |  ┌───┐                   ┌───┐                                         |
  |  │ 7 │                   │   │  The modulo operator will return 0 if   |
  |  └───┘ i=5           i=3 └───┘  the next index is equal to the length  |
  |       ┌───┐         ┌───┐       of the array, thus giving us the       |
  |       │ 6 │   i=4   │ 4 │       illusion of a cyclic iteration.        |
  |       └───┘  ┌───┐  └───┘       When the rear index [+1] is equal to   |
  |              │ 5 │              the front index, we say it's full.     |
  |              └───┘              The rear and the front indices are     |
  |                                 equal at the start (empty state).      |
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

module CircularQueue : sig
  include FIFO

  val enqueue : 'a -> 'a t -> (unit, 'a) result

  (** [create ?len x] is a mutable circular queue of maximum size [len]. The
      initialization process requires you to pass an placeholder value [x] of
      type ['a] to fill the underlying {e Array} of type ['a array]. If the
      optional argument [len] is not provided, it defaults to [10]. *)
  val create : ?len:int -> 'a -> 'a t

  (** [is_full q] returns [true] if there is no more space for more elements to
      be enqueued into [q]'s rear. [false] is returned otherwise. *)
  val is_full : 'a t -> bool
end = struct
  type 'a t =
    { mutable front : int
    ; mutable rear : int
    ; elements : 'a array
    ; max_size : int
    }

  let create ?(len = 10) x =
    let max_size = if len < 2 then 2 else len in
    { max_size; front = -1; rear = -1; elements = Array.make max_size x }
  ;;

  let is_empty q = q.front = -1 && q.rear = -1
  let is_full q = (q.rear + 1) mod q.max_size = q.front

  let clear q =
    q.front <- -1;
    q.rear <- -1
  ;;

  let enqueue elt q =
    if is_full q
    then Error elt
    else begin
      if not (is_empty q)
      then q.rear <- (q.rear + 1) mod q.max_size
      else begin
        q.front <- 0;
        q.rear <- 0
      end;
      q.elements.(q.rear) <- elt;
      Ok ()
    end
  ;;

  let dequeue q =
    if is_empty q
    then None
    else begin
      let dequeued = Some q.elements.(q.front) in
      if q.front = q.rear
      then clear q
      else q.front <- (q.front + 1) mod q.max_size;
      dequeued
    end
  ;;

  (* The 2nd conditional branch below can be simplified to:
     [1 + q.rear - q.front + q.max_size * Bool.to_int (q.front > q.rear) ]
     ----------------------------------------------------------------------- *)
  let size q =
    if is_empty q
    then 0
    else if q.front <= q.rear
    then q.rear - q.front + 1
    else q.max_size - q.front + q.rear + 1
  ;;

  let iter ~f q =
    if not (is_empty q)
    then
      for i = 0 to size q - 1 do
        f q.elements.((q.front + i) mod q.max_size)
      done
    else ()
  ;;

  let front q = if is_empty q then None else Some q.elements.(q.front)
end

let () =
  let q = Queue.create () in
  (* let q = CircularQueue.create 0 in *)
  let f_exec_count = ref 0 in
  let iteration_values : int list ref = ref [] in
  let open Queue in
  (* let open CircularQueue in *)
  begin
    (* A newly created queue:

       - Must be empty by default.
       - Must return [None] if peeked and dequeued.
       - Must have a size of 0.
       - Must not be iterated with a function [f]. *)
    assert (is_empty q);
    assert (front q = None);
    assert (dequeue q = None);
    assert (size q = 0);
    iter ~f:(fun _ -> incr f_exec_count) q;
    assert (!f_exec_count = 0);
    (* After enqueueing one element, the queue:

       - Must not be empty.
       - Must return [Some 'a] if peeked at.
       - Must have a size of 1. *)
    enqueue 1 q;
    assert (is_empty q = false);
    assert (front q = Some 1);
    assert (size q = 1);
    (* After enqueueing nine more elements, the queue:

       - Must return the first insertion (1) if peeked at.
       - Must iterate its elements in order of first to last.
       - Must have a size of 10. *)
    for i = 2 to 10 do
      enqueue i q
    done;
    assert (front q = Some 1);
    iter ~f:(fun n -> iteration_values := n :: !iteration_values) q;
    assert (!iteration_values = [ 10; 9; 8; 7; 6; 5; 4; 3; 2; 1 ]);
    assert (size q = 10);
    (* After dequeueing once, the queue:

       - Must have returned and deleted the first element.
       - Must now have a size of 9.
       - Peeking it returns the second element (2). *)
    let dequeued = dequeue q in
    assert (dequeued = Some 1);
    assert (size q = 9);
    assert (front q = Some 2);
    (* After dequeueint nine times, the queue:

       - Must have returned the dequeued elements in order.
       - Must now be empty and have size of 0. *)
    let dequeue_list =
      Seq.(
        init 9 Int.succ
        |> fold_left (fun acc _ -> (dequeue q |> Option.get) :: acc) [])
    in
    assert (dequeue_list = [ 10; 9; 8; 7; 6; 5; 4; 3; 2 ]);
    assert (is_empty q && size q = 0)
  end
;;

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

(* BrowserExample.run () *)
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

module PrinterExample = struct
  let printer = CircularQueue.create ~len:5 ""

  let run () =
    print_endline "A shared printer sits on a desk ready to be used.";
    print_endline
      "One of the officer workers decides to print [2024Q1report.xlsx].";
    Result.get_ok @@ CircularQueue.enqueue "2024Q1report.xlsx" printer;
    print_endline
      "Shortly after that, before the printer even begins to print the";
    print_endline
      "previous document, the CEO queues [vacation.pdf] and [vendor.docx]!";
    Result.get_ok @@ CircularQueue.enqueue "vacation.pdf" printer;
    Result.get_ok @@ CircularQueue.enqueue "vendor.docx" printer;
    let dequeued = CircularQueue.dequeue printer in
    printf
      "Printer> Document [%s] finished printing.\n"
      (Core.Option.value_exn dequeued);
    print_endline "Printer> Here's the printing queue:";
    CircularQueue.iter ~f:print_endline printer;
    print_endline "The rest of the queue finishes printing.";
    while CircularQueue.dequeue printer <> None do
      ()
    done;
    print_endline "5 more documents are queued, making the queue full...";
    for i = 1 to 5 do
      Result.get_ok
      @@ CircularQueue.enqueue (sprintf "document%d.pdf" i) printer
    done;
    print_endline "Printer> Here's the printing queue:";
    CircularQueue.iter ~f:print_endline printer;
    print_endline "then, the CFO wants to queue [payroll.xls] but she can't.";
    begin
      match CircularQueue.enqueue "payroll.xls" printer with
      | Error doc ->
        printf "Printer> ERROR: Could not enequeue [%s], queue is full.\n" doc
      | Ok () -> ()
    end
  ;;
end
;;

PrinterExample.run ()
