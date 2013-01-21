Install this lexer and then add the following to the dot zsh file of your choice for nicer pip searches:

    pips () { pip search $1 | pygmentize -l pip -f terminal256 -O style=vs | less }

You can probably come up with a better name than I did.
