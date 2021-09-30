# xyz_there

# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(s):
    is_found = False

    for i in range(len(s) - 2):
        if s[i] + s[i+1] + s[i+2] == 'xyz' and (s[i-1] != '.' or i == 0):
            is_found = True
            break

    return is_found
