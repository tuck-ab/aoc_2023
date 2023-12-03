# Advent of Code 2023

My solutions for the [Advent of Code 2023](https://adventofcode.com/2023)

## Running the code

All library dependencies in `requirements.txt`. Run 

```$ pip install -r requirements.txt```

to install the dependencies.
Getting the solution for a given day and part is done using the following command.

```$ python main.py -d [daynumber] -p [partnumber]```

The inputs are sourced in the program and do not need to be seperatly downloaded. This
is done by using cookies which means that a file called `private.json` needs to be added
to contain the cookies from a given account to allow access the inputs. I am not going
to upload my cookies to this repo so `private.json` is also found in `.gitinore`. Your 
own cookies can be found by using inspect element and checking the cookies in the 
header when refreshing the one of the input pages, eg. 
([https://adventofcode.com/2023/day/1/input](https://adventofcode.com/2023/day/1/input)). 
The cookies that are needed are `_ga`, `_gid`, and `session` and should be stored in 
`private.json` in the following structure.

```
{
  "aoc_cookies`: {
    "_ga" : ...,
    "_gid" : ...,
    "session" : ...
  }
}
```

NOTE: I am fairly sure it is only the `session` cookie that is required but I have not
tested this so would recommend including all three.

## Structure of the solutions

Due to the way the entry points are called each day's solution needs to be in a
specific file `days/day[daynumber].py`. In the file there need to be two functions,
`part_1(input_data)` and `part_2(input_data)`. These are the functions that get called
when running the solution. These functions should `return` the values which will then
automatically get printed. The parameter `input_data` is the sourced input data which
has been split by line.
