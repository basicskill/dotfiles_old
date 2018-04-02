" Gajd
	inoremap <Space><Space> <Esc>/<++><Enter>c4l
" LaTeX
	autocmd FileType tex noremap <F5> <Esc>:w\|!pdflatex<space><c-r>%<Enter>%
	autocmd FileType tex inoremap <c-b> \textbf{}<++><Esc>T{i
	autocmd FileType tex inoremap <c-u> \underline{}<++><Esc>T{i
	autocmd FileType tex inoremap <c-i> \textit{}<++><Esc>T{i
	autocmd FileType tex inoremap ;sec \section{}<++><Esc>T{i
	autocmd FileType tex inoremap ;ssec \subsection{}<++><Esc>T{i
	autocmd FileType tex inoremap ;sssec \subsubsection{}<++><Esc>T{i
