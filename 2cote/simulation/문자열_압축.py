def compress(s, n):
    length = len(s)
    i = 0
    result = []
    count = 1
    while 1 :
        if i + n - 1 > length:
            result.append(s[i:])
            break
        s1 = s[i:i+n]
        s2 = s[i+n:i+n+n]
        if s1 == s2:
            count += 1
            i = i+n
        else:
            if count > 1:
                result.append(str(count))
                result.append(s1)
                i = i+n
                count = 1
            else:
                result.append(s1)
                i = i+n
                count = 1
    return result

def solution(s):
    answer = 1001
    n = int(len(s) / 2)
    if len(s) == 1:
        return 1
    for i in range(1, n + 1):
        answer = min(answer, len(''.join(compress(s, i))))
        # print(''.join(compress(s, i)), i)

    return answer

print(solution('a'))