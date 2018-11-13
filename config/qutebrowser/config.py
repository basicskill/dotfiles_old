config.load_autoconfig()

c.downloads.position = 'bottom'
#c.content.user_stylesheets = '~/dark.css'
# pametne stvari: quantum-vim, mps-youtube, neovim
# nord boje
# https://github.com/szorfein/dotfiles

c.content.cookies.accept = 'all'
c.colors.webpage.bg = 'black'


nTab='file:///home/mladen/.config/startpage/startpage.html'
c.aliases = {
        'w': 'session-save', 'q': 'quit', 'wq': 'quit --save'

}
c.auto_save.session = True
c.auto_save.interval = 15000 

c.backend = 'webengine'

c.tabs.wrap = True

c.url.default_page = '~/.config/startpage/startpage.html'

c.url.searchengines = {
        'DEFAULT' :    'https://duckduckgo.com/?q={}',
        'gh'      :    'https://github.com/search?q={}',
        'yt'      :    'https://youtube.com/results?search_query={}',
        'aw'      :    'https://wiki.archlinux.org/index.php/{}',
        'tpb'     :    'https://thepiratebay.org/index.php?q=b{}',
        '4'       :    'https://boards.4chan.org/{}/',
        'tr'      :    'https://translate.google.com/#en/sr/{}',
        'sh'      :    'https://sci-hub.tw/{}',
        'r'       :    'https://www.reddit.com/r/{}',
        'wa'      :    'https://www.wolframalpha.com/input/?i={}',
        'w'       :    'http://wttr.in/{}',
        'tw'      :    'https://www.thinkwiki.org/wiki/{}',
}

c.url.start_pages = ['file:///home/mladen/.config/startpage/startpage.html']

#~~~~~~~~~~~~~~~~~~~~~ Tabovi ~~~~~~~~~~~~~~~~~~~~~# 
c.tabs.mousewheel_switching = False
c.tabs.new_position.unrelated = 'next'
config.bind('D', 'tab-close')

#~~~~~~~~~~~~~~~~~~~~~ hintovi ~~~~~~~~~~~~~~~~~~~~~# 
c.colors.hints.bg = 'black'
c.colors.hints.fg = 'rgb(211, 220, 40)'
c.colors.hints.match.fg = 'green'
c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'
c.colors.keyhint.fg = '#FFFFFF'
c.colors.keyhint.suffix.fg = '#FFFF00'

#~~~~~~~~~~~~~~~~~~~~~ tabs colors ~~~~~~~~~~~~~~~~~~~~~# 
c.colors.tabs.indicator.system = 'rgb'
c.colors.tabs.bar.bg = 'black'
c.colors.tabs.even.bg = '#595959'
c.colors.tabs.even.fg = 'white'
c.colors.tabs.odd.bg = '#373737'
c.colors.tabs.odd.fg = 'white'
c.colors.tabs.selected.even.bg = 'black'
c.colors.tabs.selected.even.fg = 'white'
c.colors.tabs.selected.odd.bg = 'black'
c.colors.tabs.selected.odd.fg = 'white'


#~~~~~~~~~~~~~~~~~~~~~ UNBajndovi ~~~~~~~~~~~~~~~~~~~~~# 
config.unbind('d')
config.unbind('m')

#~~~~~~~~~~~~~~~~~~~~~ Download ~~~~~~~~~~~~~~~~~~~~~# 
c.colors.tabs.indicator.error = '#ff0000'
c.colors.tabs.indicator.start = '#0000aa'
c.colors.tabs.indicator.stop = '#00aa00'


#~~~~~~~~~~~~~~~~~~~~~ Bajndovi ~~~~~~~~~~~~~~~~~~~~~# 
## Bindings for normal mode

## Specijalni
config.bind("'", 'enter-mode jump_mark')
config.bind('+', 'zoom-in')
config.bind('-', 'zoom-out')
config.bind('.', 'repeat-command')
config.bind('/', 'set-cmd-text /')
config.bind(':', 'set-cmd-text :')
config.bind('=', 'zoom')
#config.bind('?', 'help')
config.bind('@', 'run-macro')
config.bind('`', 'enter-mode set_mark')
config.bind('{{', 'navigate prev -t')
config.bind('}}', 'navigate next -t')

# Koma ;
config.bind(';I', 'hint images tab')
config.bind(';R', 'hint --rapid links window')
config.bind(';Y', 'hint links yank-primary')
config.bind(';d', 'hint links download')
config.bind(';f', 'hint all tab-fg')
config.bind(';h', 'hint all hover')
config.bind(';i', 'hint images')
config.bind(';y', 'hint links yank')

config.bind(';t', 'hint inputs')
config.bind(',', 'hint inputs')
config.bind('I', 'hint inputs ;; a')

# Ctrl
config.bind('<Ctrl-F5>', 'reload -f')
config.bind('<Ctrl-N>', 'open -w')
config.bind('<Ctrl-Q>', 'wq')
config.bind('<Ctrl-Return>', 'follow-selected -t')
config.bind('<Ctrl-Shift-N>', 'open -p')
config.bind('<Ctrl-V>', 'enter-mode passthrough')
config.bind('<Ctrl-p>', 'tab-pin') # !!!

config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave')
config.bind('<F11>', 'fullscreen')
config.bind('<F5>', 'reload')
config.bind('<Return>', 'follow-selected')
config.bind('<back>', 'back')
config.bind('<forward>', 'forward')

# g
config.bind('gj', 'tab-move -')
config.bind('gk', 'tab-move +')
config.bind('gB', 'set-cmd-text -s :bookmark-load -t')
config.bind('gC', 'tab-clone')
config.bind('gf', 'view-source')
config.bind('gg', 'scroll-to-perc 0')
config.bind('go', 'set-cmd-text :open {url:pretty}')

config.bind('ge', 'open https://mail.google.com/mail/u/0/#inbox')
config.bind('gm', 'open https://www.facebook.com/messages/t/')
config.bind('gi', 'open https://www.instagram.com/?hl=en')
config.bind('gd', 'open https://drive.google.com/drive/my-drive')
config.bind('gw', 'open https://web.whatsapp.com/')
config.bind('gy', 'open https://www.youtube.com/') 
config.bind('ci', 'open https://www.integral-calculator.com/')

# G (ruzno!!)
config.unbind('gtM')
config.unbind('gtm')
config.unbind('gti')
config.unbind('gtd')
config.unbind('gtw')
config.unbind('gty')


config.bind('wa', 'open https://www.wolframalpha.com/') # !!!

config.bind('Yb', 'open -t https://www.youtube.com/') 
config.bind('YB', 'open -t https://www.youtube.com/') 

# Slova
config.bind('ad', 'download-cancel')
config.bind('dw', 'download') # !!!!


config.bind('F', 'hint all tab')

config.bind('N', 'search-prev')
config.bind('O', 'set-cmd-text -s :open -t')



config.bind('co', 'tab-only')
config.bind('cd', 'download-clear')
config.bind('f', 'hint')
config.bind('T', 'tab-move -1 ;; open -t')
config.bind('t', 'open -t')

config.bind('H', 'back')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('L', 'forward')

config.bind('1', 'tab-focus 1')
config.bind('2', 'tab-focus 2')
config.bind('3', 'tab-focus 3')
config.bind('4', 'tab-focus 4')
config.bind('5', 'tab-focus 5')
config.bind('6', 'tab-focus 6')
config.bind('7', 'tab-focus 7')
config.bind('8', 'tab-focus 8')
config.bind('9', 'tab-focus 9')
config.bind('0', 'tab-focus -1')

config.bind('h', 'scroll left')
config.bind('i', 'enter-mode insert')
config.bind('j', 'scroll down')
config.bind('k', 'scroll up')
config.bind('l', 'scroll right')
config.bind('n', 'search-next')
config.bind('o', 'set-cmd-text -s :open')


config.bind('q', 'record-macro')
config.bind('r', 'reload')
config.bind('sf', 'save')

config.bind('u', 'undo')
config.bind('v', 'enter-mode caret')
config.bind('wP', 'open -w -- {primary}')

config.bind('wf', 'hint all window')
config.bind('wh', 'back -w')
config.bind('wp', 'open -w -- {clipboard}')

config.bind('yD', 'yank domain -s')
config.bind('yP', 'yank pretty-url -s')
config.bind('yT', 'yank title -s')
config.bind('yY', 'yank -s')
config.bind('yd', 'yank domain')
config.bind('yp', 'yank pretty-url')
config.bind('J', 'scroll left', mode='caret')
config.bind('H', 'scroll down', mode='caret')
config.bind('yy', 'yank')
config.bind('yt', 'yank title')


################ END ################ 
## Bindings for caret mode
# config.bind('$', 'move-to-end-of-line', mode='caret')
# config.bind('0', 'move-to-start-of-line', mode='caret')
# config.bind('<Ctrl-Space>', 'drop-selection', mode='caret')
# config.bind('<Escape>', 'leave-mode', mode='caret')
# config.bind('<Return>', 'yank selection', mode='caret')
# config.bind('<Space>', 'toggle-selection', mode='caret')
# config.bind('G', 'move-to-end-of-document', mode='caret')
# config.bind('K', 'scroll up', mode='caret')
# config.bind('L', 'scroll right', mode='caret')
# config.bind('Y', 'yank selection -s', mode='caret')
# config.bind('[', 'move-to-start-of-prev-block', mode='caret')
# config.bind(']', 'move-to-start-of-next-block', mode='caret')
# config.bind('b', 'move-to-prev-word', mode='caret')
# config.bind('c', 'enter-mode normal', mode='caret')
# config.bind('e', 'move-to-end-of-word', mode='caret')
# config.bind('gg', 'move-to-start-of-document', mode='caret')
# config.bind('h', 'move-to-prev-char', mode='caret')
# config.bind('j', 'move-to-next-line', mode='caret')
# config.bind('k', 'move-to-prev-line', mode='caret')
# config.bind('l', 'move-to-next-char', mode='caret')
# config.bind('v', 'toggle-selection', mode='caret')
# config.bind('w', 'move-to-next-word', mode='caret')
# config.bind('y', 'yank selection', mode='caret')
# config.bind('{', 'move-to-end-of-prev-block', mode='caret')
# config.bind('}', 'move-to-end-of-next-block', mode='caret')

## Bindings for command mode
# config.bind('<Alt-B>', 'rl-backward-word', mode='command')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='command')
# config.bind('<Alt-D>', 'rl-kill-word', mode='command')
# config.bind('<Alt-F>', 'rl-forward-word', mode='command')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='command')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='command')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='command')
# config.bind('<Ctrl-C>', 'completion-item-yank', mode='command')
# config.bind('<Ctrl-D>', 'completion-item-del', mode='command')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='command')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='command')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='command')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='command')
# config.bind('<Ctrl-N>', 'command-history-next', mode='command')
# config.bind('<Ctrl-P>', 'command-history-prev', mode='command')
# config.bind('<Ctrl-Return>', 'command-accept --rapid', mode='command')
# config.bind('<Ctrl-Shift-C>', 'completion-item-yank --sel', mode='command')
# config.bind('<Ctrl-Shift-Tab>', 'completion-item-focus prev-category', mode='command')
# config.bind('<Ctrl-Tab>', 'completion-item-focus next-category', mode='command')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='command')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='command')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='command')
# config.bind('<Down>', 'completion-item-focus --history next', mode='command')
# config.bind('<Escape>', 'leave-mode', mode='command')
# config.bind('<Return>', 'command-accept', mode='command')
# config.bind('<Shift-Delete>', 'completion-item-del', mode='command')
# config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
# config.bind('<Tab>', 'completion-item-focus next', mode='command')
# config.bind('<Up>', 'completion-item-focus --history prev', mode='command')

## Bindings for hint mode
# config.bind('<Ctrl-B>', 'hint all tab-bg', mode='hint')
# config.bind('<Ctrl-F>', 'hint links', mode='hint')
# config.bind('<Ctrl-R>', 'hint --rapid links tab-bg', mode='hint')
# config.bind('<Escape>', 'leave-mode', mode='hint')
# config.bind('<Return>', 'follow-hint', mode='hint')

## Bindings for insert mode
# config.bind('<Ctrl-E>', 'open-editor', mode='insert')
# config.bind('<Escape>', 'leave-mode', mode='insert')
# config.bind('<Shift-Ins>', 'insert-text {primary}', mode='insert')

## Bindings for passthrough mode
# config.bind('<Ctrl-V>', 'leave-mode', mode='passthrough')

## Bindings for prompt mode
# config.bind('<Alt-B>', 'rl-backward-word', mode='prompt')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='prompt')
# config.bind('<Alt-D>', 'rl-kill-word', mode='prompt')
# config.bind('<Alt-F>', 'rl-forward-word', mode='prompt')
# config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='prompt')
# config.bind('<Alt-Y>', 'prompt-yank', mode='prompt')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='prompt')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='prompt')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='prompt')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='prompt')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='prompt')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='prompt')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='prompt')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='prompt')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='prompt')
# config.bind('<Ctrl-X>', 'prompt-open-download', mode='prompt')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='prompt')
# config.bind('<Down>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Escape>', 'leave-mode', mode='prompt')
# config.bind('<Return>', 'prompt-accept', mode='prompt')
# config.bind('<Shift-Tab>', 'prompt-item-focus prev', mode='prompt')
# config.bind('<Tab>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Up>', 'prompt-item-focus prev', mode='prompt')

## Bindings for register mode
config.bind('<Escape>', 'leave-mode', mode='register')

## Bindings for yesno mode
config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='yesno')
config.bind('<Alt-Y>', 'prompt-yank', mode='yesno')
config.bind('<Escape>', 'leave-mode', mode='yesno')
config.bind('<Return>', 'prompt-accept', mode='yesno')
config.bind('n', 'prompt-accept no', mode='yesno')
config.bind('y', 'prompt-accept yes', mode='yesno')
