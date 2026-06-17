# EPCC HPC Summer School 2026

This page contains key dates and information for the EPCC HPC Summer
School 2026 from Saturday June 13th to Saturday June 27th.

For the HPC Summer School we're using material from a range of
existing courses so this is also a central page to help collect them all
together.

## Schedule

There will be scheduled sessions all-day from Monday to Friday over
both weeks. We have deliberately left the weekends and evenings free
so you can relax and explore Edinburgh **except** for group evening
meals on Saturday 13th and Friday 26th.

### Arrival / Departure

There will be a "get-together" meal (food and soft drinks provided) at
**7pm on Saturday 13th** at [Pizza Posto](https://pizzaposto.co.uk/):
16 Nicolson St, Edinburgh, EH8 9DH. This is less than 10 minutes' walk
from the flats in Darroch Court.

There will be a final meal at **7pm on Friday 26th** at The Canopy
Restaurant nearby at the Edinburgh Futures Institute.

### ACF Visit

We will be visiting the Advanced Computing Facility on the afternoon
of Wednesday 17th June. We will take taxis in 2 groups:

#### Group 1

* Abdul Mahdi
* Alice Seaman
* Callum Wright-Parish
* Cara Voysey
* Elliot Henton-Mitchell
* Jack Hill
* Klara Kurucova
* Mehul Bandhu

#### Group 2

* Nourdin Gaber Ibrahim
* Oskar Harber
* Rhea Bose
* Rommel Gregorio
* Sivanujan Sivapalan
* Syeda Nasir
* Taha Ahmed
* Ginny Douglas

While you are waiting / after you get back you will be working at the
desks in EPCC (Level 2 Bayes).

Group 1 will leave in 2 taxis (4 students + 1 staff in each taxi) from
Potterow, the main road just outside the Bayes lecture theatre, at
**13:15**; Group 2 will leave at **14:30**.

I expect that Group 1 will be back at Bayes just before 4pm; Group 2
back just after 5pm.

The address is: ACF Building, Edinburgh Technopole, Bush Estate,
Penicuik, EH26 0QA

Entry to the ACF is via a barrier – you need to buzz to be let through.

If there are any issues then contact me (David Henty) on: 07974 730432.



### Lectures

The standard day will run from 09.30 to 17:00 with an hour for lunch
around 13:00 and coffee/tea breaks mid-morning and mid-afternoon.

However, for the first day **Monday 15th** could you please arrive at
EPCC in the Bayes Building, 47 Potterrow, Edinburgh EH8 9BT, **at
09:00** to give us more time for introductions, admin tasks etc.

Lectures will take place in Bayes or Room 2.14 in the **Lister Learning
and Teaching Centre**, 5 Roxburgh Pl, Edinburgh EH8 9SU (this is about 5
minutes from Darroch Court).

Here is the schedule: in "Practical" sessions, students will work on
their own on exercises based on the lecture material, with an EPCC
staff member on hand to help. Note that all lecture sessions will also
have their own hands-on exercises - it is not just "chalk and talk"!

| Day | Morning (normally 9:30)  || Afternoon (normally 14:00) ||
| --- | ---|--  | --- |--|
| |  | |
| Mon 15 | Bayes (**arrive 09:00**) | Introductions / bash / git | Bayes | bash / git |
| Tue 16 | Bayes | Introduction to C |Bayes | Introduction to C |
| Wed 17 | Bayes | Introduction to HPC (i) | Bayes | ACF Visit / [Practical](https://github.com/davidhenty/sharpen) |
| Thu 18 | Bayes | Introduction to HPC (ii) | Bayes | Machine Learning (i)|
| Fri 19| Bayes | Machine Learning (ii) | Bayes | Practical |
| | | | | |
| Mon 22 | Lister | OpenMP for CPUs (i) | Lister |  OpenMP for CPUs (ii) |
| Tue 23 | Lister | OpenMP for CPUs (iii) | Lister | OpenMP for GPUs (i)  |
| Wed 24 | Lister | OpenMP for GPUs (ii)   | Bayes |  Practical |
| Thu 25 | Lister | Introduction to MPI (i)  | Lister |  Introduction to MPI (ii)  |
| Fri 26 | Bayes | HPC Guest Lectures | Bayes | Practical |

### Image sharpening example

The afternoon practical sessions (Wednesday and Friday) are a chance
for you to either catch up with the material from the first few days
(if it was new to you) or to work on a more substantial problem.

We will be using the **Image Sharpening example**.

For now this exercise illustrates a number of points:

 * an algorithm that does a significant amount of computation;
 * how to run a Python program on the ARCHER2 login node;
 * how to compile and run a C program on the ARCHER2 login node;
 * a comparison of the relative performance of C and (naively written) Python;
 * an opportunity to see a real C program (warts and all!).

You can find the image sharpening example at https://github.com/davidhenty/sharpen

The code loops over all the pixels in an image and applies a large
filter to each pixel that uses the values of the pixels in its near
vicinity (by default a 17x17 square).

On ARCHER2 you will need to load a module to get a suitable version of
Python: `module load cray-python`

To view the input and output images (fuzzy.pgm and sharpened.pgm), use `module load imagemagick` then `display fuzzy.pgm`. If you cannot get graphics
to work on your machine then you can copy the images back to your desktop, but you will have to convert then to a non-PGM format first. For example, on ARCHER2 you can
issue `convert fuzzy.pgm fuzzy.png`.

#### Timing

The code prints out times: the calculation time and the overall run time. The calculation time just measures how long it took to apply the filter to the image **excluding** the IO overheads of reading in the fuzzy image and writing out the sharpened one; the overall run time is the total time from start to finish. To find out how long was spent in IO just subtract the two.

#### Python example

To run the code:
````
module load cray-python
python ./sharpen.py
````

Things you might like to investigate:

*    How fast is the code on your laptop compared to the ARCHER2 login nodes?

*    If you want the program to run faster you can change the size of the smoothing filter - try reducing the value of `d` in `sharpenalg.py` from its default value d=8. How does the runtime vary with d? Can you understand this behaviour by looking at the code?

*    The program is deliberately written very simply and the performance can easily be improved. For example, the values of the (very time-consuming) function `filter()` could be pre-calculated and stored in an array. If you alter the code make sure that the output is still correct, e.g. by comparing the output image `sharpened.pgm` before and after your changes: they should be **identical**, i.e. `diff sharpened.pgm sharpened-reference.pgm` should show no differences (i.e. no output).

  #### C example

The C example is described in `doc/sharpen-cirrus.pdf` but note that
the *details are for the Cirrus system and this year we are using
ARCHER2.*

This sheet covers a lot of topics and assumes you have not used an HPC system before. The material in sections 3.6 to 3.8 is most relevant here: you can
skip most of the early sections. The instructions talk about downloading a tar file but you do not need to do this as you already have the source code from github.

To compile and run on the login nodes:
````
make
./sharpen
````

Things to look at include:

 *   Do you understand the code? The way 2D arrays are allocated using `malloc` is a little complicated - if you really want to know what is going on here then ask a demonstrator!
 *   How much faster is the compiled C version compared to the Python code?

### Parallel sharpen

Note that all parallel jobs **must be run from /work** so after logging in type:
````
cd /work/tc073/tc073/username/
````

This is an opportunity for you to investigate parallel scaling of the
image sharpening example as described in sections 3.10 onward.

#### Using the batch system

To run a job in the batch system (assuming you have compiled the code): `sbatch sharpen.slurm`

You can check the progress of jobs using: `squeue --me`

When complete, output will appear in a file called something like `slurm-1234567.out`

### Exercises

The default exercises are around looking at the scaling of the pure
MPI version and seeing if it follows Amdahl's law. You should:

  * plot graphs of speedup and parallel efficiency
  * see what value of alpha gives a good fit
  * check if this agrees with what you would estimate from the IO time

To change the number of processors, alter the values of `nodes`, `ntasks` and `tasks-per-node`.

If you want to look at Gustafson's law - larger problems scale better
- then increase the filter size by changing `d`, e.g. you could try
`d=10` or `d=14`.

