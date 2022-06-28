import requests

def grab_file(raw_path: str, file_name: str):
    raw = requests.get(raw_path)
    text = str(raw.text)
    file = open(file_name, "x")
    file.write(text)
    file.close()