class Path:

  def __init__(self, path: int = 0):
    self.number = path
    self.scene = 0

  def next_scene(self):
    self.scene += 1

  def change_path(self, path: int = 0):
    self.number = path
    self.scene = 0
