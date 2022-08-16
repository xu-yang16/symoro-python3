SYMORO
======

SYOMRO is a software package for SYmbolic MOdeling of RObots.

This software package is developed as part of the OpenSYMORO project by
the robotics team at [IRCCyN][lk:irccyn] under the supervision of Wisama
Khalil.

For details on the algorithms used, please see [the paper][lk:hal]
published in the AIM 2014 conference.


Requirements (tested on Win10 and anaconda successfully)
------------
+ python (==3.8.13)
+ sympy (== 0.7.3)
+ numpy (>= 1.6.1)
+ wxPython (>= 2.8.12)
+ PyOpenGL (>= 3.0.1b2)


Getting Started
---------------
```bash
pip uninstall symoro -y
git clone https://github.com/xu-yang16/symoro-python3.git
cd symoro-python3
python setup.py develop
python bin/symoro-bin.py
```


Licence
-------
See [LICENCE][lk:licence].


Contributors
------------
See [Contributors][lk:contributors].


[lk:irccyn]: http://www.irccyn.ec-nantes.fr/
[lk:hal]: http://hal.archives-ouvertes.fr/hal-01025919
[lk:setup]: https://github.com/symoro/symoro/wiki/Setup
[el:aravind]: mailto:aravind.v@tum-create.edu.sg
[lk:licence]: https://github.com/symoro/symoro/blob/master/LICENCE
[lk:contributors]: https://github.com/symoro/symoro/graphs/contributors


