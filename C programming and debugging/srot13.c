#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int rot13cmp(char const *a, char const *b)
{
  int i = 0;
 
  while(1)
    {
      int f = a[i];
      int s = b[i];

      if (a[i] == 10 && b[i] == 10)
	return 0;
      else if (a[i] == 10)
	return -1;
      else if (b[i] == 10)
	return 1;

      if ((a[i] >= 64 && a[i] <= 77) || (a[i] >= 97 && a[i] <= 109))
	f += 13;
      else if ((a[i] >= 78 && a[i] <= 90) || (a[i] >= 110 && a[i] <= 122))
	f -= 13;
      if ((b[i] >= 64 && b[i] <= 77) || (b[i] >= 97 && b[i] <= 109))
	s += 13;
      else if ((b[i] >= 78 && b[i] <= 90) || (b[i] >= 110 && b[i] <= 122))
	s -= 13;

      int d = f - s;
      if ( d != 0)
	return d;

      i++;
    }
}

int cmp(const void *a, const void *b)
{  return rot13cmp(*(const char **)a, *(const char **)b);
}
int main()
{
  int buffer_size = 2048;
  int counter = 0;
  int n_newline = 0;
  char *input = (char*) malloc(sizeof(char) * buffer_size);

  if (input == NULL)
    {
      fprintf(stderr, "Error allocating memory.");
      exit(1);
    }

  int c = 0;
  while(1)
    {
      c = getc(stdin);
      if ( c == EOF)
	break;
      
      input[counter] = (char) c;
      counter++;

      if (counter == buffer_size)
	{
	  input = (char*) realloc(input, buffer_size * 2);
	  if (input == NULL)
	    {
	      fprintf(stderr, "Error reallocating memory.");
	      exit(1);
	    }
	  buffer_size *= 2;
	}
    }
  
  if (counter == 0)
    exit(0);
  
  if (input[counter -1] != '\n')
    {
      if (counter == buffer_size)
	{
	  input = (char*) realloc(input, buffer_size * 2);
	  if (input == NULL)
	    {
	      fprintf(stderr, "Error reallocating memory.");
	      exit(1);
	    }
	  buffer_size *= 2;
	}
      input[counter] = '\n';
      counter++;
    }
  
  
  for (int k = 0; k < counter; k++)
    {
      if (input[k] == '\n')
	n_newline++;
    }

  char **helper = (char**)malloc(sizeof(char*) * counter);
  if (helper == NULL)
    {
      fprintf(stderr, "Error allocating memory.");
      exit(1);
    }

  char *pointer = input;
  int pos = 0;
  for (int i = 0; i < n_newline; i++)
    {
      if ( i == 0 && *pointer == '\n')
	{
	  helper[pos] = pointer;
	  pos++;
	  i++;
	  pointer++;
	}
      helper[pos] = pointer;
      pos++;
      while (*pointer != '\n')
	pointer++;
      pointer++;
    }

  qsort(helper, n_newline, sizeof(char*), cmp);

  char *temp;
  for (int k = 0; k < n_newline; k++)
    {
      temp = helper[k];
      while (*temp != '\n')
	{
	  printf("%c", *temp);
	  temp++;
	}
      printf("%c", *temp);
    }

  free(input);
  free(helper);
  return 0;

}
