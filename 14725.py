import sys

n = int(input())

class Node() : 
  def __init__(self, key):
    self.key = key
    self.children = {}

class Trie : 
  def __init__(self) : 
    self.head = Node(None)

  def insert(self, foods) : 
    cur = self.head
    for food in foods : 
      if food not in cur.children : 
        cur.children[food] = Node(food)
      cur = cur.children[food]

  def printAnthill(self, cur, depth) : 
    for k, v in sorted(cur.children.items()) : 
      for _ in range(depth) : 
        print("--", end="")
      print(k)

      self.printAnthill(v, depth+1)

def solve(n) :
  trie = Trie()
  for _ in range(n) :
    line = sys.stdin.readline().strip().split()
    foods = line[1 : len(line)]
    trie.insert(foods)
  
  trie.printAnthill(trie.head, 0)

solve(n)