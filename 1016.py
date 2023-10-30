min, max = map(int, input().split())

#에라토스테네스의 체 사용
answer = max - min + 1
divisibleByTheSquare = [False] * (max-min+1)

for i in range(2, int(max**0.5+1)):
    square = i**2
    for j in range((((min-1)//square)+1)*square, max+1, square):
        #min보다 크면서 가장 작은 square의 배수를 시작지점을 맞춰주기 위한 for문
        #ex) 10부터 100까지라고 한다면 
        #   4의 배수를 12부터 삭제해나가기 시작 12, 16, 20, ...
        
        #   9의 배수를 18부터 삭제해나가기 시작 18, 27, ...
        if not divisibleByTheSquare[j-min] :
            divisibleByTheSquare[j-min] = True
            answer -= 1
print(answer)