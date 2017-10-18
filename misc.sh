
function set_action { # $@
  if [[ -z $@ ]]; then
    action="git status"
  else
    action=$@
  fi
}

################################################################################

function walk { # $@
  set_action $@
  caller_path=$(pwd)
  cd ~/github/
  for d in $(find -mindepth 1 -maxdepth 1); do
    echo $d
    cd $d
    $action
    echo =======================================================================
    cd ..
  done
  cd $caller_path
}

################################################################################

clear
walk $@
