clean:
    pip uninstall delivery

install:
    pip install -e .['dev'] --upgrade --no-cache