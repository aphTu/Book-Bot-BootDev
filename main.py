from stats import *
import sys

def main():
  if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    exit(1)
  
  text = get_book_text(sys.argv[1])
  header_print(sys.argv[1])
  print(f"Found {count_words(text)} total words") 
  characters = count_characters(text)
  print("--------- Character Count -------")
  print_report(sorting_dictionary(characters))

main()