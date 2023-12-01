# word hunter

this is a simple, terminal-based program that automates finding (almost) all the words in the imessage game 'word hunt'.

note: i do not have access to the exact dictionary that gamepigeon use, so the generated words may not always be valid in-game.

## instructions

## prerequisites


first, if you haven't installed python3 before, do so at this link:

https://www.python.org/downloads/

this will be necessary to run the program locally.

then, you have the following two options to download the files:

## 1. download zip (recommended)


click on the green 'code' button on this repo.


<img width="335" alt="image" src="https://github.com/vkayy/word-hunter/assets/62311142/3f677cae-b8a6-4352-93d6-7bae332ab337">


then, click 'download zip'.


<img width="388" alt="image" src="https://github.com/vkayy/word-hunter/assets/62311142/bc86b565-1f9e-4639-aeb3-97884b6a3d24">


then, unzip the folder locally, and the files should be downloaded.


## 2. clone repo with git (can be faster)


if you haven't installed git, do so at this link:

https://git-scm.com/downloads

then, enter this command in your terminal/command prompt:

```
git clone https://github.com/vkayy/word-hunter.git
```

this will create your own local repo with the same code as mine.


## using the program


to run the program, you can simply right-click on it in your finder/file library and open it with the python launcher.

you will be asked to input the size of the board, and the letters in the board.


as an example, if this was your board,

<img width="388" alt="image" src="https://github.com/vkayy/word-hunter/assets/62311142/5f545954-ded8-4869-95f2-a034562f8bb8">

you would enter a size of `4`, and the letters `OATRIHPSHTNRENEI`.

note that the letter input is case-insensitive, so you could also enter `oaTrIhPsHtnReNei` (but why?).


following this, you will have a basic display of your board output, followed by the possible words in ascending length.

then, you will be prompted to either quit or enter another board.

note: as mentioned earlier, some generated words may not be valid in-game, and some words may be missing. feel free to add or remove words from the dictionary text file as you please, but ensure that the same format, e.g.:

```
cheese
burger
python
```

rather than:

```
cheese, burger, python
```

or:

```
cheese,
burger,
python,
```

## languages, frameworks and libraries used

- python
- os, sys
- itertools

## motives

my girlfriend and i are very competitive with word hunt (although, i beat her all the time), and this is the harvest of that situation.
