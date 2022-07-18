import os
import sys

sys.path.append(
  os.path.expanduser('~/.inv/')
)

class Spec:

  consumable = True

  def use(self) -> None:
    print("You try it, but it doesn't do anything.")
    return None

class OutOfError(Exception):

  def __init__(self, item:str, *args):
    super().__init__(args)
