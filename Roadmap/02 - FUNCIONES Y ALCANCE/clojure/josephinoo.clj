(defn without-return [a b]
  (println (+ a b)))

(defn with-return [c d]
  (+ c d))

(defn without-parameters []
  (println "This is a function without parameters"))

(defn with-parameters [e]
  (println "This is the parameter to print: " e))

(defn inner-function []
  (defn second-function []
    (println "hello"))
  (second-function))


(defn recursive [g]
  (if (not= g 10)
    (do
      (println g)
      (recursive (inc g)))
    (println "final")))

(defn local [w]
  (let [local 10]
    (println (+ w local))))



; Extra
(defn extra [text1 text2]
  (doseq [item (range 1 100)]
    (cond
      (and (= (mod item 3) 0) (= (mod item 5) 0)) (println item text1 text2)
      (= (mod item 5) 0) (println item text2)
      (= (mod item 3) 0) (println item text1)
      :else (println item))))


(do
  (without-return 2 2)
  (println (with-return 2 2))

  (without-parameters)
  (with-parameters "hello")

  (inner-function)
  (recursive 1)

  (println (count [1 2 3]))

  (println local)
  (local 2)

  (extra "one" "two"))

(def global-variable 10)

(defn more-example-local []
  (let [local-variable 5]
    (println "Local variable:", local-variable))
  (println "Global variable:", global-variable))

; Calling the function
(more-example-local)

(println "Global variable outside the function:", global-variable)
