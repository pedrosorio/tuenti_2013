For each script, parse it, identifying the (integer) position of fixed (ordered) scenes and the conditions for the "floating" ones (smaller or larger than an integer).

Run the check function on each scene, which takes the position and conditions for the scene and returns -1 if the position and conditions conflict, the position if the scene is possible and the possible interval if the scene has no fixed position.

Finally, run the overlaps function with all the points and intervals, returning valid if they overlap (i.e. scenes can have different orders) and the scene order if they don't overlap. 