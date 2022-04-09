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
  bibtex-tidy --curly --space=4 --align=0 --sort=key --duplicates=key,doi,abstract,citation --merge=combine --strip-enclosing-braces --no-escape --sort-fields=title,shorttitle,author,year,month,day,journal,booktitle,location,on,publisher,address,series,volume,number,pages,doi,isbn,issn,url,urldate,copyright,category,note,metadata --remove-empty-fields --enclosing-braces=title $@
}

function notebook {
  jupyter notebook $@ 2>/dev/null &
}

function connect {
  sudo openconnect --no-dtls connect.rice.edu -u vhp1 $@
}

function nots {
  ssh nots.rice.edu $@
}

function touchmap { # Vu-Precision
  xinput map-to-output "ELAN900C:00 04F3:2C6B" eDP-1 $@
}

################################################################################

export MANPATH="$MANPATH:~/bin/man" # NOTS

export PATH="$PATH:/usr/local/texlive/2021/bin/x86_64-linux"
export PATH="$PATH:~/bin" # NOTS
export PATH="$PATH:~/code/misc"
export PATH="$PATH:~/Dropbox/main"
export PATH="$PATH:~/Dropbox/main/bin"

################################################################################

PS1="\e[33m\@ \e[35m\u@\h \e[33m\w\e[m\n\$ "

################################################################################
## vhp1 end
################################################################################
