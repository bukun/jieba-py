.PHONY: build test format docs html clean

build: clean test
	#rm -f dist/*
	python -m build
	# 或使用 PDM（如果安装了）
	# pdm build
html:
	cd docs && make html
test:
	pytest .
docstrfmt:
	docstrfmt -l 80 docs/*.rst
format:
	uvx ruff check --fix .
	uvx ruff format .
install: clean
	python3 -m pip install .
clean:
	rm -rf build dist *.egg-info _build/html

sync:
	uv sync --no-install-project
