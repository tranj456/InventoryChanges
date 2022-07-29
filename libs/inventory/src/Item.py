import os
import sys
import inspect

from .Config import *
from .Template import Template

sys.path.append(
  os.path.expanduser(f'{Config.values["INV_PATH"]}')
)

class ItemSpec:

  consumable = True

  def use(self) -> None:
    print(f"You try the {self.__module__}, but it doesn't do anything.")
    return None

class FixtureSpec(ItemSpec):

  consumable = False

  def __init__(self):
    pass

class Factory:

  def __init__(self, name):
    self.name = name.title().replace(" ","")
    self.file = '\n\n'.join([
      "from inventory.Item import ItemSpec",
      inspect.getsource(Template)
    ])
    self.make()

  def make(self):
    self.file = self.file.replace(
      "Template", 
      f"{self.name}(ItemSpec)"
    )
    with open(f"{self.name}.py", "w") as fh:
      fh.write(self.file)

class OutOfError(Exception):

  def __init__(self, item:str, *args):
    super().__init__(args)

class IsFixture(Exception):

  def __init__(self, item:str, *args):
    super().__init__(args)
