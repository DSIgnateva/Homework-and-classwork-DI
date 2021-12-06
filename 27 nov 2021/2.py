s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

for i in range(len(s)):
    a = i + 10
    if s[i:a] in s[a:]:
        print(s[i:a])