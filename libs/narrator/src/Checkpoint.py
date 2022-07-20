import os

from .Path import *

def exists(filepaths: list) -> bool:
  for file in filepaths:
    if not os.path.exists(file):
      return False
  return True
