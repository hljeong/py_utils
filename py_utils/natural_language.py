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


def oxford(ts):
    ts = list(ts)
    match ts:
        case []:
            return ""

        case [t]:
            return t

        case [t1, t2]:
            return f"{t1} and {t2}"

        case [*ts, t]:
            return f"{', '.join(ts)}, and {t}"
