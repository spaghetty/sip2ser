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
        ("Fax Spool", "s2sfaxspool"),
        ("Cdr Extractor", "s2scdrextractor"),
        ("Mail Proxy", "s2smailproxy"),
	("Personal Recorder", "s2srecorder"),
        ("Italian Languages Support", "sipxlang-it")
        ]
    screen = SnackScreen()

    form = GridForm(screen, 'Select package set', 1, 6)
    g = CheckboxTree(6)
    for e in pkglist:
        g.append(e[0], e[1:])
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
for l in r:
    for i in l:
    	f.write(i+"\n")
f.close()

%end
