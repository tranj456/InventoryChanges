import yaml
from time import sleep

from .Path import Path

class Narrator:

  def __init__(self):
    fh = open(".paths.yml")
    self.paths = yaml.safe_load(fh)
    self.path = Path()

  def narrate(self):
    lines = self.paths[self.path.number][self.path.scene]
    for line in lines:
      print(line)
      sleep(1)
