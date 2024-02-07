import json
from urllib.request import urlopen

def object_from_json_url(url):
  with urlopen(url) as in_file:
    return json.load(in_file)
