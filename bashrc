# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

export PATH=~/.scripts:$PATH
#set -o vi

# Use bash-completion, if available
[[ $PS1 && -f /usr/share/bash-completion/bash_completion ]] && \
    . /usr/share/bash-completion/bash_completion

# User specific aliases and functions
alias ll="ls -alh --color"
alias ls="ls -lh --color"
alias v="vim"
alias sv="sudo vim"
alias p="ipython"
alias sp="sudo python"

# Sudo
alias pacman="sudo pacman"
alias pc="sudo pacman"
alias pip="sudo pip"
alias mount="sudo mount"
alias umount="sudo umount"

# telefon
alias telefon="simple-mtpfs"
alias utelefon="fusermount -u"

# Prompt
export PS1='\[\033[00;32m\]\u\[\033[00;33m\]@\[\033[00;32m\]\h\[\033[01;30m\]:\[\033[01;36m\]\w\n\[\033[01;37m\]\$ \[\033[00m\]'

# Nesto za jezik
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# Auto complete
complete -cf sudo 
complete -c man

# zika
alias muzika="ncmpcpp"
#
export VISUAL="vim"

alias dmenu="dmenu -nb '#101010' -nf '#ddd' -sb '#385e6b' -sf '#101010'"



# tmp!
alias pch="Downloads/pycharm/bin/pycharm.sh"
