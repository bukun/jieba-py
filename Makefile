.PHONY: build test format docs html clean

build: run_helper clean test
	#rm -f dist/*
	python -m build
	# 或使用 PDM（如果安装了）
	# pdm build
html:
	cd docs && make html && sphinx-build -b html -D language=en . ../_build/html_en
test:
	pytest .
docstrfmt:
	docstrfmt -l 80 docs/*.rst
format:
	uvx ruff check --fix .
	uvx ruff format .
install: run_helper clean
	python3 -m pip install .
clean:
	rm -rf build dist *.egg-info _build/html
run_helper:
	python3 script_helper.py
sync:
	uv sync

pot:
	cd docs && sphinx-build -b gettext . _build/gettext

po: pot
	cd docs && sphinx-intl update -p _build/gettext -l en

