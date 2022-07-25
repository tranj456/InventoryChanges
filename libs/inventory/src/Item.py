import os
import sys

from .Config import *

sys.path.append(
  os.path.expanduser(f'{Config.values["INV_PATH"]}')
)

class ItemSpec:

  consumable = True

  def use(self) -> None:
    print("You try it, but it doesn't do anything.")
    return None

class FixtureSpec(ItemSpec):

  consumable = False

  def __init__(self):
    pass

class OutOfError(Exception):

  def __init__(self, item:str, *args):
    super().__init__(args)

class IsFixture(Exception):

  def __init__(self, item:str, *args):
    super().__init__(args)
