def get_book_text(file_path):
  text = ""
  with open(file_path) as f:
    text = f.read()
  return text

def count_words(text):
  text_split = text.split()
  counter = 0
  for word in text_split:
    counter+=1
  return counter

def count_characters(text):
  text_split = text.split()
  counter = {}
  for word in text_split:
    for character in word:
      if character.lower() in counter:
        counter[character.lower()]+= 1
      else:
        counter[character.lower()]= 1
  return counter

def sort_on(items):
  return items["num"]
def sorting_dictionary(_dict):
  sorted_dict = []
  for k in _dict:
    sorted_dict.append({"char": k, "num": _dict[k]})
    
  sorted_dict.sort(reverse=True,key=sort_on)
  return sorted_dict

def header_print(file_path):
  print("=" * 12 + " BOOKBOT " + "=" * 12)
  print(f"Analyzing book found at {file_path}")
  print("----------- Word Count ----------")

def print_report(_list):
  for i in range(0,len(_list)):
    if(_list[i]["char"].isalpha()):
      print(f"{_list[i]["char"]}: {_list[i]["num"]}")
    else: 
      continue