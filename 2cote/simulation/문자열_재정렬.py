# 문자열
s = input()
result = []
total = 0
for c in s:
    if c >= 'A' and c <= 'Z':
        result.append(c)
    else:
        total += int(c)
result.sort()
result.append(str(total))
result = ''.join(result)
print(str(result))