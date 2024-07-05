open Printf

let ( let* ) = Result.bind

(******************************************************************************)
(*                                                                            *)
(*                      Single Responsibility Principle                       *)
(*                                                                            *)
(*  The 'S' in {b SOLID}, says that classes and functions should only do one  *)
(*  thing and they should do it very well; meaning, have a single responsi-   *)
(*  bility. It discourages mixing concerns in a class or function and         *)
(*  encourages the developer to separate these concerns into classes that     *)
(*  only {e have one reason to change}, as Bob Martin said in his book,       *)
(*  Clean Code, which is the originator of the SOLID principles.              *)
(*                                                                            *)
(******************************************************************************)

module ViolatesSRP = struct
  let responsibility_1 () = print_endline "I do one thing"
  let responsibility_2 () = print_endline "I do another thing"
  let responsibility_3 () = print_endline "And yet another thing..."

  let use_all_three () =
    responsibility_1 ();
    responsibility_2 ();
    responsibility_3 ()
  ;;
end

(* The module above is in violation of the SRP, it defines three different
   functions that should exist on their own, otherwise whenever we wanted
   to change any of them, we'd have to modify the same module, potentially
   introducing bugs and making them exclusive to the host module.

   The solution is to create a module for each responsibility so that if
   such code has to change, I know exactly where to go. *)

module ResponsibilityOne = struct
  let one_thing () = print_endline "I do one thing"
end

module ResponsibilityTwo = struct
  let another_thing () = print_endline "I do another thing"
end

module ResponsibilityThree = struct
  let yet_another () = print_endline "And yet another thing..."
end

module SRPCompliant = struct
  let use_all_three () =
    ResponsibilityOne.one_thing ();
    ResponsibilityTwo.another_thing ();
    ResponsibilityThree.yet_another ()
  ;;
end

(*****************************************************************************)
(*                                                                           *)
(* DIFICULTAD EXTRA (opcional):                                              *)
(*                                                                           *)
(* Desarrolla un sistema de gestión para una biblioteca. El sistema necesita *)
(* manejar diferentes aspectos como el registro de libros, la gestión de     *)
(* usuarios y el procesamiento de préstamos de libros.                       *)
(*                                                                           *)
(* Requisitos:                                                               *)
(* 1. Registrar libros: El sistema debe permitir agregar nuevos libros con   *)
(*    información básica como título, autor y número de copias disponibles. *)
(* 2. Registrar usuarios: Debe permitir agregar nuevos usuarios con info *)
(*    básica como nombre, número de identificación y correo electrónico. *)
(* 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios  *)
(*    tomar prestados y devolver libros.                                     *)
(*                                                                           *)
(* Instrucciones:                                                            *)
(* 1. Diseña una clase que no cumple: Crea una clase Library que maneje      *)
(*    los tres aspectos mencionados anteriormente (registro de libros,       *)
(*    usuarios y procesamiento de préstamos).                                *)
(* 2. Refactoriza el código: Separa las responsabilidades en diferentes      *)
(*    clases siguiendo el Principio de Responsabilidad Única.                *)
(*                                                                           *)
(*****************************************************************************)

module Library = struct
  type book =
    { title : string
    ; author : string
    ; mutable stock : int
    }

  type user =
    { id : int
    ; name : string
    ; email : string
    }

  module LendingSet = Set.Make (struct
      type t = int * string

      let compare = Stdlib.compare
    end)

  let books : book list ref =
    ref
      [ { title = "Dune"; author = "Frank Herbert"; stock = 5 }
      ; { title = "Lord of the Rings"; author = "J.R.R Tolkien"; stock = 2 }
      ; { title = "Eye of the world"; author = "Robert Jordan"; stock = 3 }
      ; { title = "It"; author = "Stephen King"; stock = 8 }
      ; { title = "Develop a second brain"; author = "Thiago Forte"; stock = 6 }
      ]
  ;;

  let users : user list ref =
    ref [ { id = 1; name = "Luis Lopez"; email = "luishendrix92@gmail.com" } ]
  ;;

  let lendings : LendingSet.t ref = ref LendingSet.empty
  let register_user user = users := user :: !users
  let add_book book = books := book :: !books

  let lend_book user_id book_title =
    let book =
      match List.find_opt (fun book -> book.title = book_title) !books with
      | None -> failwith (sprintf "Book [%s] not found" book_title)
      | Some book -> book
    in
    if book.stock > 0
    then begin
      lendings := LendingSet.add (user_id, book_title) !lendings;
      book.stock <- book.stock - 1
    end
    else failwith (sprintf "Not enough stock for [%s]" book_title)
  ;;

  let return_book user_id book_title =
    let should_return = LendingSet.mem (user_id, book_title) !lendings in
    if should_return
    then begin
      let book =
        match List.find_opt (fun book -> book.title = book_title) !books with
        | None -> failwith (sprintf "Book [%s] not found" book_title)
        | Some book -> book
      in
      lendings := LendingSet.remove (user_id, book_title) !lendings;
      book.stock <- book.stock + 1
    end
    else
      failwith
        (sprintf "User #%d doesn't need to return [%s]" user_id book_title)
  ;;
end

(* Refactoring Opportunity
   -----------------------
   I can apply SRP to separate the monolith of code into modules that do one
   thing only, and very well. For this particular case I can implement an
   entity data module for books, lendings, and users; then create a repository
   functor to have a static storage (Hashtbl) interfaced through convenient
   functions for retrieving, deleting, and adding these entities. *)

module type Entity = sig
  type id
  type t

  val get_id : t -> id
end

module Repository (E : Entity) = struct
  let data : (E.id, E.t) Hashtbl.t = Hashtbl.create 100
  let save elt = Hashtbl.replace data (E.get_id elt) elt

  let add elt =
    if Hashtbl.mem data (E.get_id elt)
    then Error "Unable to add entity, already exists."
    else (
      save elt;
      Ok ())
  ;;

  let delete_by_id elt_id =
    if Hashtbl.mem data elt_id
    then Ok (Hashtbl.remove data elt_id)
    else Error "Can't delete, id doesn't exit."
  ;;

  let get_by_id elt_id =
    match Hashtbl.find_opt data elt_id with
    | Some elt -> Ok elt
    | None -> Error "Entity not found with the provided id."
  ;;
end

module User = struct
  type id = int

  type t =
    { id : int
    ; name : string
    ; email : string
    }

  let get_id user = user.id
end

module Book = struct
  type id = string

  type t =
    { title : string
    ; author : string
    ; mutable stock : int
    }

  let get_id book = book.title
end

module Lending = struct
  type id = User.id * Book.id

  type t =
    { user_id : User.id
    ; book_id : Book.id
    ; return_date : string
    }

  let get_id lending = lending.user_id, lending.book_id
end

module SRPCompliantLibrary = struct
  (* Ideally, we should be able to use dependency injection here and while
     technically we can by using functors, the syntax isn't very intuitive
     and extension-friendly so I'll stick with this code for now. *)
  module Users = Repository (User)
  module Books = Repository (Book)
  module Lendings = Repository (Lending)

  let borrow user_id book_id =
    (* Given I'm not using a proper ORM or writing relationship-aware database
       code, I need to make sure both entities (user and book) exist before
       adding the lending entity, otherwise I'd be violating what in the DB
       world is called a "foreign key" constraint. *)
    let* _user = Users.get_by_id user_id in
    let* book = Books.get_by_id book_id in
    let return_date =
      Core.Date.(
        add_days (today ~zone:Core.Time_float.Zone.utc) 7 |> to_string_american)
    in
    if book.stock > 0
    then begin
      book.stock <- book.stock - 1;
      Lendings.add { user_id; book_id; return_date }
    end
    else Error "Can't lend book, not enough stock"
  ;;

  let return user_id book_id =
    let* _user = Users.get_by_id user_id in
    let* book = Books.get_by_id book_id in
    let* _ = Lendings.delete_by_id (user_id, book_id) in
    Ok (book.stock <- book.stock + 1)
  ;;
end

let _ =
  let open SRPCompliantLibrary in
  let inventory : Book.t list =
    [ { title = "Blood Meridian"; author = "John McCarthy"; stock = 5 }
    ; { title = "The Outsider"; author = "Stephen King"; stock = 2 }
    ; { title = "The Philosopher's Stone"; author = "J.K Rowling"; stock = 0 }
    ]
  in
  List.iter (fun book -> Books.add book |> Result.get_ok) inventory;
  Users.add { id = 1; name = "Luis Lopez"; email = "luishendrix92@gmail.com" }
  |> Result.get_ok;
  let res =
    let user_id = 1 in
    let book_title = "The Outsider" in
    let* _ = borrow user_id book_title in
    printf "User #%d successfully borrowed '%s'\n" user_id book_title;
    let* _ = return user_id book_title in
    printf "User #%d successfully returned '%s'\n" user_id book_title;
    Ok ()
  in
  match res with
  | Ok _ ->
    print_endline "Let's try borrowing a book with no stock!";
    borrow 1 "The Philosopher's Stone" |> Result.get_error |> print_endline
  | Error err -> print_endline err
;;
