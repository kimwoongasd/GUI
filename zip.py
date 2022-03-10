kor = ['사과', '바나나', '오렌지']
eng = ['apple', 'banana', 'orange']

# zip : 세로로 합쳐짐
print(list(zip(kor, eng)))

# 합친것을 분리
# 각 항목에 1번쨰 2번쨰 끼리 분히됨
mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)