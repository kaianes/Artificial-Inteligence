######################
### Lab1 Exercises ###
#######################

### Exercise 1 — product or sum
def product_or_sum(a: int, b: int) -> int:
    prod = a * b
    return prod if prod <= 1000 else a + b

# demos
print("Exercise 1:")
print(product_or_sum(40, 20))  # 800
print(product_or_sum(50, 30))  # 80
print()

### Exercise 2 — sum of current and previous (first 10 numbers)
def sum_current_previous(n: int) -> None:
    previous = 0
    for i in range(n):
        current = i
        total = current + previous
        print(f"Current: {current}, Previous: {previous}, Sum: {total}")
        previous = current  

# demo
print("Exercise 2:")
sum_current_previous(10)
print()

### Exercise 3 — characters at even indices
def even_index_chars(s: str) -> str:
    # returns the characters concatenated; print as you prefer
    return s[0::2] # start:stop:step

# demo
print("Exercise 3:")
s = "PYTHON"
result = even_index_chars(s)
print(", ".join(f"'{c}'" for c in result))  # 'P', 'T', 'O'
print()

### Exercise 4 — remove first n characters
def remove_first_n_chars(s: str, n: int) -> str:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n > len(s):
        raise ValueError("n must be <= length of string")
    return s[n:]

# demo
print("Exercise 4:")
s = "Hello, World!"
print(remove_first_n_chars(s, 7))  # "World!"
print()

### Exercise 5 — first and last numbers are the same
def first_last_same(lst: list[int]) -> bool:
    return len(lst) > 0 and lst[0] == lst[-1]

# demos
print("Exercise 5:")
print(first_last_same([1, 5, 10, 1]))   # True
print(first_last_same([1, 5, 10, 20]))  # False
print()

### Exercise 6 — numbers divisible by 5 from a list
def divisible_by_five(lst: list[int]) -> list[int]:
    return [num for num in lst if num % 5 == 0]

# demo
print("Exercise 6:")
print(divisible_by_five([1, 10, 13, 15]))  # [10, 15]
print()

### Exercise 7 — count occurrences of a substring
def count_substring(main_str: str, sub_str: str) -> int:
    return main_str.count(sub_str)

# demo
print("Exercise 7:")
print(count_substring("hello world, hello universe", "hello"))  # 2
print()

### Exercise 8 — print number pattern
def print_number_pattern(n: int) -> None:
    for i in range(1, n + 1): # Start, end inclusive
        print(str(i) * i)

# demo
print("Exercise 8:")
print_number_pattern(5)
print()
    
### Exercise 9 — palindrome number check
def is_palindrome(num: int) -> bool:
    s = str(num)
    return s == s[::-1] # s[start:end:step]

# demo
print("Exercise 9:")
print(is_palindrome(121))  # True
print(is_palindrome(123))  # False
print()

# Exercise 10 — merge odds from list1 + evens from list2
def merge_odds_evens(list1 : list[int], list2 : list[int]) -> list[int]:
    odds = [num for num in list1 if num %2 != 0]
    evens = [num for num in list2 if num %2 == 0]
    return odds + evens


# demo
print("Exercise 10:")
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 80]
print(merge_odds_evens(list1, list2))  # [25, 35, 40, 60, 80]

if __name__ == "__main__":
    pass
