
# Program comparing benchmark

This is a script that analyses and compares various programs doing the same
thing against random inputs given as files. It works as follows:

* Generates some input files, according to the type specified in config.json.
* Compiles the programs using a custom Makefile, called Makefile.
* Runs each program against each input five times takes the average time of the
five iterations for each program and each input. 

It requires two files:
* Makefile, which is custom and must support build and clean methods
* config.json, which contains information about the programs being benchmarked



It has the following syntax:

`python3 benchmark.py [path to the directory] -(g)(b)(r)(c)`

where
* g, generates inputs
* b, calls make build
* r, runs the executables
* c, calls make clear



The config.json file has the following structure:

`{
    "programs": [
        program1
        program2
        .....
    ],
    "type": input type,
    "inputs": {
        .....
    }
}`

There are eight input file types:
- `int`, where the file contains a 31-bit unsigned integer
- `float`, where the file contains a 64-bit float
- `string`, where the file contains an ASCII string which can have spaces

 For these, each input looks like this:

> `{
>     "name": name,
>     "min": min,
>     "max": max
> }`

 where `min` is the minimum value (or length of the string) and `max` is the
 maximum value (or length of the string).

- `vector<int>`, where the file contains the number of elements on the first 
line and the 31-bit integer elements, separated by spaces, on the second line
- `vector<float>`, where the file contains the number of elements on the first 
line and the 64-bit float elements, separated by spaces, on the second line
- `vector<string>`, where the file contains the number of strings on the first
line and the strings, one per line

 For these, each input looks like this:

{
    "name": name,
    "min_length": min-length,
    "max_length": max-length,
    "min": min,
    "max": max
}`

 where `min_length` is the minimum length of the vector, `max_length` is the 
 maximum length of the vector, `min` is the minimum value (or length of the
 string) and `max` is the maximum value (or length of the string).

- `matrix<int>`, where the file contains the number of rows and the number of
columns on the first line and the rows, one row per line, with integer elements
separated by spaces
- `matrix<float>`, where the file contains the number of rows and the number of
columns on the first line and the rows, one row per line, with float elements
separated by spaces

 For these, each input looks like this:

`{
    "name": name,
    "min_rows": min-rows,
    "max_rows": max-rows,
    "min_cols": min-cols,
    "max_cols": max-cols,
    "min": min,
    "max": max
}`

 where `min_rows` is the minimum number of rows in the matrix, `max_rows` is
 the maximum number of rows in the matrix, `min_cols` is the minimum number 
 of columns in the matrix, `max_cols` is the maximum number of columns in the
 matrix, `min` is the minimum value (or length of the string) and `max` is the
 maximum value (or length of the string)
