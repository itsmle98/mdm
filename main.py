#!/usr/bin/python3
import argparse
import facet

def main():
    parser = argparse.ArgumentParser(description='Manages dotfiles.')
    parser.add_argument('-d', '--dotfiles', nargs=1, help='the directory for your dotfiles', required=True)
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument('-l', '--list', action='store_true', help='list all facets and whether they have a backup')
    actions.add_argument('-i', '--install', nargs='*', help='install facets by id (if none supplied, install all of them)')
    actions.add_argument('-r', '--restore', nargs='*', help='restore facet backups by id (if none supplied, restore all of them)')
    actions.add_argument('-c', '--clean', nargs='*', help='delete facet and backups by id (if none supplied, delete all of them)')
    args = parser.parse_args()
    
    facet.setup(args.dotfiles[0])
    if args.list == True:
        facet.list()
    elif args.install is not None:
        facet.run_for_ids(facet.install, args.install)
    elif args.restore is not None:
        facet.run_for_ids(facet.restore, args.restore)
    elif args.clean is not None:
        facet.run_for_ids(facet.clean, args.clean)


if __name__ == '__main__':
    main()
