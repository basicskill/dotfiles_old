" Vim
set nu
" Gajd
" LaTeX
	autocmd FileType tex noremap <F5> <Esc>:w\|!pdflatex<space><c-r>%<Enter><Enter>
	autocmd FileType tex inoremap <c-b> \textbf{
	autocmd FileType tex inoremap <c-u> \underline{
	autocmd FileType tex inoremap <c-i> \textit{
	autocmd FileType tex inoremap ;sec \section{
	autocmd FileType tex inoremap ;ssec \subsection{
	autocmd FileType tex inoremap ;sssec \subsubsection{
