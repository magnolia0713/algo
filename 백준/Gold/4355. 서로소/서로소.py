import sys

data = sys.stdin.read().split()

for value in data:
    n = int(value)

    # 0이 입력되면 프로그램 종료
    if n == 0:
        break

    # n이 1인 경우 예외 처리
    if n == 1:
        print(0)
        continue

    result = n
    p = 2

    # 2부터 루트 n까지만 소인수 검사
    while p * p <= n:
        if n % p == 0:
            # p가 n의 소인수인 경우 n에서 p를 모두 제거
            while n % p == 0:
                n //= p
            # 오일러 피 함수 공식 적용
            result -= result // p
        p += 1

    # 반복문이 끝난 후 n이 1보다 크면 남아있는 n 자체가 소수
    if n > 1:
        result -= result // n

    # 결과 출력
    print(result)