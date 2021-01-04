 ## 01-03. datetimes  
 - Fairly simple. Remember there are a few *gotchas* like `timedelta` which have **seconds** and **days** attributes but the seconds can only hold 
 ## 04-06. collections  
 - `defaultdict` is pretty cool. Initialise it with an additional parameter to be used as the default type so it can be initialised automatically (see the additional `__missing__()` function that they have). Otherwise it's just the same as a normal `dict`. Nb that this **doesn't** mean that the values in the `defaultdict` all have to be the same type.
 - `Counter.most_common()` is pretty helpful. Have a look at `help(Counter)` for more examples
 - `ChainMap` was pretty cool. Basic usage seems to be to provide a list of mappings (think dictionaries - I didn't investigate what other mappings you could use) where items are retrieved based on a left to right priority. Nb that only the first (leftmost) mapping can be updated. So - you can add or update values in the first mapping and it will add or update that key to take precedence. E.g. `my_mapping['colour'] = 'red'` however if you tried to **delete** a mapping `del my_mapping['red']` you will get a KeyError if that mapping does not exist in the first mapping. You can also make child maps to effectively add another level of default.
 - Downloaded some data from kaggle to play with
 ## 07-09. datastructures  
 - Straightforward but interesting use of chain.from_iterables to flatten a list of lists. Also the more obscure `sum(cars.values(), [])`
 ## 10-12. pytest.  
 - Some great examples of simple games and how to test them. Need to go back and look at this more carefully. 
 