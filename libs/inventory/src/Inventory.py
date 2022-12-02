import os
import sys
import json
import argparse

from rich.table import Table
from rich.console import Console
from collections import namedtuple

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

  # Create a nice(r) display

  def display(self):
    table = Table(title=f"{os.getenv('LOGNAME')}'s inventory")

    table.add_column("Item name")
    table.add_column("Item count")
    table.add_column("Item file")
    table.add_column("Consumable")
    for item in self.inventory:
      table.add_row(
        item,
        str(self.inventory[item]["quantity"]),
        self.inventory[item]["filename"],
        str(self.determine_consumable(item))
      )

    console = Console()
    console.print(table)
    
  def determine_consumable(self, item):
    
    from importlib import import_module
    
    try:
      item_file = import_module(f"{item}")
    except ModuleNotFoundError:
      print(f"You don't seem to have any {item}.")
      return
    
    try:
      instance = getattr(item_file, item)()
    except:
      print(f"{item} doesn't seem to be a valid object.")
      return
    
    consumable = instance.consumable
    return consumable

class Items:

    def __init__(self, list):
        self.list = list.inventory

    def is_fixture(self, item) -> bool:
        return "FixtureSpec" in dir(item)

    def is_box(self, item) -> bool:
        return "BoxSpec" in dir(item)

    def trash(self, item: str, rem_quantity: int = 1):
        from importlib import import_module
        try:
            item_file = import_module(f"{item}")
        except ModuleNotFoundError:
            print(f"You don't seem to have any {item}.")
            return
        List.add(item, 0 - rem_quantity)
        if self.list[item]["quantity"] <= 0:
            try:
                list.remove(item) 
            except: pass
    
    def use(self, item: str):
    # Import necessary reflection module
        from importlib import import_module

    # Set up properties and potential kwargs
        box = False
        fixture = False

    # Verify that item is in path or inventory
        try:
            item_file = import_module(f"{item}")
        except ModuleNotFoundError:
            print(f"You don't seem to have any {item}.")
            return

    # Test type of item; remove if ItemSpec
        try:
            box = self.is_box(item_file)
            fixture = self.is_fixture(item_file)
            if fixture or box:
                raise IsFixture(item)
            number = self.list[item]["quantity"]
            list.add(item, -1)
            if number <= 0:
                raise OutOfError(item)
        except (KeyError, OutOfError) as e:
            print(f"You have no {item} remaining!")
            return
        except IsFixture as e: pass

    # Reflect the class
        try:
            instance = getattr(item_file, item)()
        except:
            print(f"{item} doesn't seem to be a valid object.")
            return

    # To or not to remove; that is the question
        if instance.consumable and number <= 0:
            try:
                list.remove(item)
            except: pass
      # File now removes at the Spec level
      # os.remove(
      #  item_file.__file__
      # )

    # Return the result or inbuilt use method
        if type(instance).__str__ is not object.__str__:
            instance.use(**instance.actions)
            print(f"{instance}")
        else:
            return instance.use(**instance.actions)

# Create instances to use as shorthand
# I thought this was a bad idea, but this
# is actually how the random module works

# https://github.com/python/cpython/blob/main/Lib/random.py

list = List()
items = Items(list)