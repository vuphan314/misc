cmd="git status"

############################################################

function loop {
  cd ..
  for d in $(find -mindepth 1 -maxdepth 1); do
    echo $d
    cd $d
    $cmd
    echo ===================================================
    cd ..
  done
}

############################################################

# reset
loop
