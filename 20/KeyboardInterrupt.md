

###  `KeyboardInterrupt` – What Is It?

**`KeyboardInterrupt`** is a built-in exception in Python that is raised **when the user interrupts program execution**, typically by pressing **Ctrl+C** (or **Cmd+C** on macOS) in the terminal.

---

###  Behavior

* Python raises `KeyboardInterrupt` when it receives the **SIGINT** signal (interrupt signal).
* It is a subclass of `BaseException`, **not** `Exception`, so it behaves differently when you use `except Exception`.

---

### Demo: Catching `KeyboardInterrupt`

```python
try:
    print("Press Ctrl+C to interrupt...")
    while True:
        pass  # Infinite loop
except KeyboardInterrupt:
    print("\nKeyboardInterrupt caught. Exiting gracefully.")
finally:
    print("Clean-up complete.")
```

 Output if you press Ctrl+C during the loop:

```
Press Ctrl+C to interrupt...
^C
KeyboardInterrupt caught. Exiting gracefully.
Clean-up complete.
```

---

###  Special Note:

If you use a **generic `except Exception`**, it will **not catch `KeyboardInterrupt`**:

```python
try:
    while True:
        pass
except Exception:
    print("This will NOT catch Ctrl+C")
```

 This won't catch the interrupt, because `KeyboardInterrupt` inherits from `BaseException`, not `Exception`.

---

###  If You Want to Catch *All* Errors, Including Interrupts:

```python
try:
    while True:
        pass
except BaseException as e:
    print("Caught:", type(e).__name__)
```

This will catch **everything**, including `SystemExit`, `KeyboardInterrupt`, etc. Use with caution—only if you really mean to handle all termination signals.

---

###  Should You Raise It Yourself?

Technically, yes—you can raise it like any exception:

```python
raise KeyboardInterrupt("Simulating Ctrl+C")
```

But it’s **unusual and discouraged** to manually raise `KeyboardInterrupt`. It’s meant to reflect an actual user-initiated interrupt.

Use it only if you're simulating signals or testing interrupt handlers.


