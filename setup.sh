#! /bin/bash


## Promenljive

dir=~/.dotfiles
files1="config/i3 config/qutebrowser config/startpage config/ranger config/compton.conf "
files2="Xdefaults Xmodmap vimrc bashrc scripts xinitrc i3blocks.conf"
files=$files1\ $files2


## Linkovanje
for file in $files; do
	echo "Linkujem $file"
	rm -r ~/.$file
	ln -s $dir/$file ~/.$file
	echo "gotovo!"
done
