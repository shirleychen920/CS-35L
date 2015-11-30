#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv)
{
  if (strlen(argv[1]) != strlen(argv[2]))
    {
      fprintf(stderr, "Not the same length.\n");
      exit(1);
    }
  int x;
  for (x = 0; x < strlen(argv[1]); ++x)
    {
      int y;
      for(y = x+1; y < strlen(argv[1]); ++y)
	{
	  if (argv[1][x] == argv[1][y])
	    {
	      fprintf(stderr, "Duplicate bytes.\n");
	      exit(1);
	    }
	}
    }

  
  char buffer;
  int found;
  while (read(0, &buffer, 1) > 0)
    {
      found = 0;
      int k;
      for (k = 0; k < strlen(argv[1]); ++k)
	{
	  if(buffer == argv[1][k])
	    {
     	      buffer = argv[2][k];
	      write(1, &buffer, 1);
	      found = 1;
	      break;
	    }
	}
      if (found == 0)
	{
	  write(1, &buffer, 1);
	}
    }
  return 0;
}
