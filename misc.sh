LS="l"

################################################################################

## receives $@
## sets $action
function set_action {
  if [[ $@ == $LS ]]; then
    action=$LS
  elif [[ -z $@ ]]; then
    action="git status"
  else
    action=$@
  fi
}

################################################################################

function execute_ls {
  cd
  rm -rf Documents/ViberDownloads
  rm -f GlobalModel.txt
  tree -L 2 --dirsfirst
}

################################################################################

## receives $action
function execute_git {
  cd $HOME/code/
  for d in $(find -mindepth 1 -maxdepth 1); do
    echo $d
    cd $d
    $action
    echo =======================================================================
    cd ..
  done
}

################################################################################

## receives $@
## sets $action
function walk {
  caller_path=$(pwd)
  set_action $@
  if [[ $action == $LS ]]; then
    execute_ls
  else
    execute_git
  fi
  cd $caller_path
}

################################################################################

clear
walk $@
