# .bashrc
# powerline-daemon -q
# POWERLINE_BASH_CONTINUATION=1
# POWERLINE_BASH_SELECT=1
# . /usr/share/powerline/bindings/bash/powerline.sh
# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

export PATH=~/.scripts:$PATH
export PATH=~/.local/share/jdk1.8.0_181/bin:$PATH
export PATH=~/.gem/ruby/2.5.0/bin:$PATH
#set -o vi

# Use bash-completion, if available
[[ $PS1 && -f /usr/share/bash-completion/bash_completion ]] && \
    . /usr/share/bash-completion/bash_completion

# User specific aliases and functions
alias ll="ls -lh --color"
alias ls="ls --color"
alias v="vim"
alias sv="sudo vim"
alias pi="ipython"
alias bp="bpython"
alias p="python"
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


# wd
alias cw='cd projekti/tutovi/tensor_flow'


# added by Anaconda3 5.3.0 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/home/mladen/.anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/home/mladen/.anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/mladen/.anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/home/mladen/.anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<
