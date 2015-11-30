#!/usr/bin/python

"""
select or reject lines common to two files

Copyright 2005, 2007 Paul Eggert.
Copyright 2010 Darrell Benjamin Carbajal.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Please see <http://www.gnu.org/licenses/> for a copy of the license.

$Id: randline.py,v 1.4 2010/04/05 20:04:43 eggert Exp $
"""

import random, sys, locale, string
from optparse import OptionParser

class comm:
    def __init__(self, file1, file2):
      if file1 == 'std':
        self.lines1 = sys.stdin.readlines()
      else: 
        f1 = open(file1, 'r')
        self.lines1 = f1.readlines()
        f1.close()
      if file2 == 'std':
        self.lines2 = sys.stdin.readlines()
      else:
        f2 = open(file2, 'r')
        self.lines2 = f2.readlines()
        f2.close()
    
    def returnfile1(self):
        return self.lines1
    
    def returnfile2(self):
        return self.lines2


def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2

Select or reject lines common to two files."""

    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-1", "--supress1",
                      action="store_true", dest="supress1", default=False,
                      help="supress the first column")
    parser.add_option("-2", "--supress2",
                      action="store_true", dest="supress2", default=False,
                      help="supress the second column)")
    parser.add_option("-3", "--supress3",
                      action="store_true", dest="supress3", default=False,
                      help="supress the third column)")
    parser.add_option("-u", "--unsorted",
                      action="store_true", dest="unsorted", default=False,
                      help="take in unsorted files")

    options, args = parser.parse_args(sys.argv[1:])


    l = locale.getlocale()
    locale.setlocale(locale.LC_ALL, l)

    if len(args) != 2:
           parser.error("wrong number of operands")
    
    if args[0] == '-':
      input_file1 = 'std'
    else:
      input_file1 = args[0]
    if args[1] == '-':
      input_file2 = 'std'
    else:
      input_file2 = args[1]
    
    try:
        supress1 = bool(options.supress1)
        supress2 = bool(options.supress2)
        supress3 = bool(options.supress3)
        unsorted = bool(options.unsorted)
    except:
        parser.error("invalid argument")

    try:
        generator = comm(input_file1, input_file2)
        text1 = generator.returnfile1()
        text2 = generator.returnfile2() 
        i = 0
        j = 0
        if unsorted == False:
         while i < len(text1) and j < len(text2):  
           while i < len(text1) and (text1[i]< text2[j]):
               if supress1 == False:
                print(text1[i].rstrip())
               i = i + 1
               if i >= len(text1):
                 while j< len(text2):
                   if supress2 == False and supress1 == True:
                    print(text2[j].rstrip())
                   elif supress2 == False and supress1 == False:
                    print "\t", (text2[j].rstrip())
                   j = j + 1
                 break   
           while i < len(text1) and (text1[i] > text2[j]):
               if supress2 == False and supress1 == True:
                print (text2[j].rstrip())
               elif supress2 == False and supress1 == False:
                print "\t", (text2[j].rstrip())
               j = j + 1
               if j >= len(text2):
                 while i < len(text1):
                  if supress1 == False:
                   print (text1[i].rstrip())
                  i = i + 1 
                 break
           while i < len(text1) and j < len(text2) and (text1[i] == text2[j]):
               if ((supress1 == True and supress2 == False)\
or (supress1 == False and supress2 == True))\
 and supress3 == False:
                print "\t", (text1[i].rstrip())
               if supress1 == True and supress2 == True and supress3==False:
                print (text1[i].rstrip())
               if supress1 == False and supress2 == False and supress3 == False:
                print "\t", "\t", (text1[i].rstrip())
               j = j + 1
               i = i + 1
               if j >= len(text2):
                 while i < len(text1):
                  if supress1 == False:
                   print (text1[i].rstrip())
                  i = i + 1
                 break 
               if i >= len(text1):
                 while j < len(text2):
                  if supress1 == True and supress2 == False:
                   print (text2[j].rstrip())
                  elif supress2 == False and supress1 == False:
                   print "\t", (text2[j].rstrip())
                  j = j + 1
                 break
        if unsorted == True:      
         while i < len(text1) and j < len(text2):
          while i< len(text1) and j < len(text2) and text1[i] != text2[j]:
           if supress1 == False:
            print (text1[i].rstrip())
           i = i + 1 
           if i >= len(text1):
                 while j < len(text2):
                  if supress1 == True and supress2 == False:
                   print (text2[j].rstrip())
                  elif supress2 == False and supress1 == False:
                   print "\t", (text2[j].rstrip())
                  j = j + 1
                 break
          while i < len(text1) and j < len(text2) and text1[i] == text2[j]:
               if ((supress1 == True and supress2 == False)\
 or (supress1 == False and supress2 == True))\
 and supress3 == False:
                print "\t", (text1[i].rstrip())
               if supress1 == True and supress2 == True and supress3 == False:
                print (text1[i].rstrip())
               if supress1 == False and supress2 == False and supress3 == False:
                print "\t", "\t", (text1[i].rstrip())
               j = j + 1
               i = i + 1
               if j >= len(text2):
                 while i < len(text1):
                  if supress1 == False:
                   print (text1[i].rstrip())
                  i = i + 1
                 break 
               if i >= len(text1):
                 while j < len(text2):
                  if supress1 == True and supress2 == False:
                   print (text2[j].rstrip())
                  elif supress2 == False and supress1 == False:
                   print "\t", (text2[j].rstrip())
                  j = j + 1
                 break          
    except:
        parser.error("error")       
        

        
if __name__ == "__main__":
    main()


