import sqlite3
from stack import Stack

class MatchDB():
  def __init__(self):
    self.match_ = Stack(999)
    self.stack = []
    self.input_str = []
    self.action = []

    self._con = sqlite3.connect("Match Table")
    self.cursor = self._con.cursor()

    self._con.execute("""
      drop table if exists match;
    """).fetchall()

    self._con.execute("""
      create table if not exists match (
        match varchar(255), 
        stack varchar(255), 
        input varchar(255), 
        action varchar(255)
      );
    """).fetchall()
  
  def insertInto(self):
    try:
      self.cursor.execute(f"""
        insert into match (match, stack, input, action) values 
        ("{self.match_}", "{self.stack}", "{self.input_str}", "{self.action}");
      """)
      self._con.commit()
    except sqlite3.Error as erro:
      print(f"Error: {erro}") 
  
  def set(self, match, stack, input_str, action):
    if match: self.match_.put(match)
    self.stack = stack
    self.input_str = input_str
    self.action = action