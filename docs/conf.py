# -- Import setup -------------------------------------------------------------

from os import path

# -- Project information ------------------------------------------------------

repository = 'docs-test'
project = 'Documentation Test Project'
copyright = '2024, Test Project'
author = 'Test Author'

# -- General configuration ----------------------------------------------------

extensions = [
    "sphinx.ext.todo",
    "adi_doctools"
]

needs_extensions = {
    'adi_doctools': '0.3'
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'

# -- External docs configuration ----------------------------------------------

interref_repos = ['doctools']

# -- Custom extensions configuration ------------------------------------------

hide_collapsible_content = True
validate_links = False

# -- todo configuration -------------------------------------------------------

todo_include_todos = True
todo_emit_warnings = True

# -- Options for HTML output --------------------------------------------------

html_theme = 'cosmic'
html_static_path = ['sources']
html_css_files = ["custom.css"]
html_favicon = path.join("sources", "scopy.png")

html_theme_options = {
    "light_logo": "logo.svg",
}

