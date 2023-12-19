import os, sys, math
from typing import List
from itertools import groupby

def readFromFile(file_path: str) -> List[str]:
  with open(file_path, 'r') as file:
    words = file.read().splitlines()
  return words

scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))
dictionaryFilePath = os.path.join(scriptDir, "dictionary.txt")
dictionary = set(readFromFile(dictionaryFilePath))

def findWords(letters: str):
  words = set()
  def backtrack(cur, rem):
    if len(cur) > 2 and ''.join(cur) in (dictionary - words):
      words.add(''.join(cur))
    if not rem:
      return
    for letter in rem:
      backtrack(cur + [letter], [ch for ch in rem if ch != letter])
  backtrack([], letters)
  return words

def winGame(letters: str):
  foundWords = findWords(letters)
  groupedWords = [list(group) for _, group in groupby(sorted(foundWords, key=len), len)]
    
  print()
  
  if not groupedWords:
    print("couldn't find any words; you probably made a typo.\n")
    main()
  else:
    for group in groupedWords:
      if len(group) > 0:
        letters = len(group[0])
        print(f"----- {letters} letter words -----\n")
        for word in group:
          print(''.join([" "] * math.floor((26 - letters) / 2)) + word.upper()) 
        print()

def main():
    letters = input("\nenter the six letters, or q to exit: ").lower()
    
    if letters == "q":
        print()
        exit()
    
    while len(letters) != 6 or not letters.isalpha():
        print("\there are only six characters, and they must be letters. try again.")
        
        letters = input("\nenter the six letters, or q to exit: ").lower()
        
        if letters == "q":
          print()
          exit()

    winGame(letters)
    
    done = input("enter any character to play again, or q to exit: ").lower()
    
    if done == "q":
        print()
        exit()
    
    main()

main()