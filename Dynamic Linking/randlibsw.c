#include "randlib.h"
#include <stdio.h>
#include <stdlib.h>

/* Input stream containing random bytes.  */

extern FILE *urandstream;


__attribute__ ((__constructor__)) 
static void
rand64_init (void)
{
  urandstream = fopen ("/dev/urandom", "r");
  if (! urandstream)
    abort ();
}


extern unsigned long long
rand64 (void)
{
  unsigned long long int x;
  if (fread (&x, sizeof x, 1, urandstream) != 1)
    abort ();
  return x;
}


__attribute__ ((__destructor__)) 
static void
rand64_fini (void)
{
  fclose (urandstream);
}
