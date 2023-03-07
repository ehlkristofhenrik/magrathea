# Project Magrathea

A new experimental way to do linear regression.

It uses a destructive algorithm for finding the best fit line out of the points.
It uses basic vector math to get 2 points.
The implementation is incorrect, but I am lazy. Deal with it.
It has O(kn^2) complexity == gradient descent (if I am correct).
The data has to be homogenious, but in theory works well discriminating outliers.
Not much tested, works on paper.
Enjoy!

I am afraid the project is a mess,
you can find the project on the master branch.

Contents:

magrathea/
  Science: second implementation
  project_magrathea: very first implementation
  magrathea_cs: third, Pythonic implementation
  ParticleSimulation: Godot engine project for visualization

TODO:
* Clean up code, folders, etc.
* Write documentation / paper
* Port it to the GPU/Multithreading
* Think of a better name
