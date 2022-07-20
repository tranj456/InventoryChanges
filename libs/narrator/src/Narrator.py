import yaml
from time import sleep

# Syntax narrator.path().next_scene()

class Narrator:

  def __init__(self):
    fh = open(".paths.yaml")
    self.paths = yaml.safe_load(fh)
    self.current_path = 0

  def path(self):
    def next_scene(self):
      pass
    pass
