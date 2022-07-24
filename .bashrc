################################################################################
## vhp1 start
################################################################################

alias l="ls -lh --group-directories-first"

function disk {
  du -h $@ | sort -h
}

function dropboxclean {
  find ~/Dropbox -iname "*conflicted*" $@
}

function bibtextidy {
  bibtex-tidy --omit=organization --curly --space=4 --align=0 --sort=key --duplicates=key,doi,abstract,citation --merge=combine --no-escape --sort-fields=author,year,title,booktitle,journal,volume,number,pages,publisher,institution,school --trailing-commas --remove-empty-fields --enclosing-braces=title $@
}

function notebook {
  jupyter notebook $@ 2> /dev/null &
}

function connect {
  sudo openconnect --no-dtls connect.rice.edu -u vhp1 $@
}

function nots {
  ssh nots.rice.edu $@
}

function scpnots {
  scp $@ nots.rice.edu:/projects/vardi/vhp1
}

function touchmap { # Vu-Precision
  xinput map-to-output "ELAN900C:00 04F3:2C6B" eDP-1 $@
}

################################################################################

export MANPATH="$MANPATH:~/bin/man" # NOTS

export PATH="$PATH:/projects/vardi/vhp1/bin" # NOTS
export PATH="$PATH:/usr/local/texlive/2022/bin/x86_64-linux"
export PATH="$PATH:~/bin" # NOTS
export PATH="$PATH:~/code/dpmcdev/mcc/bin"
export PATH="$PATH:~/code/misc"
export PATH="$PATH:~/Dropbox/main"
export PATH="$PATH:~/Dropbox/main/bin"

################################################################################

PS1="\e[33m\@ \e[35m\u@\h \e[33m\w\e[m\n\$ "

################################################################################
## vhp1 end
################################################################################
