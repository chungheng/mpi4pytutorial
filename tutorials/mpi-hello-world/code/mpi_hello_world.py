# This code is based on `mpi_hello_world.c` in www.mpitutorial.com, originally
# written by Wes Kendall. The goal of this code is to provide a Python
# equivalent to the original C-based tutorial.
#
# This code depends on `mpi4py`, a Python wrapper of MPI.
#
# An intro MPI hello world program that uses MPI_Init, MPI_Comm_size,
# MPI_Comm_rank, MPI_Finalize, and MPI_Get_processor_name.
#

from mpi4py import MPI

if __name__ == "__main__":
    # Initialize the MPI environment. The two arguments to MPI Init are not
    # currently used by MPI implementations, but are there in case future
    # implementations might need the arguments.
    comm = MPI.COMM_WORLD

    # Get the number of processes
    size = comm.Get_size()

    # Get the rank of the process
    rank = comm.Get_rank()

    # Get the name of the processor
    processor_name = MPI.Get_processor_name()

    # Print off a hello world message
    print("Hello world from processor {}, rank {} out of {} processors".format(
         processor_name, rank, size))

    # MPI_Finalize() is registered (by using Python C/API function Py_AtExit())
    # for being automatically called when Python processes exit, but only if
    # mpi4py actually initialized MPI. Therefore, there is no need to call
    # MPI.Finalize() from Python to ensure MPI finalization.
