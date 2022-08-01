import os
import sys
import json

from .Config import *

from .Item import ItemSpec
from .Item import FixtureSpec
from .Item import BoxSpec
from .Item import OutOfError
from .Item import IsFixture

PATH = f'{Config.values["INV_PATH"]}/{Config.values["INV_REGISTRY"]}'

sys.path.append(
  [
    os.path.expanduser(os.getcwd()),
    os.path.expanduser(f'{Config.values["INV_PATH"]}')
  ]
)

class Acquire:

  import shutil
  import importlib

  def __init__(self, filename):
    self.filename = filename
    self.validate()
    self.move()
    self.add()

  def is_box(self, item) -> bool:
    self.box = "BoxSpec" in dir(item)

  def validate(self):
    import importlib
    try:
      self.name, self.ext = self.filename.split(".")
      if not self.ext == "py":
        raise
      obj = importlib.import_module(self.name)
      getattr(obj, self.name)().use
      self.is_box(obj)
    except Exception as e:
      print("Not a valid item file")
      exit()

  def move(self):
    import shutil
    try:
      path = os.path.expanduser(
        f'{Config.values["INV_PATH"]}/{self.filename}'
      )
      if not self.box:
        shutil.copy(self.filename, path)
    except Exception as e:
      print(f"Couldn't acquire {self.name}")
      exit()

  def add(self):
    try:
      list.add(self.name)
    except Exception as e:
      print(f"Couldn't acquire {self.name}")
      exit()

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

  def is_fixture(self, item) -> bool:
    return "FixtureSpec" in dir(item)

  def is_box(self, item) -> bool:
    return "BoxSpec" in dir(item)

  def use(self, item: str):
    from importlib import import_module

    box = False
    fixture = False

    try:
      item_file = import_module(f"{item}")
    except ModuleNotFoundError:
      print(f"You don't seem to have any {item}.")
      return

    try:
      fixture = self.is_fixture(item_file)
      if fixture:
        raise IsFixture(item)
      box = self.is_box(item_file)
      if box:
        raise IsFixture(item)
      number = self.list[item]["quantity"]
      if number <= 0:
        raise OutOfError(item)
    except (KeyError, OutOfError) as e:
      print(f"You have no {item} remaining!")
      return
    except IsFixture as e:
      pass

    try:
      instance = getattr(item_file, item)()
    except:
      print(f"{item} doesn't seem to be a valid object.")
      return

    if(instance.consumable and not box):
      list.remove(item)
      os.remove(
        os.path.expanduser(
          f'{Config.values["INV_PATH"]}/{item}.py'
        )
      )

    if(box):
      os.remove(
        item_file.__file__
      )

    if type(instance).__str__ is not object.__str__:
      instance.use()
      print(f"{instance}")
    else:
      return instance.use()

# Create instances to use as shorthand
# I thought this was a bad idea, but this
# is actually how the random module works

# https://github.com/python/cpython/blob/main/Lib/random.py

list = List()
items = Items(list)
