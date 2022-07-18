import sys

from .Item import *
from .Inventory import *

args = sys.argv[1:]

if args:
  import importlib
  import shutil

  file = args[0]

  # TODO: Migrate the below to separate functions
  #       to test each condition separately and raise
  #       specific errors

  try:
    name, ext = file.split(".")
    if not ext == "py":
      raise
    importlib.import_module(name)
  except:
    print("Not a Python file.")
    exit()

  shutil.copy(file, f"~/.inv/{file}")
