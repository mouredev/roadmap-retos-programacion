open Printf

(******************************************************************************)
(*                                                                            *)
(*                       Dependency Inversion Principle                       *)
(*                                                                            *)
(*  DIP is the strategy of depending upon interfaes or abstract functions     *)
(*  and classes rather than upon concrete functions and classes. A good rule  *)
(*  to apply is that higher-level components should not depend on a lower     *)
(*  level component, and they should also work in isolation. DIP tells us     *)
(*  that every dependency in the design should target an interface or an      *)
(*  abstract class. Furthermore, a dependency should not target a concrete    *)
(*  class. It's also worth noting that {e Dependency Injection} is just a     *)
(*  vehicle to achieve the inversion of control.                              *)
(*                                                                            *)
(******************************************************************************)

module LowLevelModule = struct
  let do_something () = print_endline "LLM Doing something..."
end

module HighLevelModule = struct
  (** [LowLevelSubModule] is tightly coupled with the high-level module.
      This breaks the DIP and should be abstracted with a functor instead. *)
  module LowLevelSubModule = LowLevelModule

  let say_hello () =
    print_endline "Hello from HLM, submodule does something:";
    LowLevelModule.do_something ()
  ;;
end

let _ = HighLevelModule.say_hello ()

module type AbstractModule = sig
  val do_something : unit -> unit
end

module ConcreteModule : AbstractModule = struct
  let do_something () = print_endline "ConcreteModule does something..."
end

module DIP_HLM_Functor (AM : AbstractModule) : sig
  val say_hello : unit -> unit
end = struct
  (** [ASM] is an injected dependency module that implements the
      [AbstractModule] pseudointerface.*)
  module ASM = AM

  let say_hello () =
    print_endline "Hello from a DIP-complied HLM!";
    print_endline "The abstract submodule does something:";
    ASM.do_something ()
  ;;
end

module DIP_Compliant = DIP_HLM_Functor (ConcreteModule)

let _ =
  print_newline ();
  (* Sealing [DIP_Compliant] with a module signature allows us to make the
     abstract submodule (dependency) private, just like in OOP. *)
  DIP_Compliant.say_hello ()
;;

(* Here's how it's done with classes in OCaml. *)

class type abstraction = object
  method operation : unit
end

class low_level_class : abstraction =
  object
    method operation = print_endline "Low-level class operation/method"
  end

class high_level_class (dependency' : abstraction) =
  object
    val dependency = dependency'

    method use_dependency =
      print_endline "High level class uses its injected dependency:";
      dependency#operation
  end

let _ =
  let hlo = new high_level_class (new low_level_class) in
  print_newline ();
  hlo#use_dependency
;;

(*
   DIFICULTAD EXTRA (opcional):
   Crea un sistema de notificaciones.
   Requisitos:
   1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
   2. El sistema de notificaciones no puede depender de las implementaciones específicas.
   Instrucciones:
   1. Crea la interfaz o clase abstracta.
   2. Desarrolla las implementaciones específicas.
   3. Crea el sistema de notificaciones usando el DIP.
   3. Desarrolla un código que compruebe que se cumple el principio.
*)

module type Notifier = sig
  val id : string
  val notify : string -> string -> unit
end

module EmailService : Notifier = struct
  let address = "luishendrix92@gmail.com"
  let id = "EMAILER"

  let notify msg destination =
    print_endline "Email sent:\n--------------------------";
    printf "From: %s\n" address;
    printf "To: %s\n" destination;
    print_endline msg
  ;;
end

module NotificationManager (N : Notifier) : sig
  val create_and_send : string -> string -> unit
end = struct
  module NotificationService = N

  let create_and_send msg destination =
    printf
      "Sending [%s] to [%s] via %s...\n"
      msg
      destination
      NotificationService.id;
    NotificationService.notify msg destination
  ;;
end

(* We can inject an existing module that satisfies the interface: *)
module EmailNotificationManager = NotificationManager (EmailService)

(* OR... we can  also inject anonymous modules in-line: *)
module SMSNotificationManager = NotificationManager (struct
    let id = "TelcelSMS"
    let phone_number = "664-563-7778"

    let notify msg destination =
      print_endline "SMS sent:\n--------------------------";
      printf "To: [[ %s ]]\n" destination;
      printf "Text message: %s\n" msg;
      printf "From: [[ %s ]]\n" phone_number
    ;;
  end)

module UbuntuNotificationCenter = NotificationManager (struct
    let id = "UbuntuNotifications"

    let notify msg destination =
      printf "Application: %s\n" destination;
      print_endline msg
    ;;
  end)

let _ =
  print_newline ();
  EmailNotificationManager.create_and_send
    "Hello, how are you? Let's meet soon"
    "friend@hotmail.com";
  print_newline ();
  SMSNotificationManager.create_and_send "Did you buy milk?" "664-121-4442";
  print_newline ();
  UbuntuNotificationCenter.create_and_send
    "Currently playing: Los Lobos - La Bamba"
    "Spotify"
;;
