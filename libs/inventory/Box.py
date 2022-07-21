import inventory

class Box(inventory.Item.ItemSpec):

  def __init__(self):
    super().__init__()
    self.consumable = False

  def use(self):
    print("USED!")

if __name__ == "__main__":
  box = Box()
