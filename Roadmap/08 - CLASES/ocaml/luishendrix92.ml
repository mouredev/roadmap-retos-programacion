open Printf

(*/------------------------------------------------------------------------\
  |                                                                        |
  |                          Objects and Classes                           |
  |                                                                        |
  |  As a functional programming language, OCaml's main focus is to make   |
  |  use of immutable data and functions as much as possible without       |
  |  reaching the strictly pure levels of Haskell where mutations and      |
  |  side-effects are disallowed in favour of composing IO operations      |
  |  through monads and syntactic sugar with the [do] block. OCaml is a    |
  |  bit more flexible and as I already explored a few exercises ago,      |
  |  the user is more than free (and sometimes encouraged) to write        |
  |  records with mutable fields, references, perform unsafe IO, throw     |
  |  exceptions and even make use of imperative [while] and [for] loops.   |
  |                                                                        |
  |  To my surprise, the language does provide syntactic aid to harness    |
  |  the most used concepts of Object-Oriented Programming: classes,       |
  |  interfaces, virtuals, objects, public and private methods, proper-    |
  |  ties, inheritance, initialization, and instanciation. Sure it may     |
  |  not offer the whole scope of OOP but what we can use is more than     |
  |  enough to satisfy our object-oriented needs.                          |
  |                                                                        |
  |  If you are curious about what is available in terms of OOP, you can   |
  |  check the official manual with complete information about it:         |
  |  https://v2.ocaml.org/manual/objectexamples.html                       |
  |                                                                        |
  \------------------------------------------------------------------------/*)

class animal (name : string) (age : int) (species : string) =
  (* Unlike in OOP languages, we do not always need to specify the [self]
     binding unless we need to call instance methods within the object's
     definition. This reference can't espace the class, for example, to
     store it in an outside container from within. It needs to be done
     from the outside, there might be workarounds but I don't know yet. *)
  object (self : 'a)
    (* There is no way to mutate properties from the outside, it has to be done
       from the inside and expose methods such as getters and setters. *)
    val mutable name = name
    val mutable age = age
    val mutable love = 0

    (* An animal can never change species, therefore this property can just
       be non-mutable, which in terms of OOP languages could be similar to
       [final], [const], and other similar keywords. *)
    val species = species

    (* Methods can be private like in OOP languages *)
    method private increase_love =
      let new_love = love + 1 in
      love <- (if new_love > 100 then 100 else new_love)

    (* The OCaml way of doing getters and setters. *)
    method get_name = name
    method set_name name' = name <- name'
    method get_age = age
    method set_age age' = age <- age'

    method pet =
      self#increase_love;
      printf "%s was petted, its love for you is now Lv.%d!\n" name love

    method greet =
      printf "Hello, my name is %s, I'm a %s of age %d!\n" name species age

    (* In the OCaml Manual, they call methods that accept other objects of the
       same type [binary methods] and they require you to add a type hint to
       the [self] reference (line 36) and use it to annotate the parameter. *)
    method fight (other_animal : 'a) =
      printf "%s and %s are fighting...\n" name other_animal#get_name

    (* The [initializer] keyword allows us to run some code just after the
       instance was creatd. It's similar to a post-constructor hook body. *)
    initializer
      printf
        "Animal name=[%s] species=[%s] age=[%d] was created.\n"
        name
        species
        age
  end

let pickles = new animal "Mr Pickles" 6 "Dog"
let garfield = new animal "Garfield" 14 "Cat"

let () =
  pickles#greet;
  garfield#greet;
  pickles#pet;
  pickles#pet;
  garfield#pet;
  pickles#pet;
  pickles#fight garfield;
  garfield#set_age 20;
  pickles#set_name "Pickles Goodman";
  pickles#greet;
  garfield#greet
;;

(*/------------------------------------------------------------------------\
  |                                                                        |
  |                      DIFICULTAD EXTRA (Opcional)                       |
  |                                                                        |
  |  Implementa dos clases que representen las estructuras de Pila y Cola  |
  |  (estudiadas en el ejercicio número 7 de la ruta de estudio).          |
  |                                                                        |
  |  - Deben poder incializarse y disponer de operaciones para añadir,     |
  |    eliminar, retornar el número de elementos e imiromir todo su        |
  |    contenido.                                                          |
  |                                                                        |
  \------------------------------------------------------------------------/*)

class type ['a] lifo = object
  method push : 'a -> unit
  method pop : 'a option
  method peek : 'a option
  method size : int
  method print : to_str:('a -> string) -> unit
end

(* This interface implementation syntax may be familiar to people coming from
   an object-oriented background but the idiomatic way to do this in OCaml is
   by type-annotating the [self] reference (if it's not used, replace it with
   a [_]) with the type [<type params> #interface] like this:

   {[
     class ['a] stack = object (_self : 'a #lifo) end
   ]}

   The language server's diagnostics behave differently when using one or the
   other. If we use the idiomatic way, it says that the "non virtual class" is
   missing some method implementations which is a very useful error message. *)
class ['a] stack : ['a] lifo =
  object
    val mutable length = 0
    val mutable items = []

    method push elt =
      items <- elt :: items;
      length <- length + 1

    method pop =
      match items with
      | h :: tl ->
        items <- tl;
        length <- length - 1;
        Some h
      | [] -> None

    method print ~to_str =
      let print_node x =
        printf
          "|  %s   |\n+-------+\n"
          (to_str x |> Core.String.pad_left ~char:' ' ~len:2)
      in
      if length > 0
      then begin
        print_endline "Stack Top";
        print_endline "+-------+";
        List.iter print_node items;
        print_endline "Stack Btm"
      end
      else print_endline "Empty Stack"

    method peek = Core.List.hd items
    method size = length
  end

let () =
  let s = new stack in
  s#print ~to_str:string_of_int;
  for i = 1 to 7 do
    s#push i
  done;
  let popped1 = Option.value ~default:0 s#pop in
  let popped2 = Option.value ~default:0 s#pop in
  printf "Popped %d and %d.\n" popped1 popped2;
  s#print ~to_str:string_of_int
;;

(* I will wrap this class inside its own module because I want to encapsulate
   the constuctors for [node] ([Empty] and [Node]). The way it's done is by
   declaring the necessary types, interfaces, and classes while also exposing a
   factory function that instantiates a new object of the underlying class. *)
module Queue = struct
  type 'a node =
    | Empty
    | Node of
        { value : 'a
        ; mutable next : 'a node
        }

  class type ['a] fifo = object
    method enqueue : 'a -> unit
    method dequeue : 'a option
    method first : 'a option
    method size : int
    method print : to_str:('a -> string) -> unit
  end

  class ['a] linear_queue =
    object (self : 'a #fifo)
      val mutable length = 0
      val mutable front : 'a node = Empty
      val mutable rear : 'a node = Empty

      method private clear =
        length <- 0;
        front <- Empty;
        rear <- Empty

      method enqueue elt =
        let to_insert = Node { value = elt; next = Empty } in
        (match rear with
         | Node last -> last.next <- to_insert
         | Empty -> front <- to_insert);
        rear <- to_insert;
        length <- length + 1

      method dequeue =
        match front with
        | Node { value; next = Empty } ->
          self#clear;
          Some value
        | Node { value; next } ->
          length <- length - 1;
          front <- next;
          Some value
        | Empty -> None

      method first =
        match front with
        | Node { value; _ } -> Some value
        | Empty -> None

      method print ~to_str =
        if length > 0
        then begin
          print_string "Queue <front> ";
          let rec iterate node =
            match node with
            | Node { value; next } ->
              printf "[%s]->" (to_str value);
              iterate next
            | Empty -> ()
          in
          iterate front;
          print_endline "[] <rear>"
        end
        else print_endline "Empty Queue"

      method size = length
    end

  let create () = new linear_queue
end

let () =
  let q = Queue.create () in
  q#print ~to_str:string_of_int;
  for i = 1 to 7 do
    q#enqueue i
  done;
  let dequeued1 = Option.value ~default:0 q#dequeue in
  let dequeued2 = Option.value ~default:0 q#dequeue in
  printf "Dequeued %d and %d.\n" dequeued1 dequeued2;
  q#print ~to_str:string_of_int
;;

(* Output of [dune exec reto8]:

   Animal name=[Mr Pickles] species=[Dog] age=[6] was created.
   Animal name=[Garfield] species=[Cat] age=[14] was created.
   Hello, my name is Mr Pickles, I'm a Dog of age 6!
   Hello, my name is Garfield, I'm a Cat of age 14!
   Mr Pickles was petted, its love for you is now Lv.1!
   Mr Pickles was petted, its love for you is now Lv.2!
   Garfield was petted, its love for you is now Lv.1!
   Mr Pickles was petted, its love for you is now Lv.3!
   Mr Pickles and Garfield are fighting...
   Hello, my name is Pickles Goodman, I'm a Dog of age 6!
   Hello, my name is Garfield, I'm a Cat of age 20!
   Empty Stack
   Popped 7 and 6.
   Stack Top
   +-------+
   |   5   |
   +-------+
   |   4   |
   +-------+
   |   3   |
   +-------+
   |   2   |
   +-------+
   |   1   |
   +-------+
   Stack Btm
   Empty Queue
   Dequeued 1 and 2.
   Queue <front> [3]->[4]->[5]->[6]->[7]->[] <rear>
*)
