open Printf

(******************************************************************************)
(*                                                                            *)
(*                      File Management - Filesystem IO                       *)
(*                                                                            *)
(*  IO operations are sometimes harder in functional programming languages    *)
(*  but that's not the case in OCaml. The standard library provides modules   *)
(*  such as [In_channel] and [Out_channel] to handle input and output; the    *)
(*  [Unix] module to interact with Unix APIs; [Sys] to communicate with the   *)
(*  operating system; and a utility module [Filename] to make working with    *)
(*  filenames a little less painful.                                          *)
(*                                                                            *)
(*  Built on top of them, libraries such as Lwt, Core, Fileutils, EIO, Riot   *)
(*  and others provide a better interface to work with the filesystem,        *)
(*  networking, terminal UIs, concurrency, port comms, and parallelism.       *)
(*                                                                            *)
(******************************************************************************)

let write_file_exercise filename =
  let lines =
    [ "Name: Luis Felipe Lopez G."
    ; "Age: 31 years."
    ; "Favourite P.L: Clojure."
    ]
  in
  (* Writing a file with the standard library is a very transparent process:
     1. Open the output channel corresponding to the file
     2. Print contents into it through functions such as [fprintf].
     3. Close the channel as good measure and practise. *)
  let oc = open_out filename in
  printf "Attempting to write %s...\n" filename;
  Fun.protect ~finally:(fun () ->
    (* Closing a channel is very important, this practise also applies for
       other resource cleanup situations such as open database connections,
       pending HTTP requests, threads and thread pools, and more. *)
    close_out oc;
    print_endline "Out channel closed.")
  @@ fun () ->
  List.iter (fun line -> fprintf oc "%s\n" line) lines;
  print_endline "Successful write!"
;;

let read_file_exercise filename =
  (* The first way to open a file with the standard library is to read from
     start [0] to finish [in_channel_length] dumping the file's bytes into a
     string with [really_input_string] (from the [In_channel] module). *)
  begin
    let ic = open_in filename in
    let contents = In_channel.really_input_string ic (in_channel_length ic) in
    close_in ic;
    match contents with
    | Some contents -> print_string contents
    | None -> printf "Reading %s failed!\n" filename
  end;
  (* The second way involves openning the input channel and reading bytes from
     it until the reading operation (often prefixed with [input_]) raises an
     [End_of_file] exception that needs to be handled to resume execution. *)
  begin
    let ic = open_in filename in
    try
      Fun.protect ~finally:(fun () ->
        close_in ic;
        print_endline "In channel closed.")
      @@ fun () ->
      while true do
        print_endline (input_line ic)
      done
    with
    | End_of_file -> print_endline "Reached end of file."
    | _ -> print_endline "Something went wrong reading the file!"
  end
;;

(* There are actually more ways to read and write to files. OCaml 5.1 gave
   us more convenience functions in the standard library to deal with file IO
   but as things stand today, the [Core] library still offers the better
   interface. I will use some of these functions in the next challenge! *)

let delete_file_exercise filename =
  Sys.remove filename;
  printf "%s was successfully removed!\n" filename
;;

(******************************************************************************)
(*                                                                            *)
(*                        Dificultad Extra (Opcional)                         *)
(*                                                                            *)
(*  Desarrolla un programa de gestión de ventas que alamacena sus datos en    *)
(*  un archivo [.txt].                                                        *)
(*                                                                            *)
(*  - Cada producto se gaurda en una línea del archivo de la siguiente        *)
(*    manera: [nombre_producto, cantidad_vendida, precio].                    *)
(*  - Siguiendo ese formato, y mediante la terminal, debe permitir añadir,    *)
(*    consultar, actualizar, eliminar productos y salir del programa.         *)
(*  - También debe poseer opciones para calcular la venta total y por prod.   *)
(*  - La opción [salir] borra el archivo [.txt].                              *)
(*                                                                            *)
(******************************************************************************)

module StoreDb = struct
  open Core

  type sale =
    { product_name : string
    ; qty_sold : int
    ; unit_price : float
    }
  [@@deriving show]

  let filename = "sales.csv"

  let deserialize line =
    let row = Stdlib.String.trim line in
    match String.split ~on:',' (Stdlib.String.trim row) with
    | product_name :: qty_sold :: unit_price :: _ ->
      let qty_sold = Int.of_string qty_sold in
      let unit_price = Float.of_string unit_price in
      { product_name; qty_sold; unit_price }
    | _ -> failwith "Database row deserialization error."
  ;;

  let serialize { product_name; qty_sold; unit_price } =
    sprintf "%s,%d,%f" product_name qty_sold unit_price
  ;;

  let create () =
    let oc = Out_channel.create ~append:true filename in
    Out_channel.close_no_err oc
  ;;

  let insert sale =
    let oc = Out_channel.create ~append:true filename in
    protect
      ~finally:(fun () -> Out_channel.close_no_err oc)
      ~f:(fun () -> fprintf oc "%s\n" (serialize sale))
  ;;

  let get_all () =
    let lines = In_channel.read_lines filename in
    List.map ~f:deserialize lines
  ;;

  let get_by_name name =
    List.find ~f:(fun sale -> equal_string name sale.product_name) @@ get_all ()
  ;;

  let delete_by_name name =
    get_all ()
    |> List.filter ~f:(fun sale -> Stdlib.( <> ) name sale.product_name)
    |> List.map ~f:serialize
    |> Out_channel.write_lines filename
  ;;

  let update_by_name ~f name =
    let sales = get_all () in
    let target =
      List.find ~f:(fun sale -> equal_string name sale.product_name) sales
    in
    match target with
    | Some target ->
      List.filter
        ~f:(fun sale -> Stdlib.( <> ) target.product_name sale.product_name)
        sales
      |> List.cons (f target)
      |> List.map ~f:serialize
      |> Out_channel.write_lines filename
    | None -> failwith @@ sprintf "There is no product %s to update!" name
  ;;

  let destroy () = Stdlib.Sys.remove filename
end

(* NOTE: 12/03/2024 - I'm writing a terminal user interface library or at the
   very least, a set of helper functions to make writing TUIs an easier and
   beautiful experience rather than a repetitive hell. Instead, for now I'm
   using a set of mock sales to tell a story with print statements. Once the
   library is ready I will rewrite this and send a pull request. *)
let extra () =
  let open StoreDb in
  let print_all () =
    List.iter (fun sale -> print_endline (show_sale sale)) @@ get_all ()
  in
  let mock_sales : sale list =
    [ { product_name = "Macbook Pro M2 14\" 1TB"
      ; qty_sold = 3
      ; unit_price = 44_999.00
      }
    ; { product_name = "Macbook air m3 15\" 256gb"
      ; qty_sold = 2
      ; unit_price = 27_999.00
      }
    ; { product_name = "iMac (Blue) M3 512GB"
      ; qty_sold = 5
      ; unit_price = 39_999.00
      }
    ; { product_name = "Mac Mini M2 256GB"
      ; qty_sold = 5
      ; unit_price = 13_499.00
      }
    ; { product_name = "Mac Studio M2 Ultra"
      ; qty_sold = 1
      ; unit_price = 92_999.00
      }
    ; { product_name = "Mac Pro M2 Ultra 1TB"
      ; qty_sold = 3
      ; unit_price = 149_999.00
      }
    ]
  in
  create ();
  print_endline "Apple Store Mexico opened, they have some initial stock:";
  List.iter insert mock_sales;
  print_all ();
  print_endline
    "On black friday, the Macbook Pro sells like crazy, 10 more units!";
  update_by_name "Macbook Pro M2 14\" 1TB" ~f:(fun product ->
    { product with qty_sold = product.qty_sold + 10 });
  print_endline
    "The manager decided that the Mac Pro never existed, so he deletes it...";
  delete_by_name "Mac Pro M2 Ultra 1TB";
  print_endline "A new product arrives: the M3 mac mini with 512GB of RAM.";
  insert
    { product_name = "Mac Mini M3 512GB"; qty_sold = 0; unit_price = 29_999.00 };
  print_endline "This is what the report looks like before closing:";
  print_all ();
  let products = get_all () in
  let total_sales =
    List.fold_left
      (fun total { unit_price; qty_sold; _ } ->
        total +. (float_of_int qty_sold *. unit_price))
      0.00
      products
  in
  List.iter
    (fun sale ->
      printf
        "%s | Total sales: $%.2f MXN\n"
        sale.product_name
        (float_of_int sale.qty_sold *. sale.unit_price))
    products;
  printf "Total sale for all products: $%.2f MXN.\n" total_sales;
  destroy ();
  print_endline "The store has closed and the sales report deleted."
;;

let _ =
  let filename = "luishendrix92.txt" in
  write_file_exercise filename;
  print_newline ();
  read_file_exercise filename;
  print_newline ();
  (* If I were to try read the deleted file, an exception would be raised
     by the [read_in] function which was not properly handled.

     {[
       read_file_exercise filename
       #> Fatal error: exception Sys_error
       #> ("luishendrix92.txt: No such file or directory")
     ]}
  *)
  delete_file_exercise filename;
  print_newline ();
  extra ()
;;

(* Output of running [dune exec reto11]

   Attempting to write luishendrix92.txt...
   Successful write!
   Out channel closed.

   Name: Luis Felipe Lopez G.
   Age: 31 years.
   Favourite P.L: Clojure.
   Name: Luis Felipe Lopez G.
   Age: 31 years.
   Favourite P.L: Clojure.
   In channel closed.
   Reached end of file.

   luishendrix92.txt was successfully removed!

   Apple Store Mexico opened, they have some initial stock:
   { Reto11.StoreDb.product_name = "Macbook Pro M2 14\" 1TB"; qty_sold = 3;
     unit_price = 44999. }
   { Reto11.StoreDb.product_name = "Macbook air m3 15\" 256gb"; qty_sold = 2;
     unit_price = 27999. }
   { Reto11.StoreDb.product_name = "iMac (Blue) M3 512GB"; qty_sold = 5;
     unit_price = 39999. }
   { Reto11.StoreDb.product_name = "Mac Mini M2 256GB"; qty_sold = 5;
     unit_price = 13499. }
   { Reto11.StoreDb.product_name = "Mac Studio M2 Ultra"; qty_sold = 1;
     unit_price = 92999. }
   { Reto11.StoreDb.product_name = "Mac Pro M2 Ultra 1TB"; qty_sold = 3;
     unit_price = 149999. }
   On black friday, the Macbook Pro sells like crazy, 10 more units!
   The manager decided that the Mac Pro never existed, so he deletes it...
   A new product arrives: the M3 mac mini with 512GB of RAM.
   This is what the report looks like before closing:
   { Reto11.StoreDb.product_name = "Macbook Pro M2 14\" 1TB"; qty_sold = 13;
     unit_price = 44999. }
   { Reto11.StoreDb.product_name = "Macbook air m3 15\" 256gb"; qty_sold = 2;
     unit_price = 27999. }
   { Reto11.StoreDb.product_name = "iMac (Blue) M3 512GB"; qty_sold = 5;
     unit_price = 39999. }
   { Reto11.StoreDb.product_name = "Mac Mini M2 256GB"; qty_sold = 5;
     unit_price = 13499. }
   { Reto11.StoreDb.product_name = "Mac Studio M2 Ultra"; qty_sold = 1;
     unit_price = 92999. }
   { Reto11.StoreDb.product_name = "Mac Mini M3 512GB"; qty_sold = 0;
     unit_price = 29999. }
   Macbook Pro M2 14" 1TB | Total sales: $584987.00 MXN
   Macbook air m3 15" 256gb | Total sales: $55998.00 MXN
   iMac (Blue) M3 512GB | Total sales: $199995.00 MXN
   Mac Mini M2 256GB | Total sales: $67495.00 MXN
   Mac Studio M2 Ultra | Total sales: $92999.00 MXN
   Mac Mini M3 512GB | Total sales: $0.00 MXN
   Total sale for all products: $1001474.00 MXN.
   The store has closed and the sales report deleted. *)
