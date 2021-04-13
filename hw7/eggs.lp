\ Model Eggs
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  X
Subject To
 By_2: X - 2 C1 = 1
 By_3: X - 3 C2 = 1
 By_4: X - 4 C3 = 1
 By_5: X - 5 C4 = 1
 By_6: X - 6 C5 = 1
 By_7: X - 7 C6 = 0
Bounds
 C1 >= 3
 C2 >= 2
 C3 >= 2
 C4 >= 2
 C5 >= 1
 C6 >= 1
Generals
 X C1 C2 C3 C4 C5 C6
End
