from collections import namedtuple

class Path:

  def __init__(self, path: int = 0):
    self.number = path
    self.scene = 0

  def next_scene(self):
    self.scene += 1

  def change(self, outcome: float = 0):
    path, scene = str(outcome).split(".")
    self.number = int(path)
    self.scene = int(scene)
