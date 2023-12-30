import os, sys, math
from typing import List
from itertools import groupby


def toBoard(letters: str, boardSize: int) -> List[List[str]]:
    board = []
    for i in range(0, len(letters), boardSize):
        board.append(list(letters[i:i + boardSize]))
    
    print("\n")
    for row in board:
        print("".join(" " * (11 - boardSize)) + "  ".join([letter.upper() if letter.isalpha() else ' ' for letter in row]))
        print()
    return board


def findWords(board: List[List[str]], words: List[str], boardSize: int) -> List[str]:
    
    wordKey = "$"
    root = {}
    
    def dfs(r, c, parent):
        ch = board[r][c]
        board[r][c] = "."
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
        if len(word) < 3 or len(word) > (boardSize ** 2):
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


def winGame(boardString: str, boardSize: int):
    board = toBoard(boardString, boardSize)
    foundWords = findWords(board, dictionary, boardSize)
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

def readFromFile(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))
dictionaryFilePath = os.path.join(scriptDir, "dictionary.txt")
dictionary = readFromFile(dictionaryFilePath)

def main():
    
    boardSize = input("\nenter the no. of rows/columns (1-10), or q to exit: ").lower()
    
    if boardSize == "q":
        print()
        exit()
    
    while not boardSize.isdigit() or int(boardSize) < 1 or int(boardSize) > 10:
        print("\nthe board size must be a number between 1 and 10. try again.")
        
        boardSize = input("\nenter the no. of rows/columns (1-10), or q to exit: ").lower()
        
        if boardSize == "q":
            print()
            exit()
    
    boardSize = int(boardSize)
    letterCount = boardSize ** 2
        
    boardString = input("\nenter the board letters with a period for gaps (row by row, left to right), or q to exit: ").lower()

    if boardString == "q":
        print()
        exit()

    while len(boardString) != letterCount or not all(ch.isalpha() or ch == '.' for ch in boardString):
        print(f"\nthe board must be {letterCount} characters long and contain only letters. try again.")
        
        boardString = input("\nenter the board: ").lower()
        
        if boardString == "q":
            print()
            exit()

    winGame(boardString, boardSize)
    
    done = input("enter any character to play again, or q to exit: ").lower()
    
    if done == "q":
        print()
        exit()
    
    main()

main()

