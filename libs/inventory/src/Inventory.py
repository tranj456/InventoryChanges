import os
import json

from .Item import Spec

class Inventory:

  PATH = '~/.inv/.registry'

  def __init__(self):
    self.inventory = self.open_inv("r+")

  def open_inv(self, mode: str) -> dict:
    fh = open(
      os.path.expanduser(PATH),
      mode
    )
    try:
      return json.load(fh)
    except:
      return {}

  def write_inv(self, mode: str = "w+") -> None:
    pass

  def add_item(self, item: str) -> None:
    try:
      self.inventory[item]["qty"] += 1
    except:
      self.inventory[item] = {
        "qty": 1,
        "traits": {}
      }
