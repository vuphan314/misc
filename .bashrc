################################################################################
## vhp1
################################################################################

alias touchmap='xinput map-to-output "ELAN900C:00 04F3:2C6B" eDP-1' # Vu-Precision

alias l='ls -lh'

alias notebook='jupyter notebook 2>/dev/null &'

alias connect='sudo openconnect --no-dtls connect.rice.edu -u vhp1'
alias nots='ssh nots.rice.edu'

################################################################################

if [[ -n $MANPATH ]]; then
  export MANPATH="$MANPATH:~/bin/man" # NOTS
fi

export PATH="$PATH:~/bin" # NOTS
export PATH="$PATH:~/code/misc"
export PATH="$PATH:~/Dropbox/main"
export PATH="$PATH:~/Dropbox/main/bin"
export PATH="$PATH:~/Dropbox/main/eval"
export PATH="$PATH:~/Dropbox/main/eval/bin"

################################################################################

PS1="\e[33m\@ \e[35m\u@\h \e[33m\w\e[m\n\$ "
