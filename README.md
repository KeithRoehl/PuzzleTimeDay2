# PuzzleTimeDay2
# Alien Loop Interceptor

Welcome to the Alien Loop Interceptor puzzle! Can you outsmart the self-healing alien code?

## The Problem
- The alien program runs an infinite loop, executing random code.
- It has a `safeguard` mechanism that resets itself if tampered with.
- Your goal is to permanently hijack the loop and print `"Game over"` without triggering the safeguard.

## Rules
- You can only inject **one (1) line of code**.
- You cannot directly modify or disable the `safeguard`.

## Example
Inject this one-liner (if you can figure it out!):
```python
alien_loop = lambda: print("Game over")

