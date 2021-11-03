################################################################################
## vhp1
################################################################################

alias l="ls -lh"

alias notebook="jupyter notebook 2>/dev/null &"

alias connect="sudo openconnect --no-dtls connect.rice.edu -u vhp1"
alias nots="ssh nots.rice.edu"

################################################################################

export MANPATH="$MANPATH:~/bin/man"

export PATH="$PATH:~/bin"
export PATH="$PATH:~/bin/diff-so-fancy"
export PATH="$PATH:~/code/dpmc/addmc"
export PATH="$PATH:~/code/dpmc/lg"
export PATH="$PATH:~/code/dpmc/lg/build"
export PATH="$PATH:~/code/misc"
export PATH="$PATH:~/code/ssat/bin"
export PATH="$PATH:~/Dropbox/eval"
export PATH="$PATH:~/Dropbox/main"
export PATH="$PATH:~/Dropbox/main/bin"

################################################################################

PS1="\e[33m\@ \e[35m\u@\h \e[33m\w\e[m\n\$ "
