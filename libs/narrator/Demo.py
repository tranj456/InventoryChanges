import narrator

n = narrator.Narrator()

n.narrate()

q = narrator.Question(
  {
    "question": "Skip, meh, er nah",
    "responses": [
      {"choice": "skip", "outcome": 2},
      {"choice": "meh", "outcome": 0},
      {"choice": "nah", "outcome": 1.0}
    ]
  }
)

n.path.change(q.ask())

n.narrate()

q = narrator.YesNoQuestion(
  {"question":"Yes or no?","responses":[0,1]}
)

n.path.change(q.ask())

n.narrate(all=True)
