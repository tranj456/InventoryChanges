import narrator

n = narrator.Narrator()

n.narrate()

q = narrator.Question(
  {
    "question": "Skip, er nah",
    "responses": [
      {"choice": "skip", "outcome": 2},
      {"choice": "nah", "outcome": 1.0}
    ]
  }
)

while True:
  ask = input(q.prompt)
  if ask in q.responses:
    path = q.responses[ask].outcome
    n.path.change(path)
    break
  print("Not an option; try again")

#n.narrate(all=True)
n.narrate()
