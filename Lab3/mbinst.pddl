(define (problem monkey)
   (:domain monkeyproblem)
   (:objects p1 p2 p3 p4 p5 p6)
   (:init
    
     (at monkey p1)
     (on-floor)
     (at chair p6)
     (at bananas p3)

   )

   (:goal 
       (and 
        (haseatenbananas)
       )
       )
)