#lang racket

; Operators
; ---------
; Racket's operators are functions that can be passed around (and returned).
; On top of that, all functions are prefix, meaning we can't evaluate certain
; expressions as most languages would do (infix).

(printf "5 + 3 = ~a.\n" (+ 5 3)) ; Addition operator
(printf "55 - 110 = ~a.\n" (- 55 110)) ; Subtraction operator
(printf "1 radian (180°/π) = ~a°.\n" (/ 180 pi)) ; Division operator
(printf "3.33 * 3 = ~a.\n" (* 3.33 3)) ; Multiplication operator
(printf "5 % 2 = ~a.\n" (remainder 5 2)) ; Modulus / remainder operator
(printf "2^8 = ~a.\n" (expt 2 8)) ; Exponentiation operator
(printf "| 5 - 30 | = ~a.\n" (abs (- 5 30))) ; Absolute value (unary)
(printf "sqrt(25) = ~a.\n" (sqrt 25)) ; Square root (unary)

(printf "Bitwise AND: 10 & 12 = ~a.\n" (bitwise-and #b1010 #b1100))
(printf "Bitwise OR 10 | 12 = ~a.\n" (bitwise-ior #b1010 #b1100))
(printf "Bitwise XOR 10 ^ 12 = ~a.\n" (bitwise-xor #b1010 #b1100))
(printf "Bitwise NOT ~~10 = ~a.\n" (bitwise-not #b1010))
(printf "Bitwise left shift 10 << 2 = ~a.\n" (arithmetic-shift #b1010 2))
(printf "Bitwise right shift 10 >> 2 = ~a.\n" (arithmetic-shift #b1010 -2))

(define (fmt-bool x)
  (if x "YES" "NO"))

(printf "Is 5 > 3 ? ~a.\n" (fmt-bool (> 5 3))) ; Logical GT
(printf "Is 31 >= 31 ? ~a.\n" (fmt-bool (>= 31 31))) ; Logical GTE
(printf "Is -2 < -5 ? ~a.\n" (fmt-bool (< -2 -5))) ; Logical LT
(printf "Is 0 <= -1 ? ~a.\n" (fmt-bool (<= 0 -1))) ; Logical LTE
(printf "Is 12 = 12 ? ~a.\n" (fmt-bool (= 12 12))) ; Logical EQ
(printf "Is 0.5 != 0.51 ? ~a.\n" (fmt-bool (not (= 0.5 0.51)))) ; Logical NOT

(printf "Logical AND: <false> && true && true = ~a.\n" (and false true true))
(printf "Logical OR: false || <true> || false = ~a.\n" (or false true false))

; We could technically name functions with opeartor-like symbols.
; For example, the bind operator, but only the implementation for
; the list monad, which is equivalent to the `mapcat` function.
(define (>>= m f)
  (apply append (map f m)))

(let ([tiers (list "Bronze" "Silver" "Gold" "Platinum" "Diamond")]
      [levels (range 1 6)])
  (>>= tiers (lambda (tier)
               (map (curry format "~a ~a" tier)
                    levels))))

; Control Structures
; ------------------

; While loop emulation through recursion in a `letrec` block.
(letrec ([loop (lambda (i)
                 (when (< i 5)
                   (begin
                     (printf "Mambo #~a!\n" (+ i 1))
                     (loop (+ i 1)))))])
  (loop 0))

; For loop emulation through a `for` block.
; NOTE: Instead of manually incrementing or decrementing a variable, the
; values are dispensed from lists, that's why you see a call to `range`.
(define verse-template
  (curry format
         "~a little monkeys jumping on the bed
One fell off and bumped his head
Mama called the doctor and the doctor said
\"No more monkeys jumping on the bed!\"\n"))

(for ([i (reverse (range 2 6))]
      #:when (odd? i)) ; guard clause
  (displayln (verse-template i)))

; The `for` block is mainly used for **side-effects** (IO operations) so the
; expression doesn't evaluate to anything. If we want to have something
; similar to a list comprehension (Haskell, Python, etc), we use `for/list`.
; NOTE: `for` and `for/list` blocks can be nested.
(define multiplication-table
  (for/list ([i (in-range 1 11)])
    (for/list ([j (in-range 1 11)])
      (* i j))))

(displayln multiplication-table)

; There are also multiplicative versions of these blocks, namely:
; 1. `for*`: Same as `for` but multiple bindings are combined as if we were
;    nesting for loops in imperative languages.
; 2. `for/list*`: Same as `for/list` but with multiplicative bindings.
(for* ([i (in-range 5)]
       [j (in-range 3)])
  (printf "Matrix coordinate m=5 n=3: (~a, ~a)\n" i j))

; If/else (2 branches only, can be nested)
(define age 31)

(if (>= age 18)
    (displayln "I can drink, vote, and go clubbing.")
    (displayln "I'm still underage."))

; Cond block for multiple condition evaluations with a default case.
; Source: https://docs.racket-lang.org/guide/syntax-overview.htm
; Note: Switch-like behaviour can be achieved by using the `=` function.
(define (reply-more s)
  (cond
    [(string-prefix? s "hello ")
     "hi!"]
    [(string-prefix? s "goodbye ")
     "bye!"]
    [(string-suffix? s "?")
     "I don't know"]
    [else "huh?"]))

(reply-more "what is your favorite color?")

; Switch case behaviour is implemented as `case`
(define fav-color "orange")

(case fav-color
  [("black") (displayln "Such an emo person :(")]
  [("red") (displayln "I see... very vibrant :)")]
  [("orange") (displayln "Orange is the new black!")]
  [else (displayln "I have no opinion on that color...")])

; Lastly, Racket offers powerful pattern-matching features through the `match`
; block, but it's out of the scope of this exercise.
; Refer to: https://docs.racket-lang.org/reference/match.html

#| DIFICULTAD EXTRA (opcional):
|| Crea un programa que imprima por consola todos los números comprendidos
|| entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
\+=========================================================================|#

(define (!= x y) (not (= x y)))

(for ([n (in-range 10 56)]
      #:when (!= n 16)
      #:when (!= (remainder n 3) 0))
  (printf "Pair number not 16, nor evenly divisible by 3 -> ~a\n" n))

#|
  Output of running `racket luishendrix92.rkt`:
  #############################################

  5 + 3 = 8.
  55 - 110 = -55.
  1 radian (180°/π) = 57.29577951308232°.
  3.33 * 3 = 9.99.
  5 % 2 = 1.
  2^8 = 256.
  | 5 - 30 | = 25.
  sqrt(25) = 5.
  Bitwise AND: 10 & 12 = 8.
  Bitwise OR 10 | 12 = 14.
  Bitwise XOR 10 ^ 12 = 6.
  Bitwise NOT ~10 = -11.
  Bitwise left shift 10 << 2 = 40.
  Bitwise right shift 10 >> 2 = 2.
  Is 5 > 3 ? YES.
  Is 31 >= 31 ? YES.
  Is -2 < -5 ? NO.
  Is 0 <= -1 ? NO.
  Is 12 = 12 ? YES.
  Is 0.5 != 0.51 ? YES.
  Logical AND: <false> && true && true = #f.
  Logical OR: false || <true> || false = #t.
  '("Bronze 1" "Bronze 2" "Bronze 3" "Bronze 4" "Bronze 5" "Silver 1" "Silver 2" "Silver 3" "Silver 4" "Silver 5" "Gold 1" "Gold 2" "Gold 3" "Gold 4" "Gold 5" "Platinum 1" "Platinum 2" "Platinum 3" "Platinum 4" "Platinum 5" "Diamond 1" "Diamond 2" "Diamond 3" "Diamond 4" "Diamond 5")
  Mambo #1!
  Mambo #2!
  Mambo #3!
  Mambo #4!
  Mambo #5!
  5 little monkeys jumping on the bed
  One fell off and bumped his head
  Mama called the doctor and the doctor said
  "No more monkeys jumping on the bed!"

  3 little monkeys jumping on the bed
  One fell off and bumped his head
  Mama called the doctor and the doctor said
  "No more monkeys jumping on the bed!"

  ((1 2 3 4 5 6 7 8 9 10) (2 4 6 8 10 12 14 16 18 20) (3 6 9 12 15 18 21 24 27 30) (4 8 12 16 20 24 28 32 36 40) (5 10 15 20 25 30 35 40 45 50) (6 12 18 24 30 36 42 48 54 60) (7 14 21 28 35 42 49 56 63 70) (8 16 24 32 40 48 56 64 72 80) (9 18 27 36 45 54 63 72 81 90) (10 20 30 40 50 60 70 80 90 100))
  Matrix coordinate m=5 n=3: (0, 0)
  Matrix coordinate m=5 n=3: (0, 1)
  Matrix coordinate m=5 n=3: (0, 2)
  Matrix coordinate m=5 n=3: (1, 0)
  Matrix coordinate m=5 n=3: (1, 1)
  Matrix coordinate m=5 n=3: (1, 2)
  Matrix coordinate m=5 n=3: (2, 0)
  Matrix coordinate m=5 n=3: (2, 1)
  Matrix coordinate m=5 n=3: (2, 2)
  Matrix coordinate m=5 n=3: (3, 0)
  Matrix coordinate m=5 n=3: (3, 1)
  Matrix coordinate m=5 n=3: (3, 2)
  Matrix coordinate m=5 n=3: (4, 0)
  Matrix coordinate m=5 n=3: (4, 1)
  Matrix coordinate m=5 n=3: (4, 2)
  I can drink, vote, and go clubbing.
  "I don't know"
  Orange is the new black!
  Pair number not 16, nor evenly divisible by 3 -> 10
  Pair number not 16, nor evenly divisible by 3 -> 11
  Pair number not 16, nor evenly divisible by 3 -> 13
  Pair number not 16, nor evenly divisible by 3 -> 14
  Pair number not 16, nor evenly divisible by 3 -> 17
  Pair number not 16, nor evenly divisible by 3 -> 19
  Pair number not 16, nor evenly divisible by 3 -> 20
  Pair number not 16, nor evenly divisible by 3 -> 22
  Pair number not 16, nor evenly divisible by 3 -> 23
  Pair number not 16, nor evenly divisible by 3 -> 25
  Pair number not 16, nor evenly divisible by 3 -> 26
  Pair number not 16, nor evenly divisible by 3 -> 28
  Pair number not 16, nor evenly divisible by 3 -> 29
  Pair number not 16, nor evenly divisible by 3 -> 31
  Pair number not 16, nor evenly divisible by 3 -> 32
  Pair number not 16, nor evenly divisible by 3 -> 34
  Pair number not 16, nor evenly divisible by 3 -> 35
  Pair number not 16, nor evenly divisible by 3 -> 37
  Pair number not 16, nor evenly divisible by 3 -> 38
  Pair number not 16, nor evenly divisible by 3 -> 40
  Pair number not 16, nor evenly divisible by 3 -> 41
  Pair number not 16, nor evenly divisible by 3 -> 43
  Pair number not 16, nor evenly divisible by 3 -> 44
  Pair number not 16, nor evenly divisible by 3 -> 46
  Pair number not 16, nor evenly divisible by 3 -> 47
  Pair number not 16, nor evenly divisible by 3 -> 49
  Pair number not 16, nor evenly divisible by 3 -> 50
  Pair number not 16, nor evenly divisible by 3 -> 52
  Pair number not 16, nor evenly divisible by 3 -> 53
  Pair number not 16, nor evenly divisible by 3 -> 55
|#