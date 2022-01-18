################################################################################
## vhp1
################################################################################

alias touchmap='xinput map-to-output "ELAN900C:00 04F3:2C6B" eDP-1' # Vu-Precision

alias l='ls -lh'

alias notebook='jupyter notebook 2>/dev/null &'

alias connect='sudo openconnect --no-dtls connect.rice.edu -u vhp1'
alias nots='ssh nots.rice.edu'

################################################################################

export MANPATH="$MANPATH:~/bin/man"

export PATH="$PATH:~/bin"
export PATH="$PATH:~/bin/diff-so-fancy"
export PATH="$PATH:~/code/dpmcdev/addmc"
export PATH="$PATH:~/code/dpmcdev/lg"
export PATH="$PATH:~/code/dpmcdev/lg/build"
export PATH="$PATH:~/code/misc"
export PATH="$PATH:~/code/ssat/bin"
export PATH="$PATH:~/Dropbox/eval"
export PATH="$PATH:~/Dropbox/eval/bin"
export PATH="$PATH:~/Dropbox/main"
export PATH="$PATH:~/Dropbox/main/bin"

################################################################################

PS1="\e[33m\@ \e[35m\u@\h \e[33m\w\e[m\n\$ "
