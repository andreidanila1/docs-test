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
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'

# -- todo configuration -------------------------------------------------------

todo_include_todos = True
todo_emit_warnings = True

# -- Options for HTML output --------------------------------------------------

html_theme = 'sphinx_rtd_theme'  # Using Read the Docs theme (more widely available)
html_static_path = ['sources']

# Basic theme options
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
}

# If you don't have the theme-specific files, comment out the next two lines
# html_css_files = ["custom.css"]
# html_favicon = path.join("sources", "scopy.png")