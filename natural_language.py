# todo: qualify on language? ambitious...
# this is likely going to be casework galore...


def plural(s, count=2):
    if count == 1:
        return s

    if s.endswith("s"):
        return f"{s}es"

    if s.endswith("y"):
        return f"{s[:-1]}ies"

    return f"{s}s"


def this_many(n, s):
    return f"{n} {plural(s, count=n)}"
