#WIP

def transpose(lines):
    transposed = []
    string = ''.join(lines)
    rows = string.split("\n")
    longest_row = len(sorted(rows, key=len)[-1])
    for i in range(0, longest_row):
        for row in rows:
            if len(row) >= i+1:
                transposed.append(row[i])
            else:
                transposed.append(" ")
        transposed.append('\n')
    if len(transposed) > 0:
        transposed.pop(-1)
    return ''.join(transposed)



print(transpose("ABC\nDE\nTYUVW"))
