import requests

URL = "https://en.wikipedia.org/wiki/Table_football"
page = requests.get(URL)

def get_citations_needed_count(url):
  """
  Takes in a url string and returns an integer.
  """
  pass

def get_citations_needed_report(url):
  """
  Takes in a url string and returns a report string.

  The string should be formatted with each citation listed in the order found.

  For Example:

  The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.

  The Mexica people arrived in the Valley of Mexico in 1248 AD. They had migrated from the deserts north of the Rio Grande[citation needed] over a period traditionally said to have been 100 years. They may have thought of themselves as the heirs to the prestigious civilizations that had preceded them.[citation needed] What the Aztec initially lacked in political power, they made up for with ambition and military skill. In 1325, they established the biggest city in the world at that time, Tenochtitlan.

  etc.
  """
  pass

def get_citations_needed_by_section(url):
  """
  Organize the needed citations by section (i.e. the parent heading tag).
  """
  pass