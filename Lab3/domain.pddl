(define (domain sokoban)
        (:requirements :adl :strips)
        (:constants player box wall)
        (:predicates (at ?p ?x ?y)
                        (inc ?x ?nx)
                        (dec ?x ?nx)
                        (use_teleport ?t)         
        )
        (:action move-player-right
                :parameters (?x ?y ?yn)
                :precondition (and (at player ?x ?y)
                                (not (at box ?x ?yn))
                                (not (at wall ?x ?yn))
                                (inc ?y ?yn)
                )
                :effect	        (and (at player ?x ?yn)
                                (not (at player ?x ?y)))
        )
        (:action move-player-left
                :parameters (?x ?y ?yn)
                :precondition (and (at player ?x ?y)
                                (not (at box ?x ?yn))
                                (not (at wall ?x ?yn))
                                (dec ?y ?yn)
                )
                :effect		(and (at player ?x ?yn)
                                (not (at player ?x ?y)))
        )
        (:action move-player-down
                :parameters (?x ?y ?xn)
                :precondition (and (at player ?x ?y)
                                (not (at box ?xn ?y))
                                (not (at wall ?xn ?y))
                                (inc ?x ?xn)
                )
                :effect		(and (at player ?xn ?y)
                                (not (at player ?x ?y)))
        )
        (:action move-player-up
                :parameters (?x ?y ?xn)
                :precondition (and (at player ?x ?y)
                                (not (at box ?xn ?y))
                                (not (at wall ?xn ?y))
                                (dec ?x ?xn)
                )
                :effect		(and (at player ?xn ?y)
                                (not (at player ?x ?y)))
        )
        (:action push-box-right
                :parameters (?x ?y ?yn ?ynn)
                :precondition (and (at player ?x ?y)
                                (at box ?x ?yn)
                                (not (at wall ?x ?yn))
                                (inc ?y ?yn)
                                (not (at box ?x ?ynn))
                                (not (at wall ?x ?ynn))
                                (inc ?yn ?ynn)
                )
                :effect		(and (at player ?x ?yn)
                                (at box ?x ?ynn)
                                (not (at player ?x ?y))
                                (not (at box ?x ?yn)))
        )
        (:action push-box-left
                :parameters (?x ?y ?yn ?ynn)
                :precondition (and (at player ?x ?y)
                                (at box ?x ?yn)
                                (not (at wall ?x ?yn))
                                (dec ?y ?yn)
                                (not (at box ?x ?ynn))
                                (not (at wall ?x ?ynn))
                                (dec ?yn ?ynn)
                )
                :effect		(and (at player ?x ?yn)
                                (at box ?x ?ynn)
                                (not (at player ?x ?y))
                                (not (at box ?x ?yn)))
        )
        (:action push-box-down
                :parameters (?x ?y ?xn ?xnn)
                :precondition (and (at player ?x ?y)
                                (at box ?xn ?y)
                                (not (at wall ?xn ?y))
                                (inc ?x ?xn)
                                (not (at box ?xnn ?y))
                                (not (at wall ?xnn ?y))
                                (inc ?xn ?xnn)
                )
                :effect		(and (at player ?xn ?y)
                                (at box ?xnn ?y)
                                (not (at player ?x ?y))
                                (not (at box ?xn ?y)))
        )
        (:action push-box-up
                :parameters (?x ?y ?xn ?xnn)
                :precondition (and (at player ?x ?y)
                                (at box ?xn ?y)
                                (not (at wall ?xn ?y))
                                (dec ?x ?xn)
                                (not (at box ?xnn ?y))
                                (not (at wall ?xnn ?y))
                                (dec ?xn ?xnn)
                )
                :effect		(and (at player ?xn ?y)
                                (at box ?xnn ?y)
                                (not (at player ?x ?y))
                                (not (at box ?xn ?y)))
        )
        (:action teleport
                :parameters (?x ?y ?xn ?yn)
                :precondition (and (at player ?x ?y)
                                (not (at box ?xn ?yn))
                                (not (at wall ?xn ?yn))
                                (use_teleport ?t)
                )
                :effect         (and (at player ?xn ?yn)
                                (not (at player ?x ?y))
                                (not(use_teleport ?t)))
                )
)