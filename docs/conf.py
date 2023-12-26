extensions = []

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Cookbook'
version = '1.0'
release = '1.0'
language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'perldoc'

todo_include_todos = False

html_theme = 'theme'
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'relations.html',
        'searchbox.html',
    ]
}

htmlhelp_basename = 'DjangoORMCookbookdoc'

latex_elements = {}

latex_documents = [
    (master_doc, 'DjangoORMCookbook.tex', 'Django ORM Cookbook Documentation',
     'Agiliq', 'manual'),
]

def setup(app):
    app.add_stylesheet('css/custom.css')

html_theme_options = {
    'display_version': False,
}

html_show_sphinx = False
