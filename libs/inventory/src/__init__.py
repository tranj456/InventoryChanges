import os
import sys
import json

from .Config import *
from .Item import *
from .Inventory import *

args = sys.argv[1:]
path = Config.values["INV_PATH"]

if len(args) > 1:
  print("Acquire only one item at a time!")
  exit()

if args:
  import importlib
  import shutil

  file = args[0]

  # TODO: Migrate the below to separate functions
  #       to test each condition separately and raise
  #       specific errors

  try:
    print(args[0])
    name, ext = file.split(".")
    if not ext == "py":
      raise
    importlib.import_module(name)
  except Exception as e:
    print(e)
    print("Not a valid item file.")
    exit()

  try:
    obj_path = os.path.expanduser(
      f'{Config.values["INV_PATH"]}/{file}'
    )
    shutil.copy(file, obj_path)
  except:
    print(f"Error acquiring {file}.")

  try:
    list = Inventory.list
    list.add(name)
  except:
    exit()
