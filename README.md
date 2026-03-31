# tulyp (fork)

![screenshot](https://raw.githubusercontent.com/vnc1/tulyp/refs/heads/main/images/screenshot.png)

`tulyp` is a program that displays the lyrics of the currently playing song in your terminal.
It checks for lyrics from 3 sources: genius.com, google.com, and azlyrics.com

tulyp only works with music players which are compliant with the [MPRIS](https://wiki.archlinux.org/title/MPRIS) specification.

Lyrics are displayed in a curses window. You can use <kbd>j</kbd> and <kbd>k</kbd> or <kbd>↑</kbd> and <kbd>↓</kbd> to scroll one line at a time. You can also use the scroll wheel in terminal emulators that support it.

Lyrics are saved to `XDG_CACHE_HOME/tulyp/artist-title` (default: `~/.cache/tulyp/artist-title`).
If there are cached lyrics for a song, no queries will be executed.

tulyp checks what song is playing and automatically reloads itself to show the appropriate lyrics.
You can switch between lyrics sources with number keys:

* 1 - Genius
* 2 - Google
* 3 - AZlyrics

## Dependencies (they will be installed with `tulyp`)

* `beautifulsoup4` to extract lyrics from HTML
* `dbus-python` to get the currently playing song through dbus
* `lyricsgenius` provides API to get lyrics from genius.com
* `requests` to search for lyrics on Google

Audio player detection now uses D-Bus (MPRIS) instead of `psutil`. As a result, `psutil` has been removed as a dependency.

## Installation

```shell
git clone https://github.com/vnc1/tulyp.git
cd tulyp
python -m build
pipx install dist/*.whl
```

## Use

If there is only one application playing audio, running `tulyp` will automatically select it.
Otherwise, specify which program you want. (eg: `tulyp cmus`, `tulyp spotify`, `tulyp resonance`...)


## Naming

* we got a terminal user interface -> tu
* we are dealing with lyrics       -> ly
* the program is written in python -> p

laszloszurok is so good at naming things.
