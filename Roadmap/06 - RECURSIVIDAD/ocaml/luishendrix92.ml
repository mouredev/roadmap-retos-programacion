(**************************************************************************)
(*                                                                        *)
(*                                Recursion                               *)
(*                                                                        *)
(* I understand {b recursion} as a function that calls itself, or, that   *)
(* is defined in terms of itself. Its use cases are various:              *)
(*                                                                        *)
(* - {b Mathematics}: Factorial, fractals, fibonacci sequence.            *)
(* - {b Computer Science}:                                                *)
(*   - Dynamic programming algorithms that solve problems by breaking     *)
(*     them into smaller sub-problems (divide and conquer).               *)
(*   - Tree-like data structures and their algorithms.                    *)
(*   - Graph theory algorithms.                                           *)
(*   - Purely Functional programming, such as those algorithms that       *)
(*     operate on iterative data structures (lists, sets, maps, etc).     *)
(* - {b Arts}: Matrioshka dolls, infinity mirror, droste effect.          *)
(*                                                                        *)
(* Functional programming languages rely heavily on recursion due to      *)
(* procedural loops being (mostly) rejected in favour of it. Take for     *)
(* example a purely FP language like Haskell; there is NO way to write    *)
(* loops so in order to iterate you are forced to think in terms of       *)
(* recursion. OCaml is not a purely FP language and provides both loops   *)
(* and mutable references for cases in which performance is needed.       *)
(*                                                                        *)
(* In OCaml, in order to mark a function as recursive, we need to add the *)
(* [rec] keyword in front of [let], or pass an existing function to a     *)
(* {e fixing} function so that it works as intended. On top of that, the  *)
(* compiler guarantees that it will perform {b tail-call optimization}    *)
(* if it's possible. A tail-call optimized recursive function avoids      *)
(* creating multiple stack frames (leads to a {e stack overflow} if it's  *)
(* written in a way that the last call inside the function is the         *)
(* function itself with nothing in front or behind it, thus avoiding the  *)
(* need to backtrack. To achieve this, most programmers agree'd on a      *)
(* convention that involves an {e auxiliar} function defined inside or    *)
(* outside the main one, which in turn is called with some initial        *)
(* value for the accumulator and any dependency it might require. The     *)
(* main tradeoff is that some functions are incredibly complex to write   *)
(* with TCO in mind and may even require you to make use of stacks.       *)
(*                                                                        *)
(**************************************************************************)

module type Recursion = sig
  (** [print_range a b] prints lines with integer numbers from [a] to [b]. If no
      value is passed to [a], it will default to [0]. The order in which the
      printing happens depends on if [a > b] (descending order) or if [a <= b]
      (ascending order). This function is {b tail-call optimized}. *)
  val print_range : ?a:int -> int -> unit

  (** [factorial n] is the result of multiplying [n * n-1 * n-2 * ...] until
      [n] reaches 0 (base case that results in 1). The recursive mathematical
      definition of the {e factorial} is: {m n! = n \cdot (n - 1)!}. This
      function is {b not tail-call optimized}. *)
  val factorial : float -> float

  (** [factorial_tc n] is the {b tail-call optimized} version of {! factorial}.

      @raise Failure if [n < 0] (negative factorials are impossible). *)
  val factorial_tco : float -> float

  (** [fib n] is the nth integer in the fibonacci sequence
      ([0, 1, 1, 2, 3, 5, 8, 13, ...]). [n] represents the index in the
      aforementioned sequence, which is computed by adding the previous two
      numbers starting with [0] and [1]. It can be solved iteratively with
      a [for] loop but it's best represented as a recursive evaluation tree:

      {[
                   ⨍(5)
                /       \
            ⨍(4)    +    ⨍(3) = 5
           /    \      /       \
        ⨍(3) + ⨍(2) = 3   ⨍(2) + ⨍(1) = 2
            / \      / \
         ⨍(2) + ⨍(1) = 2 ⨍(1) + ⨍(0) = 1
            / \
         ⨍(1) + ⨍(0) = 1
      ]}

      Few things can be observed in this evaluation tree:

      + From a very small number ([5]), a lot of branches and individual calls
        to [fib] are created, making it exponentially inefficient. This is
        called a {b naive implementation} of a dynamic programming algorithm.
      + A lot of calls to [fib n] share the same input [n], making it possible
        to optimize using a technique called {b memoization}.

      It is possible to run the 2 branches [n-1] and [n-2] in parallel which
      reduces the execution time by a decent margin (depending on how many
      {e physical cores} the CPU has), though it does come with a cost.

      See https://v2.ocaml.org/releases/5.0/manual/parallelism.html. *)
  val fib : int -> int

  (** [fib_memo n] is the {b memoized} version of [fib n]. Memoization is a
      of optimizing dynamic programic algorithms and expensive functions by
      having a cache map (implemented as a key-value pair) that saves computed
      results to it and if the function receives the same input(s) again, the
      cached value can be retrieved thus saving tons of execution time.

      [fib_memo]'s cache is implemented with a [Hashtbl] (initial size [100]).

      @raise Failure if [n < 0]. [n] should be positive (or [0]). *)
  val fib_memo : int -> int

  (** [fib_tco n] is the {b tail-call optimized} version of [fib n].

      @raise Failure if [n < 0]. [n] should be positive (or [0]). *)
  val fib_tco : int -> int
end

module Exercise6 : Recursion = struct
  let rec print_range ?(a = 0) b =
    let delta = if a > b then -1 else 1 in
    print_endline (string_of_int a);
    if a <> b then print_range ~a:(a + delta) b
  ;;

  (* DIFICULTAD EXTRA (opcional):
     ----------------------------
     Utiliza el concepto de recursividad para:
     - Calcular el factorial de un número concreto (la función recibe ese número).
     - Calcular el valor de un elemento concreto (según su posición) en la
       sucesión de Fibonacci (la función recibe la posición).
  *)

  let rec factorial n = if n < 2. then 1. else n *. factorial (n -. 1.)

  let factorial_tco n =
    let rec aux ~acc n =
      if n < 0.
      then failwith "Negative factorial"
      else if n < 2.
      then acc
      else aux ~acc:(acc *. n) (n -. 1.)
    in
    aux ~acc:1. n
  ;;

  let rec fib n = if n < 2 then n else fib (n - 1) + fib (n - 2)

  let fib_memo =
    let cache = Hashtbl.create 100 in
    let rec aux n =
      if n < 0
      then failwith "Negative fibonacci sequence index"
      else if n < 2
      then n
      else begin
        match Hashtbl.find_opt cache n with
        | Some n -> n
        | None ->
          let result = aux (n - 1) + aux (n - 2) in
          Hashtbl.replace cache n result;
          result
      end
    in
    aux
  ;;

  let fib_tco n =
    let rec aux ~b ~a i = if i <= 0 then a else aux ~a:b ~b:(a + b) (i - 1) in
    if n < 0
    then failwith "Negative fibonacci sequence index"
    else aux ~a:0 ~b:1 n
  ;;
end
;;

begin
  let open Exercise6 in
  let open Printf in
  print_range ~a:100 0;
  printf "Factorial of 5: %f\n" (factorial 5.);
  printf
    "Tail-Call Optimized Factorial of -5: %s\n"
    (try factorial_tco (-5.) |> string_of_float with
     | Failure _ -> "ERROR");
  printf "Tail-Call Optimized Factorial of 50.0: %f\n" (factorial_tco 50.);
  (* Running [fib 37] is expensive so you will notice a slight delay*)
  printf "37th number in the fibonacci sequence (naive): %d\n" (fib 37);
  printf
    "100th number in the fibonacci sequence (memoized): %d\n"
    (fib_memo 100);
  printf "52nd number in the fibonacci sequence (tco): %d\n" (fib_tco 52)
end

(* Output of [ocaml luishendrix92.ml]:

   100
   99
   98
   97
   96
   95
   94
   93
   92
   91
   90
   89
   88
   87
   86
   85
   84
   83
   82
   81
   80
   79
   78
   77
   76
   75
   74
   73
   72
   71
   70
   69
   68
   67
   66
   65
   64
   63
   62
   61
   60
   59
   58
   57
   56
   55
   54
   53
   52
   51
   50
   49
   48
   47
   46
   45
   44
   43
   42
   41
   40
   39
   38
   37
   36
   35
   34
   33
   32
   31
   30
   29
   28
   27
   26
   25
   24
   23
   22
   21
   20
   19
   18
   17
   16
   15
   14
   13
   12
   11
   10
   9
   8
   7
   6
   5
   4
   3
   2
   1
   0
   Factorial of 5: 120.000000
   Tail-Call Optimized Factorial of -5: ERROR
   Tail-Call Optimized Factorial of 50.0: 30414093201713375576366966406747986832057064836514787179557289984.000000
   37th number in the fibonacci sequence (naive): 24157817
   100th number in the fibonacci sequence (memoized): 3736710778780434371
   52nd number in the fibonacci sequence (tco): 32951280099
*)
