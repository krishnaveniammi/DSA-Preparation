def is_balanced(s):
    stack = []  # stack for brackets
    # dictionary for mapping
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            stack.append(char)  # push opening bracket
        elif char in ")}]":
            if not stack:  # stack empty but found closing
                return False
            if stack[-1] == pairs[char]:
                stack.pop()  # matched, so remove from stack
            else:
                return False  # mismatch
    return len(stack) == 0  # balanced if empty


# Test cases
print(is_balanced("()"))        # ✅ True
print(is_balanced("({[]})"))    # ✅ True
print(is_balanced("({[})"))     # ❌ False
print(is_balanced("((("))       # ❌ False
print(is_balanced("()[]{}"))    # ✅ True