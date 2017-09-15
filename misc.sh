function set_cmd { # $@
  if [[ -z $@ ]]; then
    cmd="git status"
  else
    cmd=$@
  fi
}

################################################################################

function loop { # $@
  set_cmd $@
  cd ..
  for d in $(find -mindepth 1 -maxdepth 1); do
    echo $d
    cd $d
    $cmd
    echo =======================================================================
    cd ..
  done
}

################################################################################

clear
loop $@
