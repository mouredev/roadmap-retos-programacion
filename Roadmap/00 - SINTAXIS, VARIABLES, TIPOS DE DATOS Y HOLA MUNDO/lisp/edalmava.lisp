;; La implementación usada es Steel Bank Common Lisp (SBCL)
;; Sitio consultado: https://lisp-lang.org/
;; IDE usado: https://portacle.github.io/

;; Los comentarios de una línea empiezan por punto y coma ;
;; y pueden comenzar en cualquier punto de la línea

#|
Este es un comentario
de varias líneas.
Todo lo que esté aquí será ignorado.
|#

;; Las variables léxicas locales se declaran con el operador especial let:
(let ((x 5)(y 2)) (* x y))   ; 10
; Usando definiciones anteriores
(let* ((x 10)(y (+ x 5)))(* x y)) ; 150

;; defparameter declara una variable global y la inicializa. Si ya existe, se vuelve a inicializar.
(defparameter *mi-variable* 42) ; Variable global con valor 42
;; defvar declara una variable global solo si no existe ya. Si existe, no cambia su valor.
(defvar *otra-variable* 100) ; Declara si no está definida
(defvar *otra-variable* 200) ; No cambia el valor existente

;; Usa defconstant para definir una constante cuyo valor no debe cambiar.
(defconstant +pi+ 3.14159)

(format t "¡Hola, Lisp!")  ; Imprimir la cadena "¡Hola, Lisp!"
(print "¡Hola, Lisp usando SBCL!")
