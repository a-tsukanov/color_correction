Color correction software suite. Consists of:
* PyQt desktop app
* Flask web server for sharing presets
* Kotlin Android app for applying pre-made cloud presets (Repo is [here](https://github.com/a-tsukanov/color-correction-android))

Desktop app allows to define color substitution mapping on CIE Lab color space using a grid UI.
Simply speaking, you can color red items in the image into blue, so that they'll look natural - 
all shadows and highlights remain the same.

Here is hook it looks like:

![](ui_areas.png)
![](ui_grid_moved.png)
![](ui_menu.png)

# Installation

1. Create virtualenv for Python 3.6 (Might also work on 3.5 or 3.7, but not tested)
2. Install MongoDB (tested on 3.6.3)
3. To work with current db settings, create db `color_correction` with collection `grids`
4. Inside the virtual environment run `pip install -r requirements.txt`
5. Inside virtual env run `python run_desktop` for desktop app or `python run_backend` for backend.
