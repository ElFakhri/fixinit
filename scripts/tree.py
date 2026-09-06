#!/usr/bin/env python3
import os
import sys

EXCLUDE = {'node_modules', 'venv', '.venv', '.git', '__pycache__'}
MAX_DEPTH = 6

def walk(dirpath='.', prefix='', depth=0):
    try:
        entries = sorted(os.listdir(dirpath))
    except Exception:
        return
    entries = [e for e in entries if not e.startswith('.')]
    entries = [e for e in entries if e not in EXCLUDE]
    for i, name in enumerate(entries):
        path = os.path.join(dirpath, name)
        connector = '└── ' if i == len(entries)-1 else '├── '
        print(prefix + connector + name)
        if os.path.isdir(path) and depth+1 < MAX_DEPTH:
            ext = '    ' if i == len(entries)-1 else '│   '
            walk(path, prefix + ext, depth+1)

if __name__ == '__main__':
    start = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(start)
    walk(start)
