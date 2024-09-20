open Printf

(******************************************************************************)
(*                                                                            *)
(*                       Liskov Substitution Principle                        *)
(*                                                                            *)
(*  The LSP states that subclasses of a parent class should be able to beha-  *)
(*  ve just like their parent classes. Or the official statement: let phi(x)  *)
(*  be a property provable about objects of type T, then phi(y) should be     *)
(*  true for objects y ofthe type S where S is a subtype of T.                *)
(*  All of this means that we should be able to replace objects of a super-   *)
(*  class with objects of its subclasses without breaking the client's code.  *)
(*                                                                            *)
(*  It also states some rules:                                                *)
(*  1. A subclasss method should not strengthen its pre-condition: In human-  *)
(*     readable terms: overriden methods should not change their parameters   *)
(*     for subtypes of those parameter types.                                 *)
(*  2. A subclass method should not weaken its post-condition: We should not  *)
(*     return a more abstract type than the specified return type, but we     *)
(*     can definitely return a subtype of the return type.                    *)
(*  3. Methods should not break the invariance of the superclass' method.     *)
(*                                                                            *)
(******************************************************************************)

class virtual lsp_non_compliant_acount (owner' : string) =
  object
    val mutable balance = 0.0
    val owner = owner'
    method virtual deposit : float -> unit
    method virtual withdraw : float -> unit
    method show_balance = printf "Current balance for %s: $%f\n" owner balance
  end

class savings_account (owner' : string) =
  object
    inherit lsp_non_compliant_acount owner'

    method deposit amount =
      balance <- balance +. amount;
      printf "%s deposited %f into their account!\n" owner amount

    method withdraw amount =
      if balance < amount
      then failwith "Not enough funds for withdrawal"
      else begin
        balance <- balance -. amount;
        printf "%s withdrew %f from their account!\n" owner amount
      end
  end

class fixed_term_account (owner' : string) =
  object
    inherit lsp_non_compliant_acount owner'

    method deposit amount =
      balance <- balance +. amount;
      printf "%s deposited %f into a fixed term!\n" owner amount

    method withdraw = failwith "Unsupported method"
  end

let _ =
  (* Client Code for an LSP-breaking example *)
  let acct : lsp_non_compliant_acount ref =
    ref @@ new savings_account "Luis Lopez"
  in
  !acct#deposit 456.53;
  !acct#withdraw 245.35;
  !acct#show_balance;
  (* The code above worked great, but what if I were to swap the account ref
     value for a subclass that doen't do withdrawals and instead throws an
     exception which completely breaks the LSP. *)
  acct := new fixed_term_account "Moure Dev";
  !acct#deposit 456.53;
  begin
    try !acct#withdraw 245.35 with
    | Failure msg -> print_endline msg
  end;
  !acct#show_balance
;;

(* Let's try to make the example LSP compliant. The most feasible solution is
   to stop making assumptions about the withdrawal capabilities of these accts.
   Next step is to break a superclass [Account] (or interface) into their own
   subclasses or subinterfaces with extended capabilities that other concrete
   classes can inherit or extend in turn. This way if the client code requires
   accounts that have withdrawal capabilities, then we can start using our
   specialized subtype that performs a withdrawal operation. *)

class virtual account (owner' : string) =
  object
    val mutable balance = 0.0
    val owner = owner'
    method virtual deposit : float -> unit
    method show_balance = printf "Current balance for %s: $%f\n" owner balance
  end

class virtual withdrawable owner' =
  object
    inherit account owner'
    method virtual withdraw : float -> unit
  end

class fixed_term owner' =
  object
    inherit account owner'

    (* Any other methods or members corresponding to a specialized fixed-term
       class go here, otherwise there  would be no point in extending.*)
    method deposit amount =
      balance <- balance +. amount;
      printf "%s deposited %f into their fixed term!\n" owner amount
  end

class savings owner' =
  object
    inherit withdrawable owner'

    method deposit amount =
      balance <- balance +. amount;
      printf "%s deposited %f into their savings account!\n" owner amount

    method withdraw amount =
      if balance < amount
      then failwith "Not enough funds for withdrawal"
      else begin
        balance <- balance -. amount;
        printf "%s withdrew %f from their savings account!\n" owner amount
      end
  end

let _ =
  (* Client Code for an LSP-compliant example *)
  let acct : withdrawable = new savings_account "Luis Lopez" in
  acct#deposit 319.35;
  acct#withdraw 300.00;
  acct#show_balance
;;

(* Now, the client code is specific in that it only accepts subclasses that
   are 'withdrawable' and if I were to pass it an instance of [fixed_term]
   then the compiler would let us know, thus not breaking the LSP.

   The compiler error says:
   - This expression has type fixed_term but an expression was expdected of
     type withdrawable The first object type has no method withdraw. *)
(* let acct2 : withdrawable = new fixed_term "John Doe" in *)
(* acct#withdraw 100.0 *)

(* 
 * DIFICULTAD EXTRA (opcional):
 * ============================
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 *)

let clamp a b x = if x < a then a else if x > b then b else x

class virtual vehicle (top_speed' : float) (accel : float) =
  object
    val top_speed = top_speed'
    val acceleration = accel
    val mutable speed = 0.0

    method accelerate' =
      let clamp_speed = clamp 0.0 top_speed in
      speed <- clamp_speed (speed +. acceleration)

    method virtual accelerate : unit
    method get_speed = speed
    method brake = speed <- 0.0
  end

class boat =
  object (self)
    inherit vehicle 80.0 1.52
    method anchor = print_endline "Anchoring boat..."

    method accelerate =
      self#accelerate';
      print_endline "Boat accelerated"
  end

class motorbike =
  object (self)
    inherit vehicle 186.0 25.4

    method accelerate =
      self#accelerate';
      print_endline "Motorbike accelerated"
  end

class tesla =
  object (self)
    inherit vehicle 200.0 9.82
    val mutable charge = 0

    method accelerate =
      self#accelerate';
      charge <- clamp 0 100 (charge - 1);
      print_endline "Tesla accelerated"

    method recharge = charge <- 100
  end

let _ =
  let v : vehicle = new motorbike in
  print_newline ();
  for i = 1 to 10 do
    v#accelerate;
    printf "Motorbike's speed: %f\n" v#get_speed
  done;
  v#brake;
  print_endline "Invoking #brake on a motorbike";
  printf "Motorbike's speed: %f\n" v#get_speed
;;
