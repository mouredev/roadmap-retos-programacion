#lang racket

#|-----------------------------------------------------------------+\
||                Racket - The programming language                ||
||                                                                 ||
|| Official Website: https://racket-lang.org/#racket-lang          ||
|| Documentation: https://docs.racket-lang.org/quick/index.html    ||
||                                                                 ||
|| This is a multi-line (block) comment using the `#||#` syntax.   ||
||                                                                 ||
\+-----------------------------------------------------------------|#

; Single-line comments
; --------------------
; Unfortunately, there is no built-in way to provide documentation
; comments in Racket, but we could define a custom macro to do so.

; Top level variables in LISP-based languages are called definitions and they
; can mutated in-place, and can't be re-defined unlike in other functional
; languages. To mutate a definition we use the `set!` function although it's
; heavily discouraged in any *Scheme* dialect (chicken, racket, MIT, etc).
;
; NOTE: Definitions created inside a function's body are local to it.
(define x 5)
; (define x (+ x 10)) <- compilation error
(printf "Value of definition 'x': ~a\n" x)
(set! x (+ x 10)) ; In-place mutation of 'x'
(printf "Value of definition 'x' after mutation with set!: ~a.\n" x)

; Local bindings with `let` and `let*`.
(let ([grade1 95]
      [grade2 100]
      [grade3 66])
  (printf "Average of the grades ~a, ~a, and ~a is ~a.\n"
          grade1 grade2 grade3
          (exact->inexact (/ (+ grade1 grade2 grade3) 3))))

; `let*` allows us to refer to earlier bindings inside the vector.
(let* ([height 6.5]
       [width 12.0]
       [area (* height width)]) ; would give compilation error in a `let` block
  (printf "The area of a rectangle w=~am, h=~am is ~am^2.\n"
          height width area))

; Primitive data types
; --------------------

(displayln 42) ; Number (integer)
(displayln -99.99) ; Number (float / inexact)
(displayln 3/4) ; Number (fraction / exact)
(displayln 1+2i) ; Number (imaginary)
(displayln 3.3e+5) ; Number (scientific notation)
(displayln "Half Life 2 \u03BB") ; String
(displayln true) ; Boolean (true -> #t)
(displayln false) ; Boolean (false -> #f)

; In LISP langauges, lists are important as well, and the language itself
; is just data represented as unevaluated lists of symbols and values.
; So, even though they're not considered "primitive", they are foundational.
(displayln '(5 4 3 2 1 0)) ; List (quoted representation)
(displayln (list 0 1 2 3 4 5)) ; List (constructed through the `list` function)

(println "¡Hola, Racket!")

#|
  Output of running `racket luishendrix92.rkt`:
  #############################################

  Value of definition 'x': 5
  Value of definition 'x' after mutation with set!: 15.
  Average of the grades 95, 100, and 66 is 87.0.
  The area of a rectangle w=6.5m, h=12.0m is 78.0m^2.
  42
  -99.99
  3/4
  1+2i
  330000.0
  Half Life 2 λ
  #t
  #f
  (5 4 3 2 1 0)
  (0 1 2 3 4 5)
  "¡Hola, Racket!"
|#