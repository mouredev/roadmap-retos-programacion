(******************************************************************************)
(*                                                                            *)
(*                      Interface Segregation Principle                       *)
(*                                                                            *)
(*  The core concept of this principle (the 'I' in {b SOLID}) is, a class     *)
(*  should not be forced to implement methods that it doesn't need, caused    *)
(*  by the implementation of a broad interface, or inheriting from a general  *)
(*  abstract class that covers more ground than it should.                    *)
(*                                                                            *)
(*  The proposed solution is to create smaller interfaces that are only im-   *)
(*  plemented if the class needs those methods and/or members and only        *)
(*  inherit from a base class that won't force unwanted implementations. It   *)
(*  goes hand in hand with the Liskov-Substitution Principle as it helps      *)
(*  reduce the amount of exceptions thrown.                                   *)
(*                                                                            *)
(******************************************************************************)

open Printf

(* This interface violates the ISP because if implemented by a specific type of
   coffee machine, it will be forced to implement methods that it doesn't need
   and thus it'll need to either throw an exception or provide a NoOP body. *)
class type coffee_machine_violating_isp = object
  method drip_brew : unit
  method replace_filter : unit
  method steam_milk : unit
  method pressure_brew : unit
  method add_ground_coffee : unit
end

class type coffee_machine = object
  method brew : unit
  method add_ground_coffee : unit
end

class type drip = object
  (* Inheriting a class type from another class type in OCaml is the same
     as extending an interface in OOP languages. Though we can't implement
     multiple interfaces, we can in fact inherit from multiple classes! *)
  inherit coffee_machine
  method drip_brew : unit
  method replace_filter : unit
end

class type espresso = object
  inherit coffee_machine
  method steam_milk : unit
  method pressure_brew : unit
end

class drip_machine : drip =
  object (self)
    method private drip_brew = print_endline "Brewing through a paper filter..."

    method add_ground_coffee =
      print_endline "Adding ground coffee to drip coffee machine..."

    method replace_filter = print_endline "Replacing paper filter..."
    method brew = self#drip_brew
  end

class espresso_machine : espresso =
  object (self)
    method private pressure_brew =
      print_endline "Brewing through an espresso portafilter..."

    method add_ground_coffee =
      print_endline
        "Adding and compressing ground coffee to espresso machine..."

    method steam_milk = print_endline "Steaming milk for latte art..."
    method brew = self#pressure_brew
  end

let _ =
  let oster_drip : drip_machine = new drip_machine in
  let barista : espresso_machine = new espresso_machine in
  oster_drip#add_ground_coffee;
  oster_drip#brew;
  oster_drip#replace_filter;
  barista#add_ground_coffee;
  barista#brew;
  barista#steam_milk
;;

(******************************************************************************)
(*                                                                            *)
(*                        Dificultad Extra (Opcional)                         *)
(*                                                                            *)
(*  Crea un gestor de impresoras.                                             *)
(*  Requisitos:                                                               *)
(*  1. Algunas impresoras solo imprimen en blanco y negro.                    *)
(*  2. Otras solo a color.                                                    *)
(*  3. Otras son multifunción, pueden imprimir, escanear y enviar fax.        *)
(*  Instrucciones:                                                            *)
(*  1. Implementan el sistema, con los diferentes tipos de impresoras y fun-  *)
(*     ciones.                                                                *)
(*  2. Aplica el ISP a la implementación.                                     *)
(*  3. Desarrolla un código que compruebe que se cumple el principio.         *)
(*                                                                            *)
(******************************************************************************)

class virtual black_white_printing =
  object
    method virtual print_b_and_w : string -> unit
  end

class virtual color_printing =
  object
    method virtual print_color : string -> unit
  end

class virtual fax (number : string) =
  object
    val phone_number = number
    method virtual send_document : string -> string -> unit
  end

class virtual scanner =
  object
    method virtual scan_document : string -> unit
  end

class bw_printer =
  object
    inherit black_white_printing

    method print_b_and_w docfile =
      printf "Printing [%s] in black and white...\n" docfile
  end

class color_printer =
  object
    inherit color_printing

    method print_color docfile =
      printf "Printing [%s] in CYMK color...\n" docfile
  end

class multifunctional_printer (number : string) =
  object (self)
    (* As I mentioned before, OCaml's class system offers multiple inheritance
       but I could have also made them interfaces (class types) and in order to
       create an interface that 'implements' all of them we could have done:

       {[
         class multifunctional_printer (number : string) : object
           inherit color_printing
           inherit black_white_printing
           inherit scanner
           inherit fax
         end = object (self) end
       ]}

       This way we'd be forced to implement all of those methods but with one
       catch: using class types 'seals' a class, meaning we can't expose more
       public methods other than the ones in the interface.
    *)
    inherit color_printing
    inherit black_white_printing
    inherit scanner
    inherit fax number

    method scan_document docfile =
      printf "Scanning [%s] with a multifunctional\n" docfile

    method send_document docfile destination_number =
      printf
        "Sending [%s] from #%s to fax #%s through a multifunctional\n"
        docfile
        phone_number
        destination_number

    method private print_b_and_w docfile =
      printf
        "Printing [%s] in black and white using a multifunctional\n"
        docfile

    method private print_color docfile =
      printf "Printing [%s] in CYMK color using a multifunctional\n" docfile

    method print ?(use_color = true) docfile =
      if use_color then self#print_color docfile else self#print_b_and_w docfile
  end

let _ =
  let compaq_bw = new bw_printer in
  let epson_color = new color_printer in
  let epson_mf = new multifunctional_printer "664-934-1295" in
  compaq_bw#print_b_and_w "2024report.xlsx";
  epson_color#print_color "wedding_album.pdf";
  epson_mf#print ~use_color:false "essat.docx";
  epson_mf#send_document "private_letter.txt" "55-676-2424";
  epson_mf#scan_document "ocr_test.jpg"
;;
