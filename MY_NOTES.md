 ## 01-03. datetimes  
 - Fairly simple. Remember there are a few *gotchas* like `timedelta` which have **seconds** and **days** attributes but the seconds can only hold 
 ## 04-06. collections  
 - `defaultdict` is pretty cool. Initialise it with an additional parameter to be used as the default type so it can be initialised automatically (see the additional `__missing__()` function that they have). Otherwise it's just the same as a normal `dict`. Nb that this **doesn't** mean that the values in the `defaultdict` all have to be the same type.
 - Downloaded some data from kaggle to play with
 ## 07-09. datastructures  
 - Straightforward but interesting use of chain.from_iterables to flatten a list of lists. Also the more obscure `sum(cars.values(), [])`
 ## 10-12. pytest.  
 - Some great examples of simple games and how to test them. Need to go back and look at this more carefully. 
 