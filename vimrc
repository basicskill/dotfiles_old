" Vim
set nu
set tabstop=4
set encoding=utf-8
syntax on

" LaTeX
	autocmd FileType tex noremap <F3> <Esc>:w\|!pdflatex<space><c-r>%<Enter><Enter>

	autocmd FileType tex inoremap <c-b> \textbf{
	autocmd FileType tex inoremap <c-u> \underline{
	autocmd FileType tex inoremap <c-i> \textit{

	autocmd FileType tex inoremap ;sec \section{}<Enter><++><Esc>k$i
	autocmd FileType tex inoremap ;ssec \subsection{}<Enter><++><Esc>k$i
	autocmd FileType tex inoremap ;sssec \subsubsection{}<Enter><++><Esc>k$i

	autocmd FileType tex inoremap <tab> <Esc>/<++><Enter>c4l
	autocmd FileType tex inoremap <Shift><tab> <tab>
