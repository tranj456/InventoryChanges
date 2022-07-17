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

class items:

  import types

  def __init__(self, list):
    self.list = list.list()
    print(self.list)

  @staticmethod
  def use(item: str):
    # TODO: Search inventory dictionary instead
    import importlib
    object = importlib.import_module(f"{item}")
    instance = getattr(object, item)()
    if(instance.consumable):
      os.remove(
        os.path.expanduser(
          f'~/.inv/{item}.py'
        )
      )
    return instance.use()
