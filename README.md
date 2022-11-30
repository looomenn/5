# Finding the power of a number that, in the congruent equation, equals 1 or -1 with given modulus

## Requirements

used match ( [PEP 636](https://peps.python.org/pep-0636/) ) 

To run script you need `python >=3.10`

## Sample Execution & Output

You can run the script from the command-line using

```cmd
python _power.py
```

Used math formula

```
 a ≅ b (mod m)
```

### Problem

Find the remainder from dividing:

$$2^{100} + 5^{200} : 29 \ (ex.)$$

As a result, we must convert the power of $\boldsymbol{100}$ and $\boldsymbol{200}$ to some normal numbers. According to the theory of division with remainder we need power of 2 (from ex.) when it is equal to 1 or -1, so we can replace it.

Additionaly, $\boldsymbol{A}$ is a firstly given number (base number), $\boldsymbol{P}$ is number that we want ( power of base number ) and $\boldsymbol{M}$ - modulus.

### Input

The first line of the input gives state of program output:

```
 0 - Limit On | 1 - Limit off | 2 - Debug + Limit on | 3 - Debug only
```

The second line gives the number of test cases, $\boldsymbol{T}$. $\boldsymbol{T}$ test cases follow. Each test case has a single line containing three integers, **_A_**, **_P_** and **_M_**, as described above.

> In program A = given_int; P = power; M = modulus

#### Limit ?

With this parameter, we can specify whether the program should stop at -1 / 1 or continue with the given power.

### Output

For each test case, output the first line containing Case #x: y, where x is the test case number (starting from 1) and y is a list that contains dictionary with possible replacable equations.

Output format

```
<give_int>^<power> ≅ <result_number> (mod M)
```

### Sample input

```
2
1
7 10 100
```

#### Input explanation

`2` - state 2 $\implies$ Debug + Limit
`1` - number of test cases
`7` - given $\boldsymbol{A}$
`10` - given $\boldsymbol{P}$
`100` - given $\boldsymbol{M}$

### Sample output

```shell
[DEBUG] operation: -     power: 3     old: 343   new: 243
[DEBUG] operation: -     power: 3     old: 243   new: 143
[DEBUG] operation: -     power: 3     old: 143   new: 43
[DEBUG] operation: -     power: 4     old: 301   new: 201
[DEBUG] operation: -     power: 4     old: 201   new: 101
[DEBUG] operation: -     power: 4     old: 101   new: 1
Case #1: [{'7^1 ≅ 7 (mod 100)'}, {'7^2 ≅ 49 (mod 100)'}, {'7^3 ≅ 43 (mod 100)'}, {'7^4 ≅ 1 (mod 100)'}]
```
