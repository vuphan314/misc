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
  set currDir=%cd%
  cd /d D:\repos\
  goto looping

:ending
  cd %currDir%
