%pre --interpreter /usr/bin/python

import os, sys

def set_tty(n):
    f = open('/dev/tty%d' % n, 'a')
    os.dup2(f.fileno(), sys.stdin.fileno())
    os.dup2(f.fileno(), sys.stdout.fileno())
    os.dup2(f.fileno(), sys.stderr.fileno())

def my_setup_screen():
    
    from snack import SnackScreen, CheckboxTree, Grid, Label, Entry, Button, GridForm
    
    pkglist = [
        ("Personal Recorder", "s2srecorder"),
        ("Fax Spool", "s2sfaxspool"),
        ("Cti Link", "s2sctilink"),
        ("Cdr Extractor", "s2scdrextractor"),
        ("IVR", "s2sivr")
        ]
    screen = SnackScreen()

    form = GridForm(screen, 'Select package set', 1, 4)
    g = CheckboxTree(5)
    for e in pkglist:
        g.append(e[0], e[1])
    form.add(g, 0, 1)
    form.add(Button('OK'), 0, 2)

    result = form.runOnce()
    r = g.getSelection()
    screen.finish()
    return r


set_tty(1)
r = my_setup_screen()
set_tty(3)

f = open("/tmp/extra_pkg","w")
for i in r:
    f.write(i+"\n")
f.close()

%end
