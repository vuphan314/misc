function loop {
  cd ..
  for d in $(find -mindepth 1 -maxdepth 1); do
    cd $d
    git status
    echo ===================================================
    cd ..
  done
}

loop
