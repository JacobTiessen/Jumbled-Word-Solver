# Unscrambler - checks jumbled words against the dictionary
# usage: python unscramble.py LNDA MDNOIDA RARCY

import argparse
import sys
from collections import defaultdict

from wordfreq import top_n_list

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def key(word):
    # sort the letters so LNDA and LAND both become adln
    return "".join(sorted(word.lower()))


def load_dictionary(size, wordlist_path=None):
    if wordlist_path:
        with open(wordlist_path, encoding="utf-8") as f:
            words = [line.strip().lower() for line in f]
    else:
        # wordfreq lists words from most to least common
        words = top_n_list("en", size)

    table = defaultdict(list)
    for w in words:
        if w.isalpha() and len(w) >= 2:
            table[key(w)].append(w)
    return table


def exact(jumble, table):
    return table.get(key(jumble), [])


def one_off(jumble, table):
    # words with one extra letter or one missing letter
    results = []
    letters = jumble.lower()

    # try taking out each letter
    for c in sorted(set(letters)):
        shorter = letters.replace(c, "", 1)
        for w in table.get(key(shorter), []):
            results.append(f"{w} (-{c.upper()})")

    # try adding each letter
    for c in ALPHABET:
        for w in table.get(key(letters + c), []):
            results.append(f"{w} (+{c.upper()})")

    return results


def main():
    parser = argparse.ArgumentParser(description="Unscramble jumbled words using an English dictionary.")
    parser.add_argument("jumbles", nargs="*", help="jumbled words (or use --file)")
    parser.add_argument("-f", "--file", help="text file with one jumble per line")
    parser.add_argument("-n", "--max", type=int, default=5, help="max answers to show per jumble (default 5)")
    parser.add_argument("--size", type=int, default=100000, help="how many dictionary words to load (default 100000)")
    parser.add_argument("--wordlist", help="use your own word list file instead (one word per line)")
    parser.add_argument("--fuzzy", action="store_true", help="also show words one letter more/less")
    args = parser.parse_args()

    jumbles = list(args.jumbles)
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            jumbles += [line.strip() for line in f if line.strip()]
    if not jumbles:
        parser.print_help()
        sys.exit(1)

    table = load_dictionary(args.size, args.wordlist)
    width = max(len(j) for j in jumbles) + 2

    for j in jumbles:
        clean = "".join(ch for ch in j if ch.isalpha())
        found = exact(clean, table)[: args.max]
        print(f"{j:<{width}}-> {', '.join(found) if found else '(no match)'}")
        if args.fuzzy:
            near = one_off(clean, table)[: args.max]
            if near:
                print(f"{'':<{width}}   one off: {', '.join(near)}")


if __name__ == "__main__":
    main()
