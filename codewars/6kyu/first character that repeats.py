def first_dup(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return s[i]
        else:
            None
