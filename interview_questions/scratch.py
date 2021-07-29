if __name__ == '__main__':
    s = 'x'
    result = []
    for i in range(len(s)):
        mod = (ord(s[i]) + 4) % ord('a')
        result.append(chr(mod + ord('a')))
    print(result)
