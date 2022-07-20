import narrator

n = narrator.Narrator()
n.narrate()

q = narrator.Question(
  {
    "question": "Skip, er nah",
    "responses": [
      {"choice": "skip", "outcome": 2},
      {"choice": "nah", "outcome": 1}
    ]
  }
)

while True:
  ask = input(q.prompt)
  if ask in q.responses:
    n.path.change_path(int(q.responses[ask]))
    break
  print("Not an option; try again")

n.narrate()
