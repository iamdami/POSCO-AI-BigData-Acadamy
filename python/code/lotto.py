import random

print("** 로또 번호 자동 기입을 시작합니다.**")
for i in range(6):
    lotto = random.sample(range(1, 45), 6)
    lotto_res = ' '.join(map(str, lotto))
    print(i+1,"번째 자동 기입 ==> {}".format(lotto_res))
