module Programmer = struct
  open Yojson.Safe
  open Xml

  type t =
    { name : string
    ; age : int
    ; birth_date : string
    ; languages : string list
    }
  [@@deriving yojson]

  type ts = t list [@@deriving yojson]

  class c name age birth_date languages =
    object
      val name : string = name
      val age : int = age
      val birth_date : string = birth_date
      val languages : string list = languages

      method introduce =
        Printf.printf
          "Hello, my name is %s and I'm a %d year old developer! My Favourite \
           languages are: %s.\n"
          name
          age
          (String.concat ", " languages)
    end

  let list_to_json l = ts_to_yojson l |> pretty_to_string

  let to_xml programmer =
    Element
      ( "programmer"
      , []
      , [ Element ("name", [], [ PCData programmer.name ])
        ; Element ("age", [], [ PCData (string_of_int programmer.age) ])
        ; Element ("birth_date", [], [ PCData programmer.birth_date ])
        ; Element
            ( "languages"
            , []
            , List.map
                (fun language ->
                  Xml.Element ("language", [], [ PCData language ]))
                programmer.languages )
        ] )
  ;;

  let list_to_xml l =
    let body = Element ("employees", [], List.map to_xml l) |> to_string_fmt in
    let xml_header = {|<?xml version="1.0" encoding="UTF-8"?>|} in
    xml_header ^ "\n" ^ body
  ;;

  let of_xml = function
    | Element
        ( "programmer"
        , []
        , [ Element ("name", [], [ PCData name ])
          ; Element ("age", [], [ PCData age ])
          ; Element ("birth_date", [], [ PCData birth_date ])
          ; Element ("languages", [], langs)
          ] ) ->
      let age = int_of_string age in
      let languages =
        List.map (fun lang -> children lang |> List.hd |> pcdata) langs
      in
      new c name age birth_date languages
    | _ -> failwith "Programmer Entity XML Malformed"
  ;;

  let list_of_json fname = from_file fname |> ts_of_yojson |> Result.get_ok

  let list_of_xml fname =
    match parse_file fname with
    | Element ("employees", [], programmers) -> List.map of_xml programmers
    | _ -> failwith "XML File Parsing Failed"
  ;;
end

let mock_data : Programmer.ts =
  [ { name = "Luis Lopez"
    ; age = 32
    ; birth_date = "09/04/1992"
    ; languages = [ "Typescript"; "Clojure"; "OCaml"; "Elixir" ]
    }
  ; { name = "John Doe"
    ; age = 24
    ; birth_date = "24/12/2000"
    ; languages = [ "C#"; "Java"; "Python"; "C++"; "Lua" ]
    }
  ; { name = "Jane Marsh"
    ; age = 50
    ; birth_date = "05/09/1976"
    ; languages = [ "Kotlin"; "Rust"; "Zig"; "SQL"; "Haskell" ]
    }
  ]
;;

let create_files () =
  let open Core.Out_channel in
  write_all "db.json" ~data:(Programmer.list_to_json mock_data);
  write_all "db.xml" ~data:(Programmer.list_to_xml mock_data)
;;

let delete_files () =
  Sys.remove "db.json";
  Sys.remove "db.xml"
;;

let () =
  let open Core.In_channel in
  create_files ();
  print_endline "Contents of the JSON File:";
  print_endline "--------------------------";
  read_all "db.json" |> print_endline;
  print_endline "Contents of the XML File:";
  print_endline "--------------------------";
  read_all "db.xml" |> print_endline;
  delete_files ()
;;

(*****************************************************************************)
(*                                                                           *)
(*                        Dificultad Extra (Opcional)                        *)
(*                                                                           *)
(*  Utilizando la lógica de creación de los archivos anteriores, crea un     *)
(*  programa capaz de leer y transformar en una misma clase custom de tu     *)
(*  lenguaje los datos almacenados en el XML y el JSON. Borra los archivos.  *)
(*                                                                           *)
(*****************************************************************************)

let () =
  create_files ();
  print_endline "Deserializing from JSON file...";
  Programmer.list_of_json "db.json"
  |> List.map (fun (p : Programmer.t) ->
    new Programmer.c p.name p.age p.birth_date p.languages)
  |> List.iter (fun programmer -> programmer#introduce);
  print_endline "Deserializing from XML file...";
  Programmer.list_of_xml "db.xml"
  |> List.iter (fun programmer -> programmer#introduce);
  delete_files ()
;;

(* Output of `dune exec reto12`

   Contents of the JSON File:
   --------------------------
   [
    {
      "name": "Luis Lopez",
      "age": 32,
      "birth_date": "09/04/1992",
      "languages": [ "Typescript", "Clojure", "OCaml", "Elixir" ]
    },
    {
      "name": "John Doe",
      "age": 24,
      "birth_date": "24/12/2000",
      "languages": [ "C#", "Java", "Python", "C++", "Lua" ]
    },
    {
      "name": "Jane Marsh",
      "age": 50,
      "birth_date": "05/09/1976",
      "languages": [ "Kotlin", "Rust", "Zig", "SQL", "Haskell" ]
    }
  ]
   Contents of the XML File:
   --------------------------
   <?xml version="1.0" encoding="UTF-8"?>
   <employees>
   <programmer>
   <name>Luis Lopez</name>
   <age>32</age>
   <birth_date>09/04/1992</birth_date>
   <languages>
   <language>Typescript</language>
   <language>Clojure</language>
   <language>OCaml</language>
   <language>Elixir</language>
   </languages>
   </programmer>
   <programmer>
   <name>John Doe</name>
   <age>24</age>
   <birth_date>24/12/2000</birth_date>
   <languages>
   <language>C#</language>
   <language>Java</language>
   <language>Python</language>
   <language>C++</language>
   <language>Lua</language>
   </languages>
   </programmer>
   <programmer>
   <name>Jane Marsh</name>
   <age>50</age>
   <birth_date>05/09/1976</birth_date>
   <languages>
   <language>Kotlin</language>
   <language>Rust</language>
   <language>Zig</language>
   <language>SQL</language>
   <language>Haskell</language>
   </languages>
   </programmer>
   </employees>
   Deserializing from JSON file...
   Hello, my name is Luis Lopez and I'm a 32 year old developer! My Favourite languages are: Typescript, Clojure, OCaml, Elixir.
   Hello, my name is John Doe and I'm a 24 year old developer! My Favourite languages are: C#, Java, Python, C++, Lua.
   Hello, my name is Jane Marsh and I'm a 50 year old developer! My Favourite languages are: Kotlin, Rust, Zig, SQL, Haskell.
   Deserializing from XML file...
   Hello, my name is Luis Lopez and I'm a 32 year old developer! My Favourite languages are: Typescript, Clojure, OCaml, Elixir.
   Hello, my name is John Doe and I'm a 24 year old developer! My Favourite languages are: C#, Java, Python, C++, Lua.
   Hello, my name is Jane Marsh and I'm a 50 year old developer! My Favourite languages are: Kotlin, Rust, Zig, SQL, Haskell.
*)
