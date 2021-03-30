\ Model mip1
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  G[0] + G[2] + G[4] + G[6]
Subject To
 southern_wall: G[0] + G[1] + G[2] = 5
 eastern_wall: G[2] + G[3] + G[4] = 5
 northern_wall: G[4] + G[5] + G[6] = 5
 western_wall: G[0] + G[6] + G[7] = 5
 total_guards: G[0] + G[1] + G[2] + G[3] + G[4] + G[5] + G[6] + G[7] = 12
Bounds
Generals
 G[0] G[1] G[2] G[3] G[4] G[5] G[6] G[7]
End
