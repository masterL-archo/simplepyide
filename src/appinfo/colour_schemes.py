darcula = {'editor': {'bg': '#0a0e14', 'fg': '#8be9fd', 'select_bg': '#1b2733', 'inactive_select_bg': '#1b2733', 'caret': '#b3b1ad', 'caret_width': 1, 'border_width': 0, 'focus_border_width': 0}, 'general': {'comment': '#626a73', 'error': '#ff3333', 'escape': '#b3b1ad', 'keyword': '#ff7700', 'name': '#ff8f40', 'string': '#95e6cb', 'punctuation': '#b3b1ad'}, 'keyword': {'constant': '#ff7700', 'declaration': '#ff7700', 'namespace': '#ff7700', 'pseudo': '#ff7700', 'reserved': '#ff7700', 'type': '#ff7700'}, 'name': {'attr': '#ff8f40', 'builtin': '#e6b450', 'builtin_pseudo': '#e6b450', 'class': '#ff8f40', 'class_variable': '#ff8f40', 'constant': '#ffee99', 'decorator': '#e6b673', 'entity': '#ff8f40', 'exception': '#ff8f40', 'function': '#ffb454', 'global_variable': '#ff8f40', 'instance_variable': '#ff8f40', 'label': '#ff8f40', 'magic_function': '#ff8f40', 'magic_variable': '#ff8f40', 'namespace': '#b3b1ad', 'tag': '#ff8f40', 'variable': '#ff8f40'}, 'operator': {'symbol': '#f29668', 'word': '#f29668'}, 'string': {'affix': '#c2d94c', 'char': '#95e6cb', 'delimeter': '#c2d94c', 'doc': '#c2d94c', 'double': '#c2d94c', 'escape': '#c2d94c', 'heredoc': '#c2d94c', 'interpol': '#c2d94c', 'regex': '#95e6cb', 'single': '#c2d94c', 'symbol': '#c2d94c'}, 'number': {'binary': '#e6b450', 'float': '#e6b450', 
'hex': '#e6b450', 'integer': '#e6b450', 'long': '#e6b450', 'octal': '#e6b450'}, 'comment': {'hashbang': '#626a73', 'multiline': '#626a73', 'preproc': '#ff7700', 'preprocfile': '#c2d94c', 'single': '#626a73', 'special': '#626a73'}}
light = {'editor': {'bg': '#fafafa', 'fg': "#0066cc", 'select_bg': '#d1e4f4', 'inactive_select_bg': '#e7e8e9', 'caret': '#575f66', 'caret_width': 1, 'border_width': 0, 'focus_border_width': 0}, 'general': {'comment': '#abb0b6', 'error': '#f51818', 'escape': '#575f66', 'keyword': '#fa8d3e', 'name': '#ff8f40', 'string': '#4cbf99', 'punctuation': '#575f66'}, 'keyword': {'constant': '#fa8d3e', 'declaration': '#fa8d3e', 'namespace': '#fa8d3e', 'pseudo': '#fa8d3e', 'reserved': '#fa8d3e', 'type': '#fa8d3e'}, 'name': {'attr': '#ff8f40', 'builtin': '#ff9940', 'builtin_pseudo': '#ff9940', 'class': '#ff8f40', 'class_variable': '#ff8f40', 'constant': '#a37acc', 'decorator': '#e6b673', 'entity': '#ff8f40', 'exception': '#ff8f40', 'function': '#f2ae49', 'global_variable': '#ff8f40', 'instance_variable': '#ff8f40', 'label': '#ff8f40', 'magic_function': '#ff8f40', 'magic_variable': '#ff8f40', 'namespace': '#575f66', 'tag': '#ff8f40', 'variable': '#ff8f40'}, 'operator': {'symbol': '#ed9366', 'word': '#ed9366'}, 'string': {'affix': '#86b300', 'char': '#4cbf99', 'delimeter': '#86b300', 'doc': '#86b300', 'double': '#86b300', 'escape': '#86b300', 'heredoc': '#86b300', 'interpol': '#86b300', 'regex': '#4cbf99', 'single': '#86b300', 'symbol': '#86b300'}, 'number': {'binary': '#ff9940', 'float': '#ff9940', 
'hex': '#ff9940', 'integer': '#ff9940', 'long': '#ff9940', 'octal': '#ff9940'}, 'comment': {'hashbang': '#abb0b6', 'multiline': '#abb0b6', 'preproc': '#fa8d3e', 'preprocfile': '#86b300', 'single': '#abb0b6', 'special': '#abb0b6'}}
modern_dark = {
    # Original editor settings - preserved exactly
    'editor': {
        'bg': '#282a36', 
        'fg': '#8be9fd', 
        'select_bg': '#44475a', 
        'select_fg': '#f8f8f2', 
        'inactive_select_bg': '#402725', 
        'caret': '#f8f8f0', 
        'caret_width': 1, 
        'border_width': 0, 
        'focus_border_width': 0,
        # NEW: Extended editor UI elements
        'line_highlight': '#3e4452',
        'current_line': '#21222c',
        'gutter_bg': '#21222c',
        'gutter_fg': '#6272a4',
        'line_number': '#6272a4',
        'line_number_current': '#8be9fd',
        'scrollbar_track': '#282a36',
        'scrollbar_thumb': '#44475a',
        'scrollbar_thumb_hover': '#6272a4',
        'search_bg': '#ffb86c33',
        'search_fg': '#f8f8f2',
        'match_bg': '#ff79c6',
        'bookmark': '#bd93f9',
        'breakpoint_bg': '#ff5555',
        'diff_add': '#50fa7b22',
        'diff_delete': '#ff555522',
        'diff_change': '#ffb86c22',
        'fold_marker': '#ff79c6',
        'indent_guide': '#44475a',
        'whitespace': '#3e445288',
        'tab_size': 4,
        'show_invisibles': True
    },
    # Original general settings - preserved exactly
    'general': {
        'comment': '#6272a4', 
        'error': '#f8f8f0', 
        'escape': '#f8f8f2', 
        'keyword': '#ff79c6', 
        'name': '#50fa7b', 
        'string': '#99c794', 
        'punctuation': '#ff79c6',
        # NEW: Extended general syntax
        'number': '#bd93f9',
        'boolean': '#ff79c6',
        'none': '#ffb86c',
        'warning': '#ffb86c',
        'info': '#8be9fd',
        'hint': '#50fa7b',
        'todo': '#f1fa8c',
        'deprecated': '#ff5555'
    },
    # Original keyword settings - preserved exactly
    'keyword': {
        'constant': '#bd93f9',
        'declaration': '#ff79c6',
        'namespace': '#ff79c6',
        'pseudo': '#ff79c6',
        'reserved': '#ff79c6',
        'type': '#ff79c6',
        # NEW: Python-specific keywords
        'control': '#ff79c6',
        'import': '#8be9fd',
        'from': '#8be9fd',
        'async': '#ff79c6',
        'await': '#ff79c6',
        'def': '#50fa7b',
        'class': '#8be9fd',
        'with': '#ff79c6',
        'for': '#ff79c6',
        'while': '#ff79c6',
        'if': '#ff79c6',
        'else': '#ff79c6',
        'try': '#ff79c6',
        'except': '#ff79c6',
        'finally': '#ff79c6',
        'return': '#bd93f9',
        'yield': '#bd93f9',
        'lambda': '#50fa7b'
    },
    # Original name settings - preserved exactly
    'name': {
        'attr': '#50fa7b',
        'builtin': '#ffb86c',
        'builtin_pseudo': '#ffb86c',
        'class': '#8be9fd',
        'class_variable': '#f8f8f2',
        'constant': '#bd93f9',
        'decorator': '#8be9fd',
        'entity': '#50fa7b',
        'exception': '#8be9fd',
        'function': '#50fa7b',
        'global_variable': '#f8f8f2',
        'instance_variable': '#f8f8f2',
        'label': '#50fa7b',
        'magic_function': '#50fa7b',
        'magic_variable': '#f8f8f2',
        'namespace': '#f8f8f2',
        'tag': '#ff79c6',
        'variable': '#ffb86c',
        # NEW: Extended name categories
        'parameter': '#f1fa8c',
        'self': '#8be9fd',
        'cls': '#8be9fd',
        'module': '#ffb86c',
        'property': '#50fa7b',
        'staticmethod': '#8be9fd',
        'classmethod': '#8be9fd',
        'local_variable': '#f8f8f2',
        'comprehension': '#f1fa8c'
    },
    # Original operator settings - preserved exactly
    'operator': {
        'symbol': '#ff79c6',
        'word': '#ff79c6',
        # NEW: Detailed operators
        'assignment': '#ff79c6',
        'comparison': '#ff79c6',
        'arithmetic': '#ff79c6',
        'bitwise': '#ff79c6',
        'logical': '#ff79c6',
        'membership': '#ff79c6',
        'identity': '#ff79c6'
    },
    # Original string settings - preserved exactly
    'string': {
        'affix': '#f1fa8c',
        'char': '#f1fa8c',
        'delimeter': '#f1fa8c',
        'doc': '#f1fa8c',
        'double': '#f1fa8c',
        'escape': '#f1fa8c',
        'heredoc': '#f1fa8c',
        'interpol': '#f1fa8c',
        'regex': '#f1fa8c',
        'single': '#f1fa8c',
        'symbol': '#f1fa8c',
        # NEW: Extended string types
        'raw': '#f1fa8c',
        'bytes': '#99c794',
        'unicode': '#f1fa8c',
        'format': '#f1fa8c',
        'fstring': '#99c794'
    },
    # NEW: Your original number section - preserved exactly
    'number': {
        'binary': '#bd93f9',
        'float': '#bd93f9',
        'hex': '#bd93f9',
        'integer': '#bd93f9',
        'long': '#bd93f9',
        'octal': '#bd93f9',
        # NEW: Additional number types
        'complex': '#bd93f9',
        'scientific': '#bd93f9',
        'nan': '#ff5555',
        'inf': '#ffb86c'
    },
    # NEW: Your original comment section - preserved exactly
    'comment': {
        'hashbang': '#6272a4',
        'multiline': '#6272a4',
        'preproc': '#ff79c6',
        'preprocfile': '#f1fa8c',
        'single': '#6272a4',
        'special': '#6272a4',
        # NEW: Extended comments
        'docstring': '#6272a4aa',
        'todo': '#f1fa8c',
        'fixme': '#ffb86c',
        'note': '#8be9fd',
        'hack': '#ff5555',
        'xxx': '#ff79c6'
    },
    # NEW SECTIONS: Advanced features for rich IDE experience
    'ui': {
        'statusbar_bg': '#21222c',
        'statusbar_fg': '#f8f8f2',
        'tab_active_bg': '#6272a4',
        'tab_inactive_bg': '#44475a',
        'menu_bg': '#282a36',
        'menu_fg': '#f8f8f2',
        'menu_hover': '#44475a',
        'tooltip_bg': '#3e4452',
        'tooltip_fg': '#f8f8f2'
    },
    'font': {
        'family': 'Fira Code, JetBrains Mono, Consolas, monospace',
        'size': 12,
        'line_height': 1.5,
        'ligatures': True,
        'italic_comments': True,
        'bold_keywords': False,
        'bold_functions': True
    },
    'effects': {
        'selection_opacity': 0.8,
        'inactive_fade': 0.6,
        'blink_caret': True,
        'smooth_scroll': True,
        'overscroll': '#282a36',
        'drop_marker': '#ff79c6'
    },
    'debug': {
        'breakpoint': '#ff5555',
        'breakpoint_disabled': '#6272a4',
        'current_line_debug': '#ff79c6aa',
        'stack_frame': '#8be9fd44'
    },
    'autocomplete': {
        'bg': '#44475a',
        'fg': '#f8f8f2',
        'selected_bg': '#ff79c6',
        'selected_fg': '#282a36',
        'docs_bg': '#21222c',
        'docs_fg': '#f8f8f2'
    }
}

