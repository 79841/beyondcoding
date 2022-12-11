#  집합
#  중복 x
#  순서 x
# 인덱싱 x

a = [1, 2, 3, 4]
b = [3, 4, 5]
s = set([1, 2, 3])

aS = set(a)
bS = set(b)

# print(set[0])


# 교집합
print(aS & bS)
print(aS.intersection(bS))

# 합집합
print(aS | bS)
print(aS.union(bS))

# 차집합
print(aS - bS)
print(aS.difference(bS))

# 추가
aS.add(100)
aS.update([10, 20, 30])
print(aS)

# 삭제
aS.remove(100)
print(aS)
