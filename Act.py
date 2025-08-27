# DFA 1: States = {a, b, f}, Start = a, Final = f
def dfa1(string):
    state = "a"
    path = [state]  # track the path
    for ch in string:
        if state == "a":
            if ch == "0":
                state = "a"
            elif ch == "1":
                state = "b"
            else:
                return False, path
        elif state == "b":
            if ch == "0":
                state = "f"
            elif ch == "1":
                state = "a"
            else:
                return False, path
        elif state == "f":
            if ch == "0":
                state = "b"
            elif ch == "1":
                state = "f"
            else:
                return False, path
        path.append(state)
    return state == "f", path


# DFA 2: States = {q0, q1, q2, q3}, Start = q0, Final = q3
def dfa2(string):
    state = "q0"
    path = [state]
    for ch in string:
        if state == "q0":
            if ch == "a":
                state = "q1"
            elif ch == "b":
                state = "q2"
            else:
                return False, path
        elif state == "q1":
            if ch == "a":
                state = "q0"
            elif ch == "b":
                state = "q3"
            else:
                return False, path
        elif state == "q2":
            if ch == "a":
                state = "q3"
            elif ch == "b":
                state = "q0"
            else:
                return False, path
        elif state == "q3":
            if ch == "a":
                state = "q2"
            elif ch == "b":
                state = "q1"
            else:
                return False, path
        path.append(state)
    return state == "q3", path

# Predefined Examples
dfa1_examples = [ "101", "1011", "11", "100", "101101", "111000"]
dfa2_examples = [ "babaa", "ababab", "abba", "baba", "bababa", "aababb"]

print("=== DFA 1 (Alphabet: {0,1}) ===")
for s in dfa1_examples:
    result, path = dfa1(s)
    status = "✅ ACCEPTED" if result else "❌ REJECTED"
    print(f"Input: {s:10} | Path: {' -> '.join(path):25} | {status}")

print("\n=== DFA 2 (Alphabet: {a,b}) ===")
for s in dfa2_examples:
    result, path = dfa2(s)
    status = "✅ ACCEPTED" if result else "❌ REJECTED"
    print(f"Input: {s:10} | Path: {' -> '.join(path):25} | {status}")


while True:
    print("\nChoose DFA to test:")
    print("1 - DFA 1 (binary: 0 and 1)")
    print("2 - DFA 2 (alphabet: a and b)")
    print("0 - Exit")

    choice = input("Enter choice: ")

    if choice == "0":
        break
    elif choice == "1":
        s = input("Enter a binary string (0/1): ")
        result, path = dfa1(s)
        print("Path:", " -> ".join(path))
        if result:
            print("✅ ACCEPTED by DFA 1")
        else:
            print("❌ REJECTED by DFA 1")
    elif choice == "2":
        s = input("Enter a string (a/b): ")
        result, path = dfa2(s)
        print("Path:", " -> ".join(path))
        if result:
            print("✅ ACCEPTED by DFA 2")
        else:
            print("❌ REJECTED by DFA 2")
    else:
        print("Invalid choice! Try again.")
