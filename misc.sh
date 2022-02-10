#!/bin/bash

################################################################################

LS=l

################################################################################

## receives $@
## sets $action
function set_action {
  if [[ -z $@ ]]; then
    action="git status --short"
  else
    action=$@
  fi
}

################################################################################

function execute_ls {
  tree ~ -L 2 --dirsfirst -I 'bin|CiscoSpark|code|snap|Zotero'
}

################################################################################

## receives $action
function execute_git {
  for d in $(find ~/code -mindepth 1 -maxdepth 1 | sort); do
    echo $d
    cd $d
    $action
    echo =======================================================================
  done
}

################################################################################

## receives $@
## sets $action
function walk {
  set_action $@
  if [[ $action == $LS ]]; then
    execute_ls
  else
    execute_git
  fi
}

################################################################################

clear
walk $@
