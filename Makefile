# Makefile for 2Darti Game Engine

# Variables
PYTHON = python3
PIP = pip3
GAME_SCRIPT = main.py  # Main entry point of your game engine
VENV_DIR = venv  # Virtual environment directory

# Default target when running `make` with no arguments
.PHONY: all
all: install run

# Create a virtual environment (if not already created)
.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV_DIR)

# Install the dependencies
.PHONY: install
install: venv
	$(VENV_DIR)/bin/$(PIP) install -r requirements.txt

# Run the game engine (main.py)
.PHONY: run
run:
	$(VENV_DIR)/bin/$(PYTHON) $(GAME_SCRIPT)

# Clean up the virtual environment and other temporary files
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)

# Remove all Python bytecode files (.pyc and .pyo)
.PHONY: clean-pyc
clean-pyc:
	find . -name "*.pyc" -exec rm -f {} \;