mariana = {'editor': {'bg': '#343d46', 'fg': '#8be9fd', 'select_bg': '#4e5a65', 'select_fg': '#d8dee9', 'inactive_select_bg': '#4e5a65', 'caret': '#f9ae58', 'caret_width': 1, 'border_width': 0, 'focus_border_width': 0}, 'general': {'comment': '#a6acb9', 'error': '#f9ae58', 'escape': '#d8dee9', 'keyword': '#c695c6', 'name': '#f9ae58', 'string': '#99c794', 'punctuation': '#5fb4b4'}, 'keyword': {'constant': '#c695c6', 'declaration': '#c695c6', 'namespace': '#c695c6', 'pseudo': '#c695c6', 'reserved': '#c695c6', 'type': '#c695c6'}, 'name': {'attr': '#c695c6', 'builtin': '#6699cc', 'builtin_pseudo': '#ec5f66', 'class': '#f9ae58', 'class_variable': '#d8dee9', 'constant': '#d8dee9', 'decorator': '#6699cc', 'entity': '#6699cc', 'exception': '#6699cc', 'function': '#5fb4b4', 'global_variable': '#d8dee9', 'instance_variable': '#d8dee9', 'label': '#6699cc', 'magic_function': '#6699cc', 'magic_variable': '#d8dee9', 'namespace': '#d8dee9', 'tag': '#f97b58', 'variable': '#5fb4b4'}, 'operator': {'symbol': '#f97b58', 'word': '#f97b58'}, 'string': {'affix': '#99c794', 'char': '#99c794', 'delimeter': '#99c794', 'doc': '#99c794', 'double': '#99c794', 'escape': '#99c794', 'heredoc': '#99c794', 'interpol': '#99c794', 'regex': '#99c794', 'single': '#99c794', 'symbol': '#99c794'},
            'number': {'binary': '#f9ae58', 'float': '#f9ae58', 'hex': '#f9ae58', 'integer': '#f9ae58', 'long': '#f9ae58', 'octal': '#f9ae58'}, 'comment': {'hashbang': '#a6acb9', 'multiline': '#a6acb9', 'preproc': '#c695c6', 'preprocfile': '#99c794', 'single': '#a6acb9', 'special': '#a6acb9'}}
