\ Model FireStations
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0 X[0] + 0 X[1] + 0 X[2] + 0 X[3] + 0 X[4] + 0 X[5] + X[0] + X[1] + X[2]
   + X[3] + X[4] + X[5]
Subject To
 City_1: X[0] + X[1] >= 1
 City_1: X[0] + X[1] >= 1
 City_2: X[0] + X[1] + X[5] >= 1
 City_3: X[2] + X[3] >= 1
 City_4: X[2] + X[3] + X[4] >= 1
 City_5: X[3] + X[4] + X[5] >= 1
 City_6: X[1] + X[4] + X[5] >= 1
 Implicit,_City_1: X[0] >= 0
 Implicit,_City_2: X[1] >= 0
 Implicit,_City_3: X[2] >= 0
 Implicit,_City_4: X[3] >= 0
 Implicit,_City_5: X[4] >= 0
 Implicit,_City_6: X[5] >= 0
Bounds
Generals
 X[0] X[1] X[2] X[3] X[4] X[5] X[0] X[1] X[2] X[3] X[4] X[5]
End
