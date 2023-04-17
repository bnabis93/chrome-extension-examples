PYTHON=3.9
BASENAME=$(shell basename $(CURDIR))

env:
	conda create -n $(BASENAME) -y python=$(PYTHON) $(addprefix -c ,$(CONDA_CH))

setup:
	pip install -r requirements.txt