all: exemple

fig:
	python3 src/main.py terrain.csv 50 0.0001 1000 opt
	python3 src/main.py terrain2.csv 50 0.0001 1000 opt
	python3 src/main.py terrain3.csv 50 0.0001 1000 opt
	python3 src/main.py terrain.csv 50 1000 0.0001 opt
	python3 src/main.py terrain2.csv 50 1000 0.0001 opt
	python3 src/main.py terrain3.csv 50 1000 0.0001 opt
	python3 src/main.py terrain.csv 50 0.0001 1000 close
	python3 src/main.py terrain2.csv 50 0.0001 1000 close
	python3 src/main.py terrain3.csv 50 0.0001 1000 close
	python3 src/main.py terrain.csv 50 1000 0.0001 close
	python3 src/main.py terrain2.csv 50 1000 0.0001 close
	python3 src/main.py terrain3.csv 50 1000 0.0001 close


exemple:
	python3 src/main.py terrain3.csv 50 0.0001 1000 opt
	python3 src/main.py terrain3.csv 50 1000 0.0001 opt
	python3 src/main.py terrain3.csv 50 0.0001 1000 close
	python3 src/main.py terrain3.csv 50 1000 0.0001 close

graph:
	python3 src/graph.py

world:
	python3 src/world.py
