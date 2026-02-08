The strategy here will be to generate all the fibonacy numbers under 4 million, which can be done like this:

```python
a, b = 1, 2

# Generate Fibonacci numbers until we reach Number
while a <= NUMBER:
    print(a)  
    a, b = b, a + b

``` 
And then just apply a filter to only add to the counter the fibonacy numbers that are even, to iterate over all the numbers under 4 million we could either go with a for loop and put a if statement to break it when the number is bigger than 4 million or a while loop, which is an equivalent condition.