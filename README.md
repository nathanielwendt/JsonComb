# JsonComb
Inspired by having to manually create config files in JSON that enumerated all possible values that I wanted, I decided to create a way to denote many item combinations in a compact form.  The idea is simple:

Write this:

```json

{
   "name": "basic",
   "count": ["!C",1,2],
   "type": ["!C","mobility","cabs"]
}

```

And JsonComb will turn it into this:

```json

[{
   "name": "basic",
   "count": 1,
   "type": "mobility"
},
{
   "name": "basic",
   "count": 1,
   "type": "cabs"
},
{
   "name": "basic",
   "count": 2,
   "type": "mobility"
},
{
   "name": "basic",
   "count": 2,
   "type": "cabs"
}]

```

Check out the tests for more examples, like nesting!


###Usage

#####Source Directly:

```python
from comb import find_tokens
result_obj = find_tokens(source_obj)
```

#####Utility (JSON file processing) Source:

```python
from utility import expand
expand(source_file, True)
```

#####Utility (JSON file processing) Command Line:

```python utility.py source.json output.json```

or

```python utility.py source.json output.json showres```

to display (in the terminal) the result


###A Note on Ordering

You probably noticed that JsonComb takes a regular obj and turns it into a list of items (each combination being a list item).  Ordering might be important in an application and in JsonComb it is enforced alphabetically.  So if you have 3 keys for value expansion:

```json

{
   "alpha": ["!C",1,2],
   "zeta": ["!C","one","two"],
   "charlie": ["!C","a","b"]
}

````

The first item is alpha in the ordering so the combinations will be as follows:

```
alpha | charlie | zeta
  1        a       one
  1        a       two
  1        b       one
  1        b       two
  2        a       one
  2        a       two
  2        b       one
  2        b       two
```
  
Note that the first alphabetic key is fixed for as long as the other values vary.

###Roadmap

- Allow for customizable ordering (not just alphabetical as current default)
- More robust test suite
