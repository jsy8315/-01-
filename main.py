array = [i for i in range(10)]

print(array)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i %2 == 1]
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1,10)]
print(array)

# N*M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

array[1][1] = 5
print(array)

# N*M 크기의 2차원 리스트 초기화 (잘못된 방법)
# 동일한 객체로 인식
n = 4
m = 3
array = [[0]*m]*n
print(array)

array[1][1] = 5
print(array)

# 리스트 관련 기타 메서드
a = [1,4,3]

print("기본 리스트: ", a)

# 리스트에 원소 삽입(맨뒤에 삽입)
a.append(2)
print("삽입: ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

# 내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬: ", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

# 특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3 추가: ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

a = [1,2,3,4,5,5,5]
remove_set = {3,5}
print(a)

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)