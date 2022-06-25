# mle98's dotfiles manager

## What

This is a set of python scripts to manage configuration files (commonly referred to as dotfiles) across different machines.

## How

The fundamental problem is how to associate/dessociate a local version of a configuration file to an upstream one while minimizing accidental loss of data.

In a user's system there will be many programs/apps/scripts/etc - these are referred to as 'facets' of the user's configuration. At a high level, MDM addresses the fundamental problem by managing symbolic links from a source to a destination, as well as supporting backups for files that pointed to no target or an incorrect one, for each facet specified by the user.

Once a file is symlinked, then Git (or any other VCS) can be used to track changes across different versions. Backups fill the gap for files that are not symlinks to anything (i.e "manual configs") or point to an incorrect target (i.e updates to the facet or other attempts at managing dotfiles).

See the code for more details.

## Usage

Add facets to `FACETS` global array in `facet.py` and use MDM through the CLI. Once symlinked/installed, manage through your VCS.
