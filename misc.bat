set comm=git status

@echo off
goto starting

:looping
  for /d %%d in (*) do (
    echo %%d
    cd %%d
    %comm%
    cd ..
    echo =======================================================================
  )
  goto ending

:starting
  cls
  set currDir=%cd%
  cd /d C:\Users\vhp1\code\
  goto looping

:ending
  cd %currDir%
