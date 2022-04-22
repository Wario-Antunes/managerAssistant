all: main.py
	python main.py

run: main.py
	python main.py < input.in

map2: main.py
	python3 main.py < map2test.in
