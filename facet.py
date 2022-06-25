import pathlib
import os
import common

class Facet:
    BACKUP_SUFFIX = '.dotfile.old'
    def __init__(self, id, name, src, target) -> None:
        self.id = id
        self.name = name
        self.src = src
        self.target = target
        self.backup = f'{target}{Facet.BACKUP_SUFFIX}'

    def __str__(self) -> str:
        pass

    def has_backup(self) -> bool:
        return pathlib.Path(self.backup).is_file()

HOME_DIR = pathlib.Path.home()
FACETS = []

def setup(dotfiles):
    global FACETS
    dotfiles_dir = pathlib.Path(dotfiles)
    FACETS = [
        Facet(0, 'Neovim', dotfiles_dir / 'nvim/init.lua', HOME_DIR / '.config/nvim/init.lua'),
    ]

def install(f: Facet):
    facet = f.name
    src = f.src
    target = f.target
    id = f.id
    backup = f.backup
   
    if target.is_file():
        if target.resolve() == src.resolve():
            print(f'{id}\t{facet}\t{target} already linked to {src} - skipping')
            return
        print(f'{id}\t{facet}\t{target} exists - saving old contents (overriding any older ones)')
        common.copy_file_into_file(target, backup)
        os.unlink(target)

    os.symlink(src, target)
    print(f'{id}\t{facet}\t{target} is now linked to {src}')

def restore(f):
    facet = f.name
    target = f.target
    id = f.id
    backup = f.backup

    if not f.has_backup():
        print(f'{id}\t{facet}\tno backup exists - skipping')
        return
    
    if target.is_file():
        print(f'{id}\t{facet}\t{target} exists - deleting contents')
        os.unlink(target)
    
    common.copy_file_into_file(backup, target)
    os.unlink(backup)
    print(f'{id}\t{facet}\t{backup} is now restored to {target}')

def clean(f):
    facet = f.name
    target = f.target
    id = f.id
    backup = f.backup

    if not f.has_backup():
        print(f'{id}\t{facet}\t{backup} does not exist - skipping')
    else:
        os.unlink(backup)
        print(f'{id}\t{facet}\t{backup} is now deleted')

    if not target.is_file():
        print(f'{id}\t{facet}\t{backup} does not exist - skipping')
    else:
        os.unlink(target)
        print(f'{id}\t{facet}\t{target} is now deleted')


def run_for_ids(func, ids=[]):
    if len(ids) == 0:
        for f in FACETS:
            func(f)
    else:
        for i in ids:
            try:
                func(FACETS[int(i)])
            except:
                print(f'{i} is not a valid facet id - ignoring')

def list():
    for f in FACETS:
        print(f'{f.id}\t{f.name}\t{f.src} > {f.target}\t{"NB" if not f.has_backup() else "B"}')