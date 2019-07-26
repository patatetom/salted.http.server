# salted.http.server

Python `http.server` with salt.

Python and its `http.server` module are a great way to occasionally provide a tree structure for downloading.

However, when the command `python3 -m http.server` popularized by many HowTo is used, the tree structure is offered to all winds without restriction !

`salted.http.server` adds a constraint to `http.server` that prevents the display of the offered tree structure if the salt grain is not present :
`curl http://publicIp:8000/` will work with `http.server` but will not work with `salted.http.server` where the computed salt should be added to the url (eg. `curl http://publicIp:8000/TheComputedSaltToAddHere/`)

**`salted.http.server` is primarily intended not to accidentally share data !**


### installation

- make tree directory in your local Python 3.X library with `mkdir -p ~/.local/lib/python3.X/site-packages/salted/http/`, `touch ~/.local/lib/python3.X/site-packages/salted/__init__.py` and `touch ~/.local/lib/python3.X/site-packages/salted/http/__init__.py`
- copy `server.py` in `~/.local/lib/python3.X/site-packages/salted/http/`
