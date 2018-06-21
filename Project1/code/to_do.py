from Algorithms_Search.code.A_star import A_Star
from Algorithms_Search.code.BFS import BFS
from Algorithms_Search.code.bidirectional import bidirectSearch
from cube.cube import Cube


def act1(path ):
     act = []
     for i in range(0, len(path)):

          if i == len(path) - 1:
               return act
          m = path[i]
          n = path[i + 1]
          if m[0] == n[0] - 1:
               act.append('d')
          if m[0] == n[0] + 1:
               act.append('u')
          if m[1] == n[1] - 1:
               act.append('r')
          if m[1] == n[1] + 1:
               act.append('l')

def act2(path):
     act = []
     for i in range(0, len(path)):

          if i == len(path) - 1:
               return act
          m = path[i]
          n = path[i + 1]
          for j in range(0, 9) :
               if ( j >= 2) :
                    if m[j - 2] == n[j - 1]:
                         act.append('r')
               if (j >= 1):
                    if m[j - 1] == n[j]:
                         act.append('l')
               if (j >= 1 and j <= 6):
                    if m[j + 2] == n[j - 1]:
                         act.append('u')
               if (j >= 4):
                    if m[j - 4] == n[j - 1]:
                         act.append('l')

def act3(path):
     act = []
     for i in range(0, len(path)):

          if i == len(path) - 1:
               return act
          m = path[i]
          n = path[i + 1]
          if (n[1] == m[13] and
               n[3] == m[15] and
               n[5] == m[1] and
               n[7] == m[3] and
               n[9] == m[5] and
               n[11] == m[7] and
               n[13] == m[9] and
               n[15] == m[11] and
               n[20] == m[22] and
               n[21] == m[20]and
               n[22] == m[23]and
               n[23] == m[21]) :
               act.append('RC')
          if (n[1] == m[5] and
                    n[3] == m[7] and
                    n[5] == m[9] and
                    n[7] == m[11] and
                    n[9] == m[13] and
                    n[11] == m[15] and
                    n[13] == m[1] and
                    n[14] == m[14] and
                    n[15] == m[3] and
                    n[20] == m[21] and
                    n[21] == m[23] and
                    n[22] == m[20] and
                    n[23] == m[22] ) :
               act.append('R')
          if (n[0] == m[2] and
                    n[1] == m[0] and
                    n[2] == m[3] and
                    n[3] == m[1] and
                    n[4] == m[20] and
                    n[5] == m[21] and
                    n[14] == m[16] and
                    n[15] == m[17] and
                    n[16] == m[4] and
                    n[17] == m[5] and
                    n[20] == m[15] and
                    n[21] == m[14] and
                    n[22] == m[22] and
                    n[23] == m[23] ):
               act.append('T')
          if (n[0] == m[1] and
                    n[1] == m[3] and
                    n[2] == m[0] and
                    n[3] == m[2] and
                    n[4] == m[16] and
                    n[5] == m[17] and
                    n[14] == m[21] and
                    n[15] == m[20] and
                    n[16] == m[14] and
                    n[17] == m[15] and
                    n[20] == m[4] and
                    n[21] == m[5] and
                    n[22] == m[22] and
                    n[23] == m[23] ):
               act.append('TC')
          if ( n[0] == m[2] and
                    n[1] == m[0] and
                    n[2] == m[19] and
                    n[3] == m[17] and
                    n[4] == m[6] and
                    n[5] == m[4] and
                    n[6] == m[7] and
                    n[7] == m[5] and
                    n[8] == m[22] and
                    n[9] == m[20] and
                    n[14] == m[16] and
                    n[15] == m[17] and
                    n[16] == m[4] and
                    n[17] == m[8] and
                    n[19] == m[9] and
                    n[20] == m[2] and
                    n[21] == m[14] and
                    n[22] == m[3] ):
               act.append('F')

               if (n[0] == m[2] and
                    n[1] == m[0] and
                    n[2] == m[20] and
                    n[3] == m[22] and
                    n[4] == m[5] and
                    n[5] == m[7] and
                    n[6] == m[4]and
                    n[7] == m[6] and
                    n[8] == m[17] and
                    n[9] == m[19] and
                    n[14] == m[16] and
                    n[15] == m[17] and
                    n[16] == m[4] and
                    n[17] == m[3] and
                    n[18] == m[18] and
                    n[19] == m[2] and
                    n[20] == m[9] and
                    n[22] == m[8] ):
                    act.append('FC')
# first q input
m, s, n = input('first q')
wall = input('first q walls')
list = []
for i in range(0, int(wall)):
     a = [int(x) for x in input().split()]
     list.append(a)
#1
r = Tracker([[[1,1]]],[[[int(m),int(n)]]],int(m),int(n),list)
b = bidirectSearch(r)
b.biSearch()
print('bidirectional search')
print('path :',b.path)
print('max memory',b.maxMemory)
print('visited',b.visited)
print('expand',b.expand)
print('act',act1(b.path))


# second q input
b = [int(x) for x in input().split()]
#
#
r = Puzzle([[b]],[[[1,2,3,4,5,6,7,8,0]]])
b = bidirectional(r)
b.biSearch()
print('bidirectional search')
print('path :',b.path)
print('max memory',b.maxMemory)
print('visited',b.visited)
print('expand',b.expand)
print('act',act2((b.path)))
#



# third q input
c = [int(x) for x in input().split()]
#
#
r = Cube([[['y','b','y','b','g','y','g','y','w','g','w','g','b','w','b','w','r','r','r','r','o','o','o','o']]],[[['b','b','b','b','y','y','y','y','g','g','g','g','w','w','w','w','r','r','r','r','o','o','o','o']]])
b = BFS(r)
b.bfsSearch()
print ('bfs ')
print('path :',b.path)
print('max memory',b.maxMemory)
print('visited',b.visited)
print('expand',b.expand)
print('act',act3((b.path)))
#
