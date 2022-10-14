# list1 = [x for x in range(10)]
#
# print(list1)
#
# ## 1번 코드 -> 일반 코드
# s = 'walrus eat kimchi'  ## s에 문자열을 할당
# result = 'walrus' in s  ## 'walrus' in s를 result에 할당
# if result:  ## result가 True라면
#     print(s)  ## s 출력
#     print(result)  ## result 출력
#
# ## 2번 코드 -> := 사용
# ## s에 문자열을 할당하고, 'walrus' in s를 result에 할당하고, result가 True 라면
# if result := 'walrus' in (s := 'walrus eat kimchi'):
#     print(s)  ## s 출력
#     print(result)  ## result 출력

# x = 0
# while (x := x + 1) < 10:    # Prints 1, 2, 3, ..., 9
#     print(x)

li = []
for  i in range(5):
    li.append(i)

print(li)

li = [i for i in range(5)]