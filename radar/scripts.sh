#ls -lh | sort -h -r -k 5 | head -n 1 # list file and sort, -h is for reading with the human scale understanding -k is for sorting by the 5th colone (size) -r is reverse sorting by DESC
ls -1S | head -n 1 # -1 for just displaying one file per line, -S for DESC, head -n 1 just taking the first one

