#!/usr/bin/env python3
import os
import json

def build_index(root_dir):
    index = {}
    # each subfolder of root_dir is an author/style
    for author in os.listdir(root_dir):
        author_path = os.path.join(root_dir, author)
        if not os.path.isdir(author_path):
            continue

        # inside each author, each subfolder is a character
        for char in os.listdir(author_path):
            char_path = os.path.join(author_path, char)
            if not os.path.isdir(char_path):
                continue

            # list all files in that character folder
            files = [
                fname for fname in os.listdir(char_path)
                if os.path.isfile(os.path.join(char_path, fname))
            ]
            if not files:
                continue

            # build nested dict: index[char][author] = list_of_filenames
            index.setdefault(char, {})[author] = files

    return index

if __name__ == "__main__":
    # assume this script lives at the root of your folder tree
    ROOT = os.path.dirname(os.path.abspath(__file__))
    idx = build_index(ROOT)

    out_path = os.path.join(ROOT, "index.json")
    with open(out_path, "w", encoding="utf-8") as fp:
        # ensure_ascii=False preserves Chinese chars in the JSON keys
        json.dump(idx, fp, ensure_ascii=False, indent=2)

    print(f"Wrote index for {len(idx)} characters to {out_path}")
