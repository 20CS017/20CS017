# Find runner-up from given list
# 20CS017
# RIKEN GOYANI

n = int(input())
score = map(int, input().split())
print(sorted(list(set(score)))[-2])
