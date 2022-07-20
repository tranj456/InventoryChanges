from dotenv import dotenv_values

class Config:

  values = dotenv_values('.env')
