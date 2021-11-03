# Alora Desktop Enviroment 
	Alora DE or ADE aims to build a platform independent environment with integrated apps and widgets

## Requirements
* [python3](https://www.python.org/) >= 3.7
* [PyQt5](https://pypi.org/project/PyQt5/) or 
[PyQt6](https://pypi.org/project/PyQt6/) or 
[PySide](https://pypi.org/project/PyQt5/) or
[PySide6](https://pypi.org/project/PySide6/) 


## Getting Started
	clone this repo and run src/main.py
```bash
	git clone git@github.com:abhirajranjan/aloraDE
	python3 src/main.py 
```
## Run Whole Desktop
	simply run src/main.py without any args will run desktop interface by default
```bash 
python src/main.py
```
or 
```bash
python src/main.py --desktop
```

## Run Specific Widget
	simply run src/main.py with the widget package name that u want to run, include multiple if you want to run many. 
```bash 
python src/main.py wallpaper
```

## File Structure 
	Files in src/packages contains all the addon apps that can be used in the environment.

	All the packages that has to do with GUI can integrate src/shell.py in to include some pre UI things and some additional features within Qt.

	Alora DE also contains its own desktop to run as a complimantory desktop with existing one.

	Packages are builds in that way that they can be executed as a standalone widgets without its desktop interface.
