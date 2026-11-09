# Jumbled-Word-Solver
Imagine you have many jumbled words (Ex: LNDA, MDNOIDA, RARCY) and you wanted them to be looked at against the English dictionary. That is what this code will do. (Ex: LAND, DIAMOND, CARRY). (This can be used for puzzles if you don't want to spend an absurd amount of time cross referencing against the dictionary. 
## Setup
You need Python and the wordfreq library. Install it with:
```
pip install wordfreq
```

## How to use it
Put your jumbled words after the file name:
```
python unscramble.py LNDA MDNOIDA RARCY
```

You can also put them in a text file (one word per line):
```
python unscramble.py -f words.txt
```

If you want it to also find words that are one letter off, add --fuzzy:
```
python unscramble.py GIMNNOWY --fuzzy
```
That one gives wyoming (-N), because the N is an extra letter.

## How it works
It sorts the letters of every word alphabetically, so LAND and LNDA both turn into ADLN. Then it just matches them up. More common words show up first.

## ! MOST IMPORTANT !
Enjoy! Puzzles have never been easier... until the next code comes along..
