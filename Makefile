install:
	poetry install

brain-games:
	poetry run brain-games
build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pipx install --force dist/*.whl

.PHONY: install brain-games build publish package-install
