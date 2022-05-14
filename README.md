# pyGIFpad
 Play gifs on your Novation Launchpad!
 Btw, animated webp is also supported
Tested on Launchpad pro and Launchpad S.

## Changes
### 14.05.2022
v. 0.3 :
- Ableton Link Support
- Midi CLK support
## Demo


https://user-images.githubusercontent.com/1131462/161610433-f0b7b50e-edab-4df5-824a-cc65f0094c23.mp4


## Requirements
* Python 3
### Packages:
* pygame
* launchpad_py
* numpy
* pillow
* link (if you want to use Ableton Link support)
* rtmidi (if you want to use RTMidi support)

## Configuration parameters
```ini
launchpad_type=1
```
Selects launchpad for animation. All available devices listed in ini (but not all were tested). 


```ini
sync_mode = midi
```
Selects sync mode. Can be one of these values: 
* auto - redraws launchpad in the fixed amount of time
* ableton_link - sync redraw through Ableton Link
* midi - sync redraw trough MIDI


```ini
ableton_bpm = 120
```
Used only when sync_mode "ableton_link" is used. Start value of ableton BPM. (it changes after syncing in a fact)

```ini
midi_device_id = 6
```
Used only when sync_mode = "midi". Midi device to receive input CLK signal. If id was wrong, shows available midi devices with id to help and quits:
```
Midi Port Not Found. Available Ports:
['Arturia MiniLab mkII 0', 'Focusrite USB MIDI 1']
```

```ini
midi_sync_time = 0.25
```
Used only when sync_mode = "midi" or "ableton_Link" . Describes speed of changing frames. In beats for "ableton_link" and in seconds for "midi".

``ini
midi_sync_start = 1
```
Used only when sync_mode = "midi". Starts animation only when "start" midi command received

`` 
midi_sync_stop = 1
```
Used only when sync_mode = "midi" .Stops animation only when "stop" midi command received.


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

