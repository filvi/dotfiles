:set number

" toggle between seeing numbers and relative numbers in different modes
:augroup numbertoggle
:  autocmd!
:  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
:  autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
:augroup END

:set ruler

:set path+=**
:set wildmenu

filetype indent plugin on
syntax enable
set background=dark
set autoindent
