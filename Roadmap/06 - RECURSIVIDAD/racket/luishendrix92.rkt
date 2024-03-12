#lang racket

(letrec ([loop (lambda (n)
                 (when (>= n 0)
                   (begin
                     (printf "n = ~a\n" n)
                     (loop (- n 1)))))])
  (loop 100))

#| DIFICULTAD EXTRA (opcional):
|| ----------------------------
|| Utiliza el concepto de recursividad para:
|| - Calcular el factorial de un número concreto (la función recibe ese número).
|| - Calcular el valor de un elemento concreto (según su posición) en la
||   sucesión de Fibonacci (la función recibe la posición).
\+============================================================================|#

(define (factorial n)
  (if (> n 1)
      (* n (factorial (- n 1)))
      1))

(define (fib n)
  (if (> n 1)
      (+ (fib (- n 1)) (fib (- n 2)))
      n))

(printf "Factorial calculation: 5! = ~a\n" (factorial 5))
(printf "The 12° number in the fibonacci sequence is: ~a\n" (fib 12))

#|
  Output of running `racket luishendrix92.rkt`:
  =============================================
  n = 100
  n = 99
  n = 98
  n = 97
  n = 96
  n = 95
  n = 94
  n = 93
  n = 92
  n = 91
  n = 90
  n = 89
  n = 88
  n = 87
  n = 86
  n = 85
  n = 84
  n = 83
  n = 82
  n = 81
  n = 80
  n = 79
  n = 78
  n = 77
  n = 76
  n = 75
  n = 74
  n = 73
  n = 72
  n = 71
  n = 70
  n = 69
  n = 68
  n = 67
  n = 66
  n = 65
  n = 64
  n = 63
  n = 62
  n = 61
  n = 60
  n = 59
  n = 58
  n = 57
  n = 56
  n = 55
  n = 54
  n = 53
  n = 52
  n = 51
  n = 50
  n = 49
  n = 48
  n = 47
  n = 46
  n = 45
  n = 44
  n = 43
  n = 42
  n = 41
  n = 40
  n = 39
  n = 38
  n = 37
  n = 36
  n = 35
  n = 34
  n = 33
  n = 32
  n = 31
  n = 30
  n = 29
  n = 28
  n = 27
  n = 26
  n = 25
  n = 24
  n = 23
  n = 22
  n = 21
  n = 20
  n = 19
  n = 18
  n = 17
  n = 16
  n = 15
  n = 14
  n = 13
  n = 12
  n = 11
  n = 10
  n = 9
  n = 8
  n = 7
  n = 6
  n = 5
  n = 4
  n = 3
  n = 2
  n = 1
  n = 0
  Factorial calculation: 5! = 120
  The 12° number in the fibonacci sequence is: 144
|#