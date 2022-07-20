class Path:

  def __init__(self, path):
    self.scenes = path

  def next_scene(self, number):
    return self.scenes[number]
