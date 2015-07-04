# JsonComb
Decorate JSON files according to JsonComb spec in order to automatically generate combinations of entries while still representing it in a short form.

Inspired by having to manually create config files in JSON that enumerated all possible values that I wanted tested, I decided to create a way to denote combination expansion in JSON.  The idea is simple:

```json

{
   "name": "basic",
   "count": ["!",1,2,3],
   "type": ["!","mobility,"cabs"]
}

```

```json

```

And JsonComb will turn it into this:
<code>
{
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
},


