from stack import Stack
from match_db import MatchDB as DB
from util import CHAR_SPECIAL 
from grammar import table_ll1

class PredictiveAnalytics(DB):
  def __init__(self, input_str, S=['S']):
    super().__init__()

    self.input_str = Stack(999)
    self.input_str.put('$')
    input_str = list(reversed(input_str))
    for e in input_str:
      self.input_str.put(e)
    
    self.stack = Stack(999)
    self.stack.put('$')
    self.stack.put(S[0])

  def PredictiveAnalytics(self):
    while not self.stack.empty and self.stack.list[self.stack.top] != "$":
      top_input = self.input_str.list[self.input_str.top]
      top_stack = self.stack.list[self.stack.top]

      if top_stack == top_input:
        self.match(top_stack)
      elif self.isTerminalSymbol(top_stack): 
        break
      elif not self.getTransition(top_stack, top_input): 
        break
      else: 
        self.stackNewTransition(top_input, top_stack)

    if self.stack.list[self.stack.top] == "$" and self.input_str.list[self.stack.top] == "$":
      self.addDB("", "OK")
    else: self.addDB("", "Error")

  def addDB(self, match, action):
    DB.set(self, match, self.stack, self.input_str, action)
    DB.insertInto(self)
  
  def match(self, element):
    self.addDB(element, "Match")
    self.input_str.get()
    self.stack.get()
  
  def isTerminalSymbol(self, symbol): 
    return symbol.islower() or symbol in CHAR_SPECIAL
  
  def getTransition(self, top_stack, top_input):
    return table_ll1.get(f"{top_stack}, {top_input}")
  
  def stackNewTransition(self, top_input, top_stack):
    to_stack = self.getTransition(top_stack, top_input)
    to_stack = list(reversed(to_stack))
    action = f"{top_stack}->{list(reversed(to_stack))}"
    self.addDB("", action)

    self.stack.get()

    for e in to_stack: 
      if e != '_': 
        self.stack.put(e)
    
if __name__=="__main__":
  pa = PredictiveAnalytics(['0', 'a', 'a', 'a', '1'])
  pa.PredictiveAnalytics()