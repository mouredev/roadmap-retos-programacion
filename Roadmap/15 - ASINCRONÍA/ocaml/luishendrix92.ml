open Lwt_io

(*****************************************************************************)
(*                                                                           *)
(*                Asynchronous Programming (and Concurrency)                 *)
(*                                                                           *)
(*  Concurrency in OCaml is done via Threads, and it can also leverage the   *)
(*  [Domain] data structure for parallel programming. However there are 2    *)
(*  main libraries to handle and wrap async operations: Lwt (acronym for     *)
(*  "lightweight threads") and Async.                                        *)
(*                                                                           *)
(*  Lwt is a promise-like library that wraps IO and Unix operations, among   *)
(*  other tasks that may need to be done concurrently. Many libraries are    *)
(*  built with or on top of it; [cohttp] (HTTP library) is an example.       *)
(*    A new library is on development called Riot which promises Erlang      *)
(*  -like actor concurrency that can be run on multiple cores. But for this  *)
(*  exercise I'm gonna use 3 {e opam} packages:                              *)
(*                                                                           *)
(*  1. [lwt]: The main Lwt package that contains many modules. One of them   *)
(*     is the [Lwt_io] module that wraps your usual IO operations (print,    *)
(*     read_char, read_line, assert, etc). And the core [Lwt] module that    *)
(*     contains the glue functions like [join], [return], [pick], [bind].    *)
(*  2. [lwt.unix]: Unix functions wrapped by promises, like [sleep].         *)
(*  3. [lwt_ppx]: Syntax sugar for [bind] (and other) operations. Example:   *)
(*     [let%lwt ln = Lwt_io.read_line () in printf "I got: %s" ln] instead   *)
(*     of [Lwt_io.read_line () >>= fun ln -> Lwt_io.printf "I got %s" ln].   *)
(*                                                                           *)
(*****************************************************************************)

let time_now () =
  let open Core.Time_float in
  now () |> to_ofday ~zone:Zone.utc |> Ofday.to_sec_string
;;

let delay_function ?(seconds = 1.0) ~name f =
  let%lwt () =
    printf "[%s] will run after %.2f seconds | %s\n" name seconds (time_now ())
  in
  let%lwt () = Lwt_unix.sleep seconds in
  f ();
  printf "[%s] has been called | %s\n" name (time_now ())
;;

(* Output:

   [Ejercicio] will run after 4.00 seconds | 21:22:36
   The answer is 42!
   [Ejercicio] has been called | 21:22:40
*)
let _ =
  Lwt_main.run
  @@ delay_function ~name:"Ejercicio" ~seconds:4.0 (fun () ->
    print_endline "The answer is 42!")
;;

(****************************************************************************)
(*                                                                          *)
(*                        Dificultad Extra (opcional)                       *)
(*                                                                          *)
(*  Utilizando el concepto de asincronía y la función anterior, crea el     *)
(*  siguiente programa que ejecuta en este orden:                           *)
(*                                                                          *)
(*  - Una función C que dura 3 segundos.                                    *)
(*  - Una función B que dura 2 segundos.                                    *)
(*  - Una función A que dura 1 segundo.                                     *)
(*  - Una función D que dura 1 segundo.                                     *)
(*  - Las funciones C, B, y A se ejecutan en paralelo.                      *)
(*  - La función D comienza su ejecición cuando las 3 anteriores finalicén. *)
(*                                                                          *)
(****************************************************************************)

(* Output:

   [C] will run after 3.00 seconds | 22:02:10
   [B] will run after 2.00 seconds | 22:02:10
   [A] will run after 1.00 seconds | 22:02:10
   Uploaded image family.jpg
   [A] has been called | 22:02:11
   Response from server: Error 404
   [B] has been called | 22:02:12
   Successfully downloaded avengers.mp4
   [C] has been called | 22:02:13
   [D] will run after 1.00 seconds | 22:02:13
   Processed results, goodbye!
   [D] has been called | 22:02:14
*)
let _ =
  let open Lwt in
  let c =
    delay_function ~name:"C" ~seconds:3.0 (fun () ->
      print_endline "Successfully downloaded avengers.mp4")
  in
  let b =
    delay_function ~name:"B" ~seconds:2.0 (fun () ->
      print_endline "Response from server: Error 404")
  in
  let a =
    delay_function ~name:"A" (fun () ->
      print_endline "Uploaded image family.jpg")
  in
  (* If I create the promise and store it in a variable, nothing stops it from
     starting right away so I have to defer its creation until it's needed. *)
  let d () =
    delay_function ~name:"D" (fun () ->
      print_endline "Processed results, goodbye!")
  in
  Lwt_main.run (join [ c; b; a ] >>= d)
;;

(* Lastly, there are other ways of handling this. What about threads? I could
   have used the [Thead] module with these functions: [Thread.create] and
   [Thread.join]; and [Thread.delay] to block each thread for N seconds. *)
