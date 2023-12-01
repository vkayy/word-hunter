from typing import List
from itertools import groupby
import os, math


def toBoard(letters: str) -> List[List[str]]:
    board = []
    for i in range(0, len(letters), 4):
        board.append(list(letters[i:i + 4]))
    return board


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    
    wordKey = "$"
    root = {}
    
    def dfs(r, c, parent):
        ch = board[r][c]
        board[r][c] = "#"
        child = parent[ch]
        
        if word := child.pop(wordKey, False):
            matches.append(word)
        
        for rr, cc in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c), (r + 1, c + 1), (r + 1, c - 1), (r - 1, c + 1), (r - 1, c - 1)]:
            if not 0 <= rr < rows or not 0 <= cc < cols:
                continue
            if not board[rr][cc] in child:
                continue
            dfs(rr, cc, child)
        
        board[r][c] = ch
        
        if not child:
            parent.pop(ch)
    
    for word in words:
        if len(word) < 4 or len(word) > 15:
            continue
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node[wordKey] = word
    
    rows, cols = len(board), len(board[0])
    matches = []
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] in root:
                dfs(r, c, root)
    
    return matches


def readFromFile(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words


def beatElena(input: str):
    board = toBoard(input)
    foundWords = findWords(board, dictionary)
    groupedWords = [list(group) for _, group in groupby(sorted(foundWords, key=len), len)]
    
    print()
    
    if not groupedWords:
        print("couldn't find any words; you prolly made a typo.")
        
    else:
        for group in groupedWords:
            if len(group) > 0:
                letters = len(group[0])
                print(f"----- {letters} letter words -----\n")
                for word in group:
                    print(''.join([" "] * math.floor((26 - letters) / 2)) + word) 
                print()


dictionary = readFromFile(os.environ["DICTIONARY_FILE"])

boardString = input("enter the board: ")

beatElena(boardString)

