#! /bin/bash


## Promenljive

dir=~/dotfiles
files="config/i3 config/qutebrowser config/startpage config/ranger config/compton.conf Xdefaults Xmodmap vimrc bashrc scripts"

## Linkovanje
for file in $files; do
	echo "Linkujem $file"
	rm -r ~/.$file
	ln -s $dir/$file ~/.$file
	echo "gotovo!"
done
