function loop {
  clear
  cd ..
  for d in $(find -mindepth 1 -maxdepth 1); do
    echo $d
    cd $d
    git status
    echo ===================================================
    cd ..
  done
}

loop