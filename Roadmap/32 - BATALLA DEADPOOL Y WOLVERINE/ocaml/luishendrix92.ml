open Printf
open Moure;;

Random.self_init ()

class fighter name' attack' evasion' =
  object (self)
    val mutable recharging = false
    val mutable hp = 1000
    val name : string = name'

    val attack : int * int =
      let min_attack, max_attack = attack' in
      let min_attack, max_attack =
        min min_attack max_attack, max min_attack max_attack
      in
      max 0 min_attack, min 9999 max_attack

    val evasion : int = Math.clamp ~a:0 ~b:100 evasion'
    method set_recharging recharging' = recharging <- recharging'
    method is_alive = hp > 0
    method get_name = name
    method set_hp hp' = hp <- Math.clamp ~a:0 ~b:9999 hp'
    method get_hp = hp

    method show =
      printf "%s | HP: %d" name hp;
      if recharging then printf " | Recharging!";
      print_newline ()

    method fight (enemy : fighter) =
      if recharging
      then begin
        self#set_recharging false;
        printf "%s is recharging...\n" name
      end
      else if Random.int 100 < 100 - evasion
      then begin
        let min_attack, max_attack = attack in
        let turn_attack = Random.int_in_range ~min:min_attack ~max:max_attack in
        enemy#set_hp (enemy#get_hp - turn_attack);
        printf "%s dealt %d damage to %s..." name turn_attack enemy#get_name;
        if turn_attack = max_attack
        then begin
          enemy#set_recharging true;
          print_string " CRITICAL HIT!!"
        end;
        print_newline ()
      end
      else printf "%s missed the attack!\n" name
  end

module Battle = struct
  let wolverine = new fighter "Wolverine" (10, 120) 20
  let deadpool = new fighter "Deadpool" (10, 100) 25
  let print_divider () = print_endline "---------------------------------"

  let show_winner () =
    let winner =
      if wolverine#get_hp <= 0 then deadpool#get_name else wolverine#get_name
    in
    printf "Battle is over. %s is the winner!\n" winner;
    print_endline "Final stats:";
    deadpool#show;
    wolverine#show
  ;;

  let start () =
    let rec loop turn =
      Unix.sleep 1;
      printf "Turn #%d:\n" turn;
      deadpool#show;
      wolverine#show;
      if turn mod 2 = 0
      then wolverine#fight deadpool
      else deadpool#fight wolverine;
      print_divider ();
      if wolverine#is_alive && deadpool#is_alive
      then loop (turn + 1)
      else show_winner ()
    in
    print_endline "Wolverine vs Deadpool! Who will win?";
    print_divider ();
    loop 1
  ;;
end
;;

Battle.start ()
