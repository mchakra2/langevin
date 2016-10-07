===============================
langevin_dynamics
===============================


.. image:: https://img.shields.io/travis/mchakra2/langevin_dynamics.svg
        :target: https://travis-ci.org/mchakra2/langevin_dynamics

.. image:: https://readthedocs.org/projects/langevin-dynamics/badge/?version=latest
        :target: https://langevin-dynamics.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. image:: https://coveralls.io/repos/github/mchakra2/langevin_dynamics/badge.svg
	:target: https://coveralls.io/github/mchakra2/langevin_dynamics

.. image:: https://pyup.io/repos/github/mchakra2/langevin_dynamics/shield.svg
	:target: https://pyup.io/repos/github/mchakra2/langevin_dynamics/
	:alt: Updates




* Free software: MIT license
* Documentation: https://langevin-dynamics.readthedocs.io.


Features
--------

The aim of this project is to implement the equations governing the langevin dynamics. The Langevin equations are stochastic differential equations with two additional terms added to the Newtonian's second law equation.

.. math::
  ma=-\lambda v+\eta(t)-\frac{\partial U(x)}{\partial x}
  
  Where, -\lambda v: \text{Drag force and } \eta(t):\text{Random force}
  
  And, <\eta(t)\eta(t')> = 2T\lambda \delta(t-t')

The Langevin model accounts for the drag forces and the random forces that a system/particle experiences when it is in a solvent or a medium. The model is also capable of controlling temperature and can approximate the canonical ensemble.

Implementation Details
~~~~~~~~~~~~~~~~~~~~~~~

In this implementation of langevin dynamics, the Euler integration method has been used to update the position and the velocity at each time step. Default parameter values are coded in the **langevin_dynamics.py** file in **langevin_dynamics** sub-directory of the package. The user has to provide an input file named **input.txt** which contains the following information:


* Initial position
* Initial velocity
* Temperature
* Domain for periodic boundary condition    
* Damping coefficient
* Time step
* Total number of steps (Which determines total run time)
* Location of a Potential energy file
* Preferred path name for output file

The input file must be saved in the **IOFiles** subdirectory. The **IOFiles** subdirecroty already contains an example input file  and an example potential energy file. Please note that the keys identifying the parameters in the input file should not be altered. To run the script, clone the package by typing this in your command line:

git clone https://github.com/mchakra2/langevin_dynamics

Adjusted the **input.txt** file in **IOFiles** subdirectory to your liking. To run the langevin dynamics script, make sure you are in the main **langevin_dynamics** package directory (but out of the **langevin_dynamics** subdirectory!). Type the following:

python ./langevin_dynamics/__init__.py

You will find the output file containing the positions and velocities in the location that you have mentioned in **input.txt** file. If you did not specify the name and location of the output file, you will find the **output.txt**  file under subdirectory **IOFiles** (because that is the default output file location!).   

Credits
---------

* **Maghesree Chakraborty** - **mchakra2@ur.rochester.edu**
Special thanks to Dr. A White for being an excellent guide. 

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

