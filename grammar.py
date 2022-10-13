"""
S -> 0A1 | B;
A -> aA | _;
B -> b;

primeiros(S): {0, b}
primeiros(A): {a, _}
primeiros(B): {b}

seguidores(S): {$}
seguidores(A): {a, 1}
seguidores(B): {$}
"""
table_ll1 = {
  "S, 0": ["0", "A", "1"],
  "S, b": ["B"], 
  "A, 1": ["_"],
  "A, a": ["a", "A"],
  "B, b": ["b"]
}

"""
S -> 0A | B;
A -> aA | 1;
B -> b;

table_ll1 = {
  "S, 0": ["0", "A"],
  "S, b": ["B"], 
  "A, 1": ["1"],
  "A, a": ["a", "A"],
  "B, b": ["b"]
}
"""