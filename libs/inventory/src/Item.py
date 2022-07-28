import os
import sys
import inspect

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

class Factory:

  def __init__(self, name):
    self.name = name.title().replace(" ","")
    self.imports = "from inventory.Item import ItemSpec"
    self.globals = "consumable = True"
    self.constructor = self.make()
    self.methods = inspect.getsource(ItemSpec.use)
    self.assemble()

  def make(self) -> str:
    code = inspect.getsource(Template)
    return code.replace("Template", self.name)

  def assemble(self):
    elements = [
      self.imports,
      self.globals,
      self.constructor,
      self.methods
    ]
    with open(f"{self.name}.py", "w") as fh:
      for elem in elements:
        fh.write(f"{elem}\n\n")

class Template(ItemSpec):

  def __init__(self):
    super().__init__()

class OutOfError(Exception):

  def __init__(self, item:str, *args):
    super().__init__(args)

class IsFixture(Exception):

  def __init__(self, item:str, *args):
    super().__init__(args)