monokai = {'editor': {'bg': '#282923', 'fg': '#8be9fd', 'select_bg': '#48473d', 'select_fg': '#f8f8f2', 'inactive_select_bg': '#48473d', 'caret': '#f8f8f2', 'caret_width': 1, 'border_width': 0, 'focus_border_width': 0}, 'general': {'comment': '#74705d', 'error': '#f92472', 'escape': '#d8dee9', 'keyword': '#f92472', 'name': '#a6e22c', 'string': '#e7db74', 'punctuation': '#f92472'}, 'keyword': {'constant': '#ac80ff', 'declaration': '#f92472', 'namespace': '#f92472', 'pseudo': '#ac80ff', 'reserved': '#f92472', 'type': '#f92472'}, 'name': {'attr': '#a6e22c', 'builtin': '#67d8ef', 'builtin_pseudo': '#fd9621', 'class': '#a6e22c', 'class_variable': '#a6e22c', 'constant': '#f8f8f2', 'decorator': '#67d8ef', 'entity': '#a6e22c', 'exception': '#67d8ef', 'function': '#a6e22c', 'global_variable': '#a6e22c', 'instance_variable': '#a6e22c', 'label': '#a6e22c', 'magic_function': '#67d8ef', 'magic_variable': '#a6e22c', 'namespace': '#f8f8f2', 'tag': '#f92472', 'variable': '#f92472'}, 'operator': {'symbol': '#f83535', 'word': '#f92472'}, 'string': {'affix': '#e7db74', 'char': '#e7db74', 'delimeter': '#e7db74', 'doc': '#e7db74', 'double': '#e7db74', 'escape': '#e7db74', 'heredoc': '#e7db74', 'interpol': '#e7db74', 'regex': '#e7db74', 'single': '#e7db74', 'symbol': '#e7db74'},
            'number': {'binary': '#ac80ff', 'float': '#ac80ff', 'hex': '#ac80ff', 'integer': '#ac80ff', 'long': '#ac80ff', 'octal': '#ac80ff'}, 'comment': {'hashbang': '#74705d', 'multiline': '#74705d', 'preproc': '#f92472', 'preprocfile': '#e7db74', 'single': '#74705d', 'special': '#74705d'}}
