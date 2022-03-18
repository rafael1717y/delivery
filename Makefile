clean:
    @find ./ -name '*.pyc' -exec rm -f {} \;
    @find ./ -name 'Thumbs.db' -exec rm -f {} \;
    @find ./ -name '*~' -exec rm -f {} \;
    rm -rf .cache
    rm -rf build
    rm -rf dist
    rm -rf *.
    pip uninstall delivery

install:
    pip install -e .['dev'] --upgrade --no-cache

test:
    pytest tests/ -v -cov=delivery