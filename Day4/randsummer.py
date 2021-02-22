# ranksummer.py
# example to run: mpiexec -n 4 python collective.py 10000
import numpy
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# initializing vars
number = numpy.zeros(1)
total = numpy.zeros(1)

# perform local computation. Each process integrates its own interval

number[0] = numpy.random.uniform(size)
print("Random number is %f" % (float(number[0])))
