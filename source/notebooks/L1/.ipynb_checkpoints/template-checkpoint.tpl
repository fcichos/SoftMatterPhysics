((*- extends 'index.tex.j2' -*))

((* block header *))
    ((* block input_group *))
        ((*- if cell.metadata.get('nbconvert', {}).get('show_code', False) -*))
            ((( super() )))
        ((*- endif -*))
    ((* endblock input_group *))
    \setcounter{section}{1}
((* endblock header *))

((* block markdowncell scoped *))
    \begin{markdown}
        ((( cell.source | strip_ansi | convert_pandoc | e )))
    \end{markdown}
((* endblock markdowncell *))

((* block codecell scoped *))
    \begin{Verbatim}[commandchars=\\\{\}]
        ((( cell.source | strip_ansi | escape_latex )))
    \end{Verbatim}
((* endblock codecell *))