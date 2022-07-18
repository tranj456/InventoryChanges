import os
import json
import sys

from .Item import Spec
from .Item import OutOfError

PATH = '~/.inv/.registry' # TODO: convert to configuration variable

sys.path.append(
  os.path.expanduser('~/.inv/')
)

class Acquire:

  def __init__(self, filename):
    import shutil
    list = List()

  @staticmethod
  def check(filename):
    pass

class List:

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

  def remove(self, item: str, number: int = -1) -> None:
    self.add(item, number)

  # Automatically remove empty or negative quantity items

  def empties(self) -> None:
    deletes = []
    for item in self.inventory:
      if self.inventory[item]["quantity"] <= 0:
        deletes.append(item)
    for item in deletes:
      del self.inventory[item]

class Items:

  def __init__(self, list):
    self.list = list.inventory

  def use(self, item: str):
    from importlib import import_module
    try:
      number = self.list[item]["quantity"]
      if number <= 0:
        raise OutOfError(item)
    except (KeyError, OutOfError) as e:
      print(f"You have no {item} remaining!")
      return
    object = import_module(f"{item}")
    instance = getattr(object, item)()
    if(instance.consumable):
      list.remove("Box")
      os.remove(
        os.path.expanduser(
          f'~/.inv/{item}.py'
        )
      )
    return instance.use()

# Create instances to use as shorthand
# I thought this was a bad idea, but this
# is actually how the random module works

# https://github.com/python/cpython/blob/main/Lib/random.py

list = List()
items = Items(list)
