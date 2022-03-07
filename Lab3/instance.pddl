(define (problem sokobanlevel)
(:domain sokoban)
(:objects v0 v1 v2 v3 v4 v5 v6 v7 v8 v9 v10)
(:init (inc v0 v1) (dec v1 v0) 
(inc v1 v2) (dec v2 v1) 
(inc v2 v3) (dec v3 v2) 
(inc v3 v4) (dec v4 v3) 
(inc v4 v5) (dec v5 v4) 
(inc v5 v6) (dec v6 v5) 
(inc v6 v7) (dec v7 v6) 
(inc v7 v8) (dec v8 v7) 
(inc v8 v9) (dec v9 v8) 
(inc v9 v10) (dec v10 v9) 
(at player v4 v4)
(at box v4 v5) 
(at wall v4 v0) 
(at wall v3 v1) 
(at wall v3 v10) 
(at wall v5 v1) 
(at wall v5 v7) 
(at wall v5 v10) 
(at wall v8 v9) 
(at wall v10 v6) 
(at wall v9 v8) 
(at wall v0 v5) 
(at wall v2 v2) 
(at wall v10 v3) 
(at wall v2 v5) 
(at wall v1 v3) 
(at wall v1 v9) 
(at wall v7 v4) 
(at wall v6 v2) 
(at wall v7 v1) 
(at wall v7 v7) 
(at wall v6 v5) 
(at wall v7 v10) 
(at wall v3 v0) 
(at wall v5 v0) 
(at wall v5 v6) 
(at wall v9 v1) 
(at wall v9 v7) 
(at wall v10 v2) 
(at wall v8 v8) 
(at wall v10 v5) 
(at wall v1 v2) 
(at wall v0 v4) 
(at wall v2 v1) 
(at wall v2 v7) 
(at wall v1 v5) 
(at wall v2 v10) 
(at wall v1 v8) 
(at wall v7 v9) 
(at wall v6 v10) 
(at wall v4 v7) 
(at wall v5 v2) 
(at wall v4 v10) 
(at wall v5 v5) 
(at wall v8 v1) 
(at wall v10 v4) 
(at wall v0 v3) 
(at wall v10 v1) 
(at wall v10 v7) 
(at wall v1 v7) 
(at wall v2 v6) 
(at wall v1 v10) 
(at wall v7 v2) 
(at wall v7 v5) 
)
(:goal (and (at box v6 v6) 
)))
