# 1
S, M, L = input("small treats: "), input("medium treats: "), input("large treats: ")
x = int(S) + int(M) * 2 + int(L) * 3
if x >= 10:
    print("happy")
else:
    print("sad")


# 2
P = int(input("limit: "))
N = int(input("the number of people who have the disease on Day 0: "))
R = int(input("people infected by one: "))
x = N  # total number of people got infected
n = 0  # number of people newly got infected each day
t = 0  # days past
while x <= P:
    t += 1
    n = N * (R ** t)
    x += n
print(t)


# 3
N = int(input("number of drops: "))
X, Y = [], []
for i in range(N):
    x, y = input("x, y: ").split(",")
    X.append(int(x))
    Y.append(int(y))
x_bl, y_bl = min(X) - 1, min(Y) - 1
x_tr, y_tr = max(X) + 1, max(Y) + 1
print((x_bl, y_bl), (x_tr, y_tr))


# 4
T = input("text: ")
S = input("string: ")
ans = "no"
for i in range(len(S)):
    if S in T:
        ans = "yes"
        break
    S = S[1:] + S[0]
print(ans)


# 5
M = int(input())
N = int(input())
room = []
ans = []


for i in range(M):
    j = input().split(" ")
    room.append(j)


end_key = [M, N]
end_val = room[-1][-1]
route = {tuple(end_key): end_val}


def f(p):
    next_step = []
    count = 0
    val = p[0] * p[1]
    for m in range(M):
        for n in range(N):
            if val == int(room[m][n]) and [m+1, n+1] != p:
                p = [m + 1, n + 1]
                if p == [1, 1]:  # done
                     ans.append(True)
                else:
                    if tuple(p) in route:  # infinite loop
                        route.update({tuple(p): 0})
                        ans.append(False)
                    else:
                        route[tuple(p)] = val  # found, continue
            else:
                count += 1
    if count == M * N:  # stuck
        ans.append(False)
    else:
        for key in list(route):
            if route[key] == val:
                next_step.append(key)
        for key in next_step:
            f(list(key))


f(end_key)
if any(ans):
    print("yes")
else:
    print("no")


'''
test
3
4
3 10 8 14
1 11 12 12
7 2 3 9
'''


