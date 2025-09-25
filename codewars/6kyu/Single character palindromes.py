def solve(s):
    def check(s):
        split = int(len(s) / 2)
        if all(s[x] == s[-1-x] for x in range(split)):
            return True
        else:
            return False
    if check(s):
        return "OK"
    
    for i in range(len(s)):
        new_s = f"{s[:i]}{s[i+1:]}"
        if check(new_s):
            return "remove one"
    
    return "not possible"
        
