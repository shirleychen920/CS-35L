HW7       --By Haojie Chen
----------------------------------------------------------------
In Brian Allen's SRT implementation, there are four for loops in the main
function. I realized that this is where I should modify and make it into
a function that uses parallelization.

From Vec3 to printf("\n"), I put all the content in a function called
multithread_func;it takes a parameter of the number of threads and divides
the image in columns according to the number of threads. In order for the
function to be able to access the variables "nthreads, scene", I make them
global variables. And in order for it to store the three colors that are needed
to be printed later, I create a struct called block which contains the three 
values. And I also create a pointer that points to the "blocks", so that later
when they are needed to be printed out at the end, they can be accesses easily.
All these modifications support the multithread-processing that allows ray-\
tracer to go through different sections of pixels concurrently.

I ran into two major problems. One was "cast to pointer from integer of 
different size" in the pthread_create function. I found out that the last
parameter it takes,( (void*)i ), converts int to void*. These two types 
actually have different sizes. The size of int is 2 bytes and for void* is 
4 bytes. So I changed the type of i to long, whose size is also 4 bytes.

Another problem was when deciding the partition size, (width/nthreads) could 
return a value smaller than the actual value when coverting the result to
integer. So when doing ray-tracing, the part that has been left off would not 
be traced. So when it is tracing the last section, I set the end of the 
section to width; this way it can be fully traced.

$ make clean check
Using this commands generates the following results: 
1 thread:
real  0m48.032s
user  0m48.029s
sys   0.0.003s

2 threads:
real  0m25.062s
user  0m48.541s
sys   0m0.003s

4 threads:
real  0m16.558s
user  0m48.152s
sys   0m0.001s

8 threads:
real  0m10.676s
user  0m50.052s
sys   0m0.003s


My version of SRT with multithread processes the image faster than the original
version. Basically it divides the original workload into several and processes
them at the same time. The more threads I use, the faster it goes since each
thread does less work. Using 8 threads is almost 5 times faster than using 
1 thread.

