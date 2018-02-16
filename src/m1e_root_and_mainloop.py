"""
Example showing for tkinter and ttk:
  -- tkinter.Tk - the main (root) window
  -- The root window's mainloop - the Event Loop

A window should pop up.  That's all for this demo.

Authors: David Mutchler, Mark Hays, Michael Wollowswki, Matt Boutell,
         Chandan Rupakheti, Claude Anderson and their colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk  # Necessary in all but this trivial example.


def main():
    root = tkinter.Tk()
    root.mainloop() # kind of like a while loop. Waiting for events are common.

    print('Done with the Event Loop')  # Note when this line runs.
    # prints when the frame is closed.


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
