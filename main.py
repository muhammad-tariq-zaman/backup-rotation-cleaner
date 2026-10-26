"""Backup rotation cleaner: keep newest N backups per prefix, dry-run default."""
import argparse
import os
import sys


def plan(directory, prefix, keep=3):
    matches = []
    for name in sorted(os.listdir(directory)):
        path = os.path.join(directory, name)
        if os.path.isfile(path) and name.startswith(prefix):
            matches.append((os.path.getmtime(path), path))
    matches.sort(reverse=True)
    return {"keep": [p for _t, p in matches[:keep]],
            "delete": [p for _t, p in matches[keep:]]}


def main(argv=None):
    p = argparse.ArgumentParser(description="Keep newest N backups per prefix.")
    p.add_argument("--dir", required=True)
    p.add_argument("--prefix", required=True)
    p.add_argument("--keep", type=int, default=3)
    p.add_argument("--apply", action="store_true")
    args = p.parse_args(argv)
    r = plan(args.dir, args.prefix, args.keep)
    for path in r["keep"]:
        print(f"keep: {path}")
    for path in r["delete"]:
        if args.apply:
            os.remove(path)
            print(f"deleted: {path}")
        else:
            print(f"would-delete: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
