(define (domain monkeyproblem)
   (:requirements :adl)
   (:constants monkey bananas)
   (:predicates 
                 (goto ?x ?y) 
                 (climb ?x)
                 (push-chair ?x ?y)
                 (grab-bananas ?y)
                 (eat-bananas)
                 (on-floor)
                 (at ?x ?y)
                 (hasbananas)
                 (haseatenbananas)
                 (onchair ?x)
                 (step-down ?x)
   )

   (:action goto
             :parameters (?x ?y)
             :precondition (and 
                             (on-floor)
                             (at monkey ?y)
                             )
             :effect  (and 
                           (at monkey ?x)
                           (not (at monkey ?y))
                           )
    ) 


   (:action climb
             :parameters (?x)
             :precondition (and 
                             (at chair ?x)
                             (at monkey ?x)
                             )
             :effect  (and 
                           (onchair ?x)
                           (not (on-floor))
                           )
    ) 

   (:action step-down
             :parameters (?x)
             :precondition (and 
                             (onchair ?x)
                             (at monkey ?x)
                             )
             :effect  (and 
                           (on-floor)
                           (not (onchair ?x))
                           )
    ) 

   (:action push-chair 
             :parameters (?x ?y)
             :precondition (and 
                             (at chair ?y)
                             (at monkey ?y)
                             (on-floor)
                             )
             :effect  (and 
                           (at monkey ?x)
                           (at chair ?x)
                           (not (at monkey ?y))
                           (not (at chair ?y))
                           )
    ) 

   (:action grab-bananas
             :parameters (?y)
             :precondition (and 
                             (at bananas ?y)
                             (onchair ?y)
                             )
             :effect  (and 
                           (hasbananas)
                           )
    )
    
    (:action eat-bananas
             :parameters ()
             :precondition (and 
                             (hasbananas)
                             )
             :effect  (and 
                           (haseatenbananas)
                           )
    )
)