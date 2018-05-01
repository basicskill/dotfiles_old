function Zameni()
	:%s/CH/č/g
	:%s/CC/ć/g
	:%s/ZH/ž/g
	:%s/SH/š/g
	:%s/DJ/đ/g
endfunction

" Vim
set nu
set tabstop=4
set encoding=utf-8
syntax on
command Trans execute Zameni()

" Gajd
nnoremap <tab> <Esc>/<++><Enter>c4l
inoremap ;ga <++>

" copy
vnoremap <C-c> "cy<Esc>:!echo -n '<C-R>c' \|<space>xclip<CR><Enter> 

" LaTeX
	autocmd FileType tex noremap <F3> <Esc>:w\|!pdflatex<space><c-r>%<Enter><Enter>

	autocmd FileType tex inoremap <c-b> \textbf{
	autocmd FileType tex inoremap <c-u> \underline{
	autocmd FileType tex inoremap <c-i> \textit{

	autocmd FileType tex inoremap ;sec \section{}<Enter><++><Esc>k$i
	autocmd FileType tex inoremap ;ssec \subsection{}<Enter><++><Esc>k$i
	autocmd FileType tex inoremap ;sssec \subsubsection{}<Enter><++><Esc>k$i

	autocmd FileType tex inoremap ;i \includegraphic{
	autocmd FileType tex inoremap ;ff \begin{figure}[t]<Enter>\includegraphics{}<Enter>\centering<Enter>\end{figure}<Esc>2k$i
	autocmd FileType tex inoremap ;fw \begin{wrapfigure}{r}{\textwidth}<Enter>\centering<Enter>\includegraphics{}<Enter>\end{figure}<Esc>k$i

" Markdown
	autocmd FileType md noremap <F3> <Esc>:w\|!pandoc<space><c-r>%<space>-t<space>beamer<space>-o<space>%.pdf<Enter><Enter>
