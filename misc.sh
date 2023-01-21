#!/bin/bash

################################################################################

function execute_ls {
  if [[ -d ~/Pictures/Screenshots ]]; then
    rmdir ~/Pictures/Screenshots
  fi
  tree ~ --dirsfirst -L 2 -I 'bin|code|Documents|Music|Public|snap|Templates|Videos|Zotero'
}

################################################################################

function execute_git {
  for d in $(find ~/code -mindepth 1 -maxdepth 1 | sort); do
    echo =======================================================================
    echo $d
    cd $d
    if [[ -z $@ ]]; then
      git status
    else
      $@
    fi
  done
}

################################################################################

function walk {
  if [[ $@ == l ]]; then
    execute_ls
  else
    execute_git $@
  fi
}

################################################################################

# clear
walk $@
