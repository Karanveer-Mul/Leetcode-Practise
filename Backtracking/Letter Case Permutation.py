def backTrack(str1, str2, i):
    output = []
    if i == len(str1):
        return str2

    c = str1[i+1]

    if c.isalpha():
        output.append(backTrack(str1, str2+c.lower(), i+1))
        output.append(backTrack(str1, str2+c.upper(), i+1))
    else:
        output.append(backTrack(str1, str2+c, i+1))

    return output

s = "a1b2"

output = backTrack(s, "", 0)

print(output) 


