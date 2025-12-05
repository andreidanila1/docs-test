# Documentation Test Project - doc

This project is a test setup for GitHub Pages documentation workflow, copied from the Scopy project.

## Structure

- `docs/` - Contains the Sphinx documentation source files
- `.github/workflows/generate_doc.yml` - GitHub Actions workflow for building and deploying documentation

## Usage

1. Push changes to the `main` branch to trigger documentation build
2. Documentation will be automatically deployed to GitHub Pages
3. Access the documentation at: `https://[username].github.io/docs-test/`

## Local Development

To build documentation locally:

```bash
cd docs
pip install -r requirements.txt
make html
```

The built documentation will be available in `docs/_build/html/`.

## Original Source

This project structure and workflow were copied from the [Scopy project](https://github.com/analogdevicesinc/scopy).
