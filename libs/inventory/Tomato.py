from inventory.Item import ItemSpec

class Tomato(ItemSpec):

  consumable = True

  def __init__(self):
    super().__init__()
