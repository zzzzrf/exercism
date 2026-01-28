def flatten(iterable):
    ans = []
    for item in iterable:
        if isinstance(item, list):
            ans.extend(flatten(item))
        elif item is not None:
            ans.append(item)
    return ans
