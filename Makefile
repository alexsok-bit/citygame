env = .venv
python = $(env)/bin/python
pip = $(env)/bin/pip

.PHONY: build run

build:
	python3 -m venv $(env_dir)
	$(pip) install -r requirements.txt
	$(python) get_cities.py
	$(python) extract_cities.py

run:
	$(python) main.py

clean:
	rm cities.html
