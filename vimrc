function Zameni()
	:%s/CH/č/g
	:%s/CC/ć/g
	:%s/ZH/ž/g
	:%s/SH/š/g
	:%s/DJ/đ/g
endfunction

" Vim
set nocompatible
filetype off

set nu
set tabstop=4
set shiftwidth=4
set encoding=utf-8
syntax on
command Trans execute Zameni()
noremap <F2> :Trans<Enter>

" Vundle
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" --- Mesto za pluginove ---
Plugin 'gmarik/Vundle.vim'
Plugin 'vim-scripts/indentpython.vim'
call vundle#end()
filetype plugin indent on

" Gajd
nnoremap <tab> <Esc>/<++><Enter>c4l
inoremap ;ga <++>

" copy
vnoremap <C-c> "cy<Esc>:!echo -n '<C-R>c' \|<space>xclip<CR><Enter> 

" LaTeX
	autocmd FileType tex noremap <F3> <Esc>:w\|!pdflatex<space><c-r>%<Enter><Enter>

	autocmd FileType tex inoremap <c-b> \textbf{
	autocmd FileType tex inoremap <c-u> \underline{
	"autocmd FileType tex inoremap <c-i> \textit{

	autocmd FileType tex inoremap ;sec \section{}<Enter><++><Esc>k$i
	autocmd FileType tex inoremap ;ssec \subsection{}<Enter><++><Esc>k$i
	autocmd FileType tex inoremap ;sssec \subsubsection{}<Enter><++><Esc>k$i

	autocmd FileType tex inoremap ;i \includegraphic{
	autocmd FileType tex inoremap ;ff \begin{figure}[t]<Enter>\includegraphics{}<Enter>\centering<Enter>\end{figure}<Esc>2k$i
	autocmd FileType tex inoremap ;fw \begin{wrapfigure}{r}{\textwidth}<Enter>\centering<Enter>\includegraphics{}<Enter>\end{figure}<Esc>k$i

	autocmd FileType tex vnoremap <c-b> \textbf{
	autocmd FileType tex vnoremap <c-u> \underline{
	"autocmd FileType tex vnoremap <c-i> \textit{

" Markdown
	autocmd FileType markdown noremap <F3> <Esc>:w\|!pandoc<space><c-r>%<space>-t<space>beamer<space>-o<space>%.pdf<Enter><Enter>
	autocmd Filetype rmd map <F3> :w\|!echo<space>"require(rmarkdown);<space>render('<c-r>%')"<space>\|<space>R<space>--vanilla<Enter><Enter>

" Prolog <3 
	autocmd FileType prolog noremap <F3> <Esc>:w\|!gprolog<space>--consult-file<space>%<Enter>

"split navigations
	nnoremap <C-J> <C-W><C-J>
	nnoremap <C-K> <C-W><C-K>
	nnoremap <C-L> <C-W><C-L>
	nnoremap <C-H> <C-W><C-H>

" PEP8
au BufNewFile, BufRead *.py
    \ set tabstop=4
    \ set softtabstop=4
    \ set shiftwidth=4
    \ set textwidth=79
    \ set expandtab
    \ set autoindent
    \ set fileformat=unix

"au BufNewFile,BufRead *.js, *.html, *.css
"   \ set tabstop=2
"   \ set softtabstop=2
"   \ set shiftwidth=2
