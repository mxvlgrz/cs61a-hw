;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Streams

(define (find s predicate)
  (if (null? s)
    #f
    (if (predicate (car s))
      (car s)
      (find (cdr-stream s) predicate)
    )
  )
)

(define (scale-stream s k)
  (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))
)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? seen-so-far curr) #t)
          (else (pair-tracker (append seen-so-far `(,curr)) (cdr-stream curr)))
    )
  )
  (pair-tracker () s)
)

(define (contains? lst s)
  (if (null? lst)
    #f
    (if (eq? (car lst) s)
      #t
      (contains? (cdr lst) s)
    )
  )
)

(define (has-cycle-constant s)
  (define (helper slow-p fast-p)
    (if (eq? slow-p fast-p)
      #t
      (if (null? (cdr-stream fast-p))
        #f
        (if (null? (cdr-stream (cdr-stream fast-p)))
          #f
          (helper (cdr-stream slow-p) (cdr-stream (cdr-stream fast-p)))
        )
      )
    )
  )
  (if (null? (cdr-stream s))
    #f
    (if (null? (cdr-stream (cdr-stream s)))
      #f
      (helper (cdr-stream s) (cdr-stream (cdr-stream s))) 
    )
  )
)

; Tail recursion

(define (accumulate combiner start n term)
  (define (helper result combiner i term)
    (if (= i 0)
      result
      (helper (combiner result (term i)) combiner (- i 1) term)
    )
  )
  (helper start combiner n term)
)

; Macros

(define-macro (list-of expr for var in lst if filter-expr)
  `(map (lambda (,var) ,expr) (filter (lambda (,var) ,filter-expr) ,lst))
)