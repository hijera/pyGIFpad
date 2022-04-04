# pyGIFpad
 Play gifs on your Novation Launchpad!
 Btw, animated webp is also supported
Tested on Launchpad pro and Launchpad S.

##Requirements
* Python 3
###Packages:
* pygame
* launchpad_py
* numpy
* pillow

## Configuration parameters
```ini
launchpad_type=1
```
Selects launchpad for animation. All available devices listed in ini (but not all were tested). 

```ini
gif_folder=.
```
Directory with all gif/webp files.

```ini
defaultgif=name.gif
```
specifies gif by default. 

```
frame_time=0.03
```
describes delay per one frame in seconds. For example, 0.03 is about 30 fps. 
Minimal delay is limited by launchpad performance

## Specific configuration sections
Launchpad buttons can be used to switch between animations.
To use it, add section
```ini
[CONFIG_BUTTON_Y_X]
gif=filename.gif
```
where X and Y - coordinates of launchpad button , which will switch to animation filename.gif
Button coordinates equals to launchpad_py coordinates (look documentation at https://github.com/FMMT666/launchpad.py)

