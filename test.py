# 이제 1부터 50까지의 수를 너가 골라서 내가 맞히는 게임을 만들거야.

import random

# 일단 너가 먼저 1부터 50까지의 수를 랜덤하게 하나 골라줘.
random_number = random.randint(1,50)
print(random_number)

# 내가 1부터 50까지의 수 중 하나를 골른다고 가정했을 때 너가 고른 수 보다 큰지 작은지 말해줘.

# 만약 내가 답을 틀렸을때 다시 기회를 줘. 기회는 틀린 것 까지 합해서 총 5번 이야.

# 만약 50보다 더 큰 수,작은 수를 적으면 기회는 사라지지 않지만 너가 경고를 줘, 이 기회는 세번이고, 세번이 넘어가면 게임을 끝내줘

# 맞을 경우,맞았다고 말해주고 게임을 끝내고 게임을 다시 시작 할 수 있게 해줘.