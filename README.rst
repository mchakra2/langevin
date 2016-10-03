===============================
langevin_dynamics
===============================


.. image:: https://img.shields.io/travis/mchakra2/langevin_dynamics.svg
        :target: https://travis-ci.org/mchakra2/langevin_dynamics

.. image:: https://readthedocs.org/projects/langevin-dynamics/badge/?version=latest
        :target: https://langevin-dynamics.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/mchakra2/langevin_dynamics/shield.svg
	:target: https://pyup.io/repos/github/mchakra2/langevin_dynamics/
	:alt: Updates
.. image:: https://coveralls.io/repos/github/mchakra2/langevin_dynamics/badge.svg?branch=master
	:target: https://coveralls.io/github/mchakra2/langevin_dynamics?branch=master

	   The aim of this project is to implement the equations governing the langevin dynamics. The Langevin equations are stochastic differential equations with two additional terms added to the Newtonian's second law equation.  The Langevin model accounts for the drag forces that a system experiences when it is in a solvent or a medium. The model is also capable of controlling temperature and can approximate the canonical ensemble. For this project the Euler integration method has been used to update the position and velocity at each time step. Errors were encountered while trying to run tests on langevin_dynamics.py when class was used in the code. I tried commenting out that section and take a new approach without using classes. Tests were failing for pypy compiler, I decided to remove it as a tox environment. The unit tests check if the periodic boundary is working properly, whether random and damping forces are actually added for the langevin dynamics and if the force is the same as that read from the tabular potential file in absence of the damping force and the random force.


* Free software: MIT license
* Documentation: https://langevin-dynamics.readthedocs.io.


Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

