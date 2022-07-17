import os
import json
import sys

from .Item import Spec

PATH = '~/.inv/.registry' # TODO: convert to configuration variable

class list:

  # File operations

  def __init__(self):
    self.inventory = {}
    try:
      fh = open(
        os.path.expanduser(PATH),
        "r+"
      )
      self.inventory = json.load(fh)
      fh.close()
    except: pass

  def write(self) -> None:
    self.empties()
    with open(
      os.path.expanduser(PATH),
      "w"
    ) as fh:
      json.dump(self.inventory, fh)

  # Representation

  def __str__(self) -> str:
    return json.dumps(self.inventory)

  # Add/remove items

  def add(self, item: str, number: int = 1) -> None:
    if item in self.inventory:
      self.inventory[item]["quantity"] += number
    else:
      self.inventory[item] = {
        "quantity": number,
        "filename": f"{item}.py"
      }
    self.write()

  def remove(self, item: str, number: int = 1) -> None:
    self.add(item, -1 * number)

  # Automatically remove empty or negative quantity items

  def empties(self) -> None:
    for item in self.inventory:
      if self.inventory[item]["quantity"] <= 0:
        del self.inventory[item]

if __name__ == "__main__":
  exit()
