# JsonComb
Decorate JSON files according to JsonComb spec in order to automatically generate combinations of entries while still representing it in a short form.

Inspired by having to manually create config files in JSON that enumerated all possible values that I wanted tested, I decided to create a way to denote combination expansion in JSON.  The idea is simple:

```json

{
   "name": "basic",
   "count": ["!C",1,2,3],
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

