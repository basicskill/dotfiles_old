# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

export PATH=~/.scripts:$PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
alias ll="ls -alh --color"
alias v="vim"
alias sv="sudo vim"

# Pacman
alias pacman="sudo pacman"
alias yaourt="sudo yaourt"
alias pc="sudo pacman"
alias pip="sudo pip"

# Prompt
export PS1='\[\033[00;32m\]\u\[\033[00;33m\]@\[\033[00;32m\]\h\[\033[01;30m\]:\[\033[01;36m\]\w\n\[\033[01;37m\]\$ \[\033[00m\]'

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# Auto complete
complete -cf sudo 
complete -c man
