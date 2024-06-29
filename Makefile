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
lint:
	poetry run flake8 brain_games

.PHONY: install brain-games build publish package-install
