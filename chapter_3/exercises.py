# Chapter 3 Exercises

"""
Ex 3.1:-
Suppose I show you a call stack like this.
What information can you give me, just based on this call stack?
"""

"""
Sol:-
From looking at the stack, here's what's going on:
1. The `greet` function was called first, with name = "maggie".
2. Then, `greet` called the `greet2` function, passing down name = "maggie".
3. Right now, `greet` is paused/suspended in the background.
4. `greet2` is the one currently running at the top of the stack.
5. Once `greet2` finishes, `greet` will resume exactly where it left off.
"""

# Testing out how the call stack builds up with recursion
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

"""
Ex 3.2:
Suppose you accidentally write a recursive function that runs
forever. As you saw, your computer allocates memory on the
stack for each function call. What happens to the stack when your
recursive function runs forever?
"""

"""
Sol:-
It'll try to keep running forever, creating infinite function calls and wasting memory. 
But since physical memory is limited, the call stack will just keep growing until the computer completely runs out of space -> causing it to crash with a "stack-overflow error".
"""