open Printf

(**************************************************************************)
(*                                                                        *)
(*                           Class Inheritance                            *)
(*                                                                        *)
(*  Inheritance is possible in OCaml, however, it's failry limited and    *)
(*  you need to use the explicit subtype to parent type coercion          *)
(*  operator [:>] to, for example, keep a list of subtypes of the same    *)
(*  parent type. The only caveat is that once you coerce an object's      *)
(*  type, you will not be able to call specialized subtype methods.       *)
(*                                                                        *)
(*  The way inheritance works in OCaml is throug the [inherit] keyword    *)
(*  right at the start of an object definition; this keyword behaves      *)
(*  the same way as the [super] constructor in langauges like Java/C#.    *)
(*    You can also define a class as virtual (and some or all methods)    *)
(*  so that the programmer can't instantiate it but can extend it and     *)
(*  use or override the default implementation of its virtual methods.    *)
(*  The language also features class types as pseudo-interfaces and       *)
(*  member/method restrictors, but that's a topic for another time :) !   *)
(*                                                                        *)
(**************************************************************************)

class virtual animal name age breed =
  object
    val mutable name : string = name
    val mutable age : int = age
    val breed : string = breed
    method get_name = name
    method set_name name' = name <- name'
    method get_age = age
    method set_age age' = age <- age'
    method get_breed = breed
    method virtual make_sound : unit
  end

class dog name age breed =
  object (self)
    inherit animal name age breed

    method make_sound =
      printf
        "%s the %d year old %s dog says: WOOF WOOF!!\n"
        self#get_name
        self#get_age
        self#get_breed
  end

class cat name age breed =
  object (self)
    inherit animal name age breed

    method make_sound =
      printf
        "%s the %d year old %s cat says: MEOW MEOW...\n"
        self#get_name
        self#get_age
        self#get_breed
  end

let () =
  (* These 2 animals don't require type coercion because none of these subtypes
     implement methods that aren't defined in the parent type. Virtual methods
     defined in the parent type can be either left unimplemented and ready for
     any subtype to implement them by themselves; or, they can be defined and
     let the subtype choose to overwrite or use the default implementation. *)
  let firulais : animal = new dog "Firulais" 3 "Dachshund" in
  let bigotes : animal = new cat "Bigotes" 12 "Russian Blue" in
  firulais#make_sound;
  bigotes#make_sound;
  print_newline ()
;;

(**************************************************************************)
(*                                                                        *)
(*                      Dificultad Extra (Opcional)                       *)
(*                                                                        *)
(*  Implementa la jerarquía de una empresa de desarrollo formada por      *)
(*  empleados que pueden ser gerentes, gerentes de proyectos o            *)
(*  programadores. Cada empleado tiene un identificador y un nombre.      *)
(*  Dependiendo de su labor, tienen propiedades y funciones exclusivas    *)
(*  de su actividad, y almacenan los empleados a su cargo.                *)
(*                                                                        *)
(**************************************************************************)

let curr_id : int ref = ref 0

class virtual employee name skills =
  let generated_id =
    incr curr_id;
    !curr_id
  in
  object
    val id : int = generated_id
    val name : string = name
    val mutable skills : string list = skills
    method get_id = id
    method get_name = name
    method get_skills = skills
    method set_skills skills' = skills <- skills'
    method virtual to_string : string
  end

type proj =
  { name : string
  ; requirements : string list
  }

class programmer name languages =
  object (self : 'a)
    inherit employee name languages
    method get_languages = self#get_skills

    method learn_language language =
      self#set_skills (language :: self#get_skills)

    method to_string =
      sprintf
        "[Programmer #%d | Name: %s | Tech stack: %s]"
        self#get_id
        self#get_name
        (String.concat ", " self#get_skills)
  end

class project_manager name skills project =
  let open Core.Option in
  object (self : 'a)
    inherit employee name skills
    val mutable project : proj option = project
    val mutable team : employee list = []
    method get_project = project

    method private get_project_name =
      match project with
      | Some project -> sprintf "project '%s'" project.name
      | None -> "no project"

    method assign_project project' =
      project <- project';
      printf
        "%s has been assigned %s to manage!\n"
        self#get_name
        self#get_project_name

    method select_team (candidates : employee list) =
      team
      <- Core.List.filter
           ~f:(fun candidate ->
             let requirements =
               Option.fold ~none:[] ~some:(fun p -> p.requirements) project
             in
             Core.List.exists
               ~f:(fun skill ->
                 Core.List.exists ~f:(fun req -> req = skill) requirements)
               candidate#get_skills)
           candidates;
      printf
        "%s were selected to work for PM %s on %s!\n"
        (List.map (fun e -> e#get_name) team |> String.concat ", ")
        self#get_name
        self#get_project_name

    method to_string =
      sprintf
        "[PM #%d | Name: %s | Managing: %s | Skills: %s]"
        self#get_id
        self#get_name
        self#get_project_name
        (String.concat ", " self#get_skills)
  end

let () =
  let e1 =
    new programmer "Luis" [ "spring boot"; "github"; "ocaml"; "circleci" ]
  in
  let e2 = new programmer "Karla" [ "python"; "figma"; ".net"; "mongodb" ] in
  let e3 = new programmer "Doug" [ "flutter"; "github"; "aws"; "azure" ] in
  let e4 = new programmer "Smith" [ "react"; "javascript"; "c#"; "angular" ] in
  let e5 = new programmer "Marina" [ "haskell"; "python" ] in
  let pm1 =
    new project_manager "Moure" [ "scrum"; "architecture design" ] None
  in
  let pm2 =
    new project_manager "Julia" [ "scrum"; "devops"; "mobile development" ] None
  in
  print_endline "Corporation roster:";
  print_endline "-------------------";
  print_endline e1#to_string;
  print_endline e2#to_string;
  print_endline e3#to_string;
  print_endline e4#to_string;
  print_endline e5#to_string;
  print_endline pm1#to_string;
  print_endline pm2#to_string;
  print_endline "-------------------";
  pm1#assign_project
  @@ Some
       { name = "MoureApp"
       ; requirements = [ "flutter"; "aws"; "github"; "spring boot" ]
       };
  pm2#assign_project
  @@ Some
       { name = "AirBnB"
       ; requirements = [ "react"; "mongodb"; ".net"; "rabbitmq" ]
       };
  (* Type coercion from subtype to parent type is needed because the code that
     is consuming them (select_team) needs a list of any employee subtype (not
     just programmers) and it will not use any specialized method. *)
  let candidates : employee list =
    [ (e1 : programmer :> employee)
    ; (e2 : programmer :> employee)
    ; (e3 : programmer :> employee)
    ; (e4 : programmer :> employee)
    ; (e5 : programmer :> employee)
    ]
  in
  pm1#select_team candidates;
  pm2#select_team candidates;
  print_endline "-------------------";
  print_endline "Marina's current skills didn't fit any existing project but...";
  print_endline
    "a new project is coming and she learns 2 of its 3 requirements.";
  pm1#assign_project
  @@ Some
       { name = "WhatIsThis 2.0"
       ; requirements = [ "machine learning"; "pytorch"; "scikitlearn" ]
       };
  e5#learn_language "machine learning";
  e5#learn_language "pytorch";
  pm1#select_team candidates
;;

(* Output of running [dune exec reto9]
   ===================================
   Firulais the 3 year old Dachshund dog says: WOOF WOOF!!
   Bigotes the 12 year old Russian Blue cat says: MEOW MEOW...

   Corporation roster:
   -------------------
   [Programmer #1 | Name: Luis | Tech stack: spring boot, github, ocaml, circleci]
   [Programmer #2 | Name: Karla | Tech stack: python, figma, .net, mongodb]
   [Programmer #3 | Name: Doug | Tech stack: flutter, github, aws, azure]
   [Programmer #4 | Name: Smith | Tech stack: react, javascript, c#, angular]
   [Programmer #5 | Name: Marina | Tech stack: haskell, python]
   [PM #6 | Name: Moure | Managing: no project | Skills: scrum, architecture design]
   [PM #7 | Name: Julia | Managing: no project | Skills: scrum, devops, mobile development]
   -------------------
   Moure has been assigned project 'MoureApp' to manage!
   Julia has been assigned project 'AirBnB' to manage!
   Luis, Doug were selected to work for PM Moure on project 'MoureApp'!
   Karla, Smith were selected to work for PM Julia on project 'AirBnB'!
   -------------------
   Marina's current skills didn't fit any existing project but...
   a new project is coming and she learns 2 of its 3 requirements.
   Moure has been assigned project 'WhatIsThis 2.0' to manage!
   Marina were selected to work for PM Moure on project 'WhatIsThis 2.0'!
*)
