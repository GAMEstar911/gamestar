# Gamestar

Gamestar is a lightweight Python toolkit and CLI for:

- scanning source files for common risky patterns,
- running scripts with friendly error explanations,
- printing short motivational prompts.

## Features

- `gamestar scan <file>`: highlights hardcoded passwords and dynamic execution calls.
- `gamestar run <file>`: executes a script and prints a human-readable error report on failure.
- `gamestar motivate`: prints one motivational message.

## Installation

### Local development install

```bash
pip install -e .
```

### Install from built wheel

```bash
python -m build
pip install dist/gamestar-*.whl
```

## CLI Usage

```bash
gamestar scan path/to/file.py
gamestar run path/to/file.py
gamestar motivate
```

## Python API

```python
from gamestar import scan_file, run_file, explain_error, motivate

scan_file("sample.py")
run_file("app.py")
print(explain_error(ValueError("bad value")))
motivate()
```

## Docker

Build:

```bash
docker build -t gamestar:latest .
```

Run scanner:

```bash
docker run --rm -v "$PWD:/workspace" gamestar:latest scan /workspace/path/to/file.py
```

Run debugger:

```bash
docker run --rm -v "$PWD:/workspace" gamestar:latest run /workspace/path/to/file.py
```

## Development

```bash
make install-dev
make test
make lint
```

## Publish to GitHub and PyPI

1. Push to GitHub:

```bash
git push -u origin main
```

2. Create an account on `https://pypi.org` and create a new project named `gamestar`.
3. In the PyPI project settings, add a trusted publisher:
Repository owner: `GAMEstar911`
Repository name: `gamestar`
Workflow name: `publish.yml`
Environment name: `pypi`

4. Tag a release:

```bash
git tag vX.Y.Z
git push origin vX.Y.Z
```

5. GitHub Actions will publish automatically to PyPI when the tag is pushed.
6. Install from PyPI:

```bash
pip install gamestar
```

## License

MIT. See `LICENSE`.
