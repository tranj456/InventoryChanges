class Question:

  def __init__(self, prompt: dict):
    self.responses = {}
    self.prompt = prompt["question"]
    for response in prompt["responses"]:
      self.set_opt(response)
    options = [self.responses[val].choice for val in self.responses]
    self.prompt += f" ({'/'.join(options)}): "

  def is_key(self, char: str) -> bool:
    if char in list(self.responses.keys()):
      return True
    return False

  def set_opt(self, option: dict) -> dict:
    choice = option["choice"]
    for letter in choice:
      if not self.is_key(letter):
        opt = Option(letter, option)
        self.responses[letter] = opt
        break

class Option:

  def __init__(self, key: str, option: dict):
    self.choice = option["choice"].replace(
      key,
      f"[{key.upper()}]",
      1
    )
    self.outcome = option["outcome"]

