#! /bin/bash

#################
#		#
#		#
#		#
#################

## Promenljive

dir=~/dotfiles
files="config/i3/config"

## Linkovanje
for file in $files; do
	echo "Linkujem $file"
	ln -s $dir/$file ~/.$file
	echo "gotovo!"
done
