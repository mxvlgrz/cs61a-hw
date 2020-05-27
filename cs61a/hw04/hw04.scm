; Q1
(define (sign x)
  (if (= x 0) 0 (if (> x 0) 1 -1))
)

; Q2
(define (square x) (* x x))

(define (pow b n)
  (if 
    (= n 2) (square b) 
    (if (= (modulo n 2) 0) 
      (square (pow b (/ n 2)))  
      (* b (pow b (- n 1)))
    )
  )
)

; Q3
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

; Q4
(define (ordered? s)
  (if (null? (cdr s)) 
    #t 
    (if (<= (car s) (car (cdr s)))
      (ordered? (cdr s))
    #f)
  )
)

; Q5
(define (nodots s)
  (if (null? s) 
    s 
    (if (pair? s) 
      (cons 
        (if (pair? (car s)) 
          (nodots (car s)) 
          (car s)) 
        (nodots (cdr s))) 
      (cons s ())
    )
  )
)

; Q6
(define (empty? s) (null? s))

(define (add s v)
  (if (empty? s)
    (cons v ())
    (if (= (car s) v)
      s
      (if (> (car s) v)
        (cons v s)
        (cons (car s) (add (cdr s) v))
      )
    )
  )
)

; Q7
; Sets as sorted lists
(define (contains? s v)
  (if (null? s) 
    #f
    (if (= (car s) v)
      #t
      (if (> (car s) v) 
        #f
        (contains? (cdr s) v)
      )
    )
  )
)

; Q8
(define (intersect s t)
  (if (empty? t) 
    ()
    (if (contains? s (car t))
        (cons (car t) (intersect s (cdr t)))
        (intersect s (cdr t))
    )
  )
)

(define (union s t)
  (if (empty? t)
    s
    (add (union s (cdr t)) (car t))
  )
)