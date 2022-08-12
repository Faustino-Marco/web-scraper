import requests
from bs4 import BeautifulSoup
import pandas as pd

# parse raw html by parsing it
# install beautifulsoup
# import beautiful soup from bs4

# step 1: go get content
URL = "https://en.wikipedia.org/wiki/Table_football"

##############################################
# page = requests.get(URL)
##############################################

# print(page.content)
# print(page.content)

# Create "soup" (name by convention) aka parsed content
# 2nd arg is type of parsing (html)
##############################################
# soup = BeautifulSoup(page.content, "html.parser")
##############################################
# test with `print(soup)`


# isolate target content by class
##############################################
# results = soup.find(class_="mw-parser-output")
##############################################

# test with a print
# print(results)

# different but still difficult to interpret
# try bs4 `prettify` method

##############################################
# cleanedup_results = results.prettify()
##############################################


# print(cleanedup_results)

# perform `find()` on ^RESULTS^ (not prettified)
# possibly find_all()

##############################################
# paragraphs = results.find_all("p")
##############################################

# print(paragraphs)
# print(type(paragraphs))

### Anchors example ### 
# results has a find_all shortcut!!

##############################################
# anchors = results("a")
##############################################

# print(anchors)

# write a loop to get each p
# for anchor in anchors:
  # print(anchor)

# ResultSets are iterable and can be used in comps
# use a comprehension

##############################################
# links = [anchor["href"] for anchor in anchors]
##############################################



# go to a link
# python_link = links[1]
# python_url = URL + python_link
# print("\n", python_url)

# create new `soup` for link to follow and operate there
# python_response = requests.get(python_url)
# python_soup = BeautifulSoup(python_response.content, "html.parser")
# print(python_soup)

### end anchors example ### 


def get_citations_needed_count(url):
  """
  Takes in a url string and returns an integer.

  According to the chrome tools inspection, the tag for 'citation needed' links on this page is:

  `<a href="/wiki/Wikipedia:Citation needed" title="Wikipedia:Citation needed">`

  Dig down and find these in the page and populate a list with the parent <p> tag content.

  Return the length of the list.

  Notes:
  - It looks like the class for all the content we want to check in the body of this page is in the tag called:

  `<div class="mw-parser-output">`

  Start by digging for this "mw-parser-output" tag and then finding the links we're looking for...

  `<a href="/wiki/Wikipedia:Citation needed" title="Wikipedia:Citation needed">`

  ...by finding all the tags and checking if they match our target tag and counting the matches.

  *** DON'T FORGET `_` BETWEEN WORDS IN HREF TAG STRING

  """
  target_parent_class = "mw-parser-output"

  # don't forget '_' in spaces for tag
  target_href = '/wiki/Wikipedia:Citation_needed'

  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")

  # Find the target parent class
  results = soup.find(class_=target_parent_class)

  # Find all the target tags within the parent class
  anchors = results("a")

  # Put target tags into a list
  links = [anchor["href"] for anchor in anchors]
  # print(links)

  # confirm whether or not target tag is in results
  # print(target_href in links)

  # Frequency Check (geeksforgeeks.org; see README.md)
  # df1 = pd.Series(links).value_counts().sort_index().reset_index().reset_index(drop=True)

  df1 = pd.Series(links).value_counts()

  # df1.columns = ['Link', 'Frequency']

  # Find Frequency of target href
  print(df1[target_href])

  # print(f"The list frequency of elements is :\n {df1.to_string(index=True)}" )
  
  # Find Index of target href
  # print(df1[df1['Link'] == target_href])

  # print(df1['Frequency']['Link'][target_href])

  # return 'frequency' value at discovered index
  num_citations_needed = df1[target_href]

  return f"The number of citations needed is {num_citations_needed}."



# print(get_citations_needed_count(URL))


def get_citations_needed_report(url):
  """
  Takes in a url string and returns a report string.

  The string should be formatted with each citation listed in the order found.

  For Example:

  The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.

  The Mexica people arrived in the Valley of Mexico in 1248 AD. They had migrated from the deserts north of the Rio Grande[citation needed] over a period traditionally said to have been 100 years. They may have thought of themselves as the heirs to the prestigious civilizations that had preceded them.[citation needed] What the Aztec initially lacked in political power, they made up for with ambition and military skill. In 1325, they established the biggest city in the world at that time, Tenochtitlan.

  etc.
  """
  target_href = '/wiki/Wikipedia:Citation_needed' 

  para_link = URL
  citations_response = requests.get(para_link)

  para_soup = BeautifulSoup(citations_response.content, "html.parser")
  para = para_soup("p")
  for p in para:
    if target_href in p.prettify():
      return p.text
  # list_items = para.select("p")
  


print(get_citations_needed_report(URL))

# STRETCH

# def get_citations_needed_by_section(url):
#   """
#   Organize the needed citations by section (i.e. the parent heading tag).
#   """
#   pass