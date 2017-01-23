@echo off
goto starting

:looping
  set subm=git submodule update --remote
  set comm=git status
  for /d %%d in (*) do (
    echo %%d
    cd %%d
    %comm%
    cd ..
    echo ===================================================
  )
  goto ending

:starting
  cls
  set currDir=%cd%
  cd /d D:/repos/
  goto looping

:ending
  cd %currDir%
