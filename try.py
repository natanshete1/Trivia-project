import Answer
import Question

ans = Answer.l_Ans

qus = Question.l_Qus
print("*****Trivia Game*****")
score = 0
print(qus[0])
print(f"a = {ans[0][0]}\nb = {ans[0][1]}\nc = {ans[0][2]}\nd = {ans[0][3]}")
guess = input("Enter answer :")
while guess not in ("a","b","c","d"):
    print("Try Again(a,b,c,d)")
    print(qus[0])
    print(f"a = {ans[0][0]}\nb = {ans[0][1]}\nc = {ans[0][2]}\nd = {ans[0][3]}")
    guess = input("Enter answer :")
if guess == "b":
    score +=9
    print("Right answer\n*************************")
else:
    print("Wrong answer\n*************************")

print(qus[1])
print(f"a = {ans[1][0]}\nb = {ans[1][1]}\nc = {ans[1][2]}\nd = {ans[1][3]}")
guess = input("Enter answer :")
while guess not in ("a","b","c","d"):
    print("Try Again(a,b,c,d)")
    print(qus[1])
    print(f"a = {ans[1][0]}\nb = {ans[1][1]}\nc = {ans[1][2]}\nd = {ans[1][3]}")
    guess = input("Enter answer :")
if guess == "b":
    score +=9
    print("Right answer\n*************************")
else:
    print("Wrong answer\n*************************")

print(qus[2])
print(f"a = {ans[2][0]}\nb = {ans[2][1]}\nc = {ans[2][2]}\nd = {ans[2][3]}")
guess = input("Enter answer :")
while guess not in ("a","b","c","d"):
    print("Try Again(a,b,c,d)")
    print(qus[2])
    print(f"a = {ans[2][0]}\nb = {ans[2][1]}\nc = {ans[2][2]}\nd = {ans[2][3]}")
    guess = input("Enter answer :")
if guess == "b":
    score +=9
    print("Right answer\n*************************")
else:
    print("Wrong answer\n*************************")

print("First Round score = ", score)
print("**********************************\n")
print("***************Second Round********************")

print(qus[3])
print(f"a = {ans[3][0]}\nb = {ans[3][1]}\nc = {ans[3][2]}\nd = {ans[3][3]}")
guess = input("Enter answer :")
while guess not in ("a","b","c","d"):
    print("Try Again(a,b,c,d)")
    print(qus[3])
    print(f"a = {ans[3][0]}\nb = {ans[3][1]}\nc = {ans[3][2]}\nd = {ans[3][3]}")
    guess = input("Enter answer :")
if guess == "b":
    score +=9
    print("Right answer\n*************************")
else:
    print("Wrong answer\n*************************")

print(qus[4])
print(f"a = {ans[4][0]}\nb = {ans[3][1]}\nc = {ans[4][2]}\nd = {ans[4][3]}")
guess = input("Enter answer :")
while guess not in ("a", "b", "c", "d"):
    print("Try Again(a,b,c,d)")
    print(qus[4])
    print(f"a = {ans[4][0]}\nb = {ans[4][1]}\nc = {ans[4][2]}\nd = {ans[4][3]}")
    guess = input("Enter answer :")
if guess == "a":
    score +=9
    print("Right answer\n*************************")
else:
    print("Wrong answer\n*************************")

print(qus[5])
print(f"a = {ans[5][0]}\nb = {ans[5][1]}\nc = {ans[5][2]}\nd = {ans[5][3]}")
guess = input("Enter answer :")
while guess not in ("a", "b", "c", "d"):
    print("Try Again(a,b,c,d)")
    print(qus[5])
    print(f"a = {ans[5][0]}\nb = {ans[5][1]}\nc = {ans[5][2]}\nd = {ans[5][3]}")
    guess = input("Enter answer :")
if guess == "b":
    score +=9
    print("Right answer\n*************************")
else:
    print("Wrong answer\n*************************")

print("Second Round score = ", score)
print("**********************************\n")
print("*******************Third Round*********************")

print(qus[6])
print(f"a = {ans[6][0]}\nb = {ans[6][1]}\nc = {ans[6][2]}\nd = {ans[6][3]}")
guess = input("Enter answer :")
while guess not in ("a", "b", "c", "d"):
    print("Try Again(a,b,c,d)")
    print(qus[6])
    print(f"a = {ans[6][0]}\nb = {ans[6][1]}\nc = {ans[6][2]}\nd = {ans[6][3]}")
    guess = input("Enter answer :")
if guess == "a":
    score +=9
    print("Right answer\n*************************")
else:
    print("Wrong answer\n*************************")

print(qus[7])
print(f"a = {ans[7][0]}\nb = {ans[7][1]}\nc = {ans[7][2]}\nd = {ans[7][3]}")
guess = input("Enter answer :")
while guess not in ("a", "b", "c", "d"):
    print("Try Again(a,b,c,d)")
    print(qus[7])
    print(f"a = {ans[7][0]}\nb = {ans[7][1]}\nc = {ans[7][2]}\nd = {ans[7][3]}")
    guess = input("Enter answer :")
if guess == "a":
    score +=9
    print("Right answer\n*************************")
else:
    print("Wrong answer\n*************************")

print(qus[8])
print(f"a = {ans[8][0]}\nb = {ans[8][1]}\nc = {ans[8][2]}\nd = {ans[8][3]}")
guess = input("Enter answer :")
while guess not in ("a", "b", "c", "d"):
    print("Try Again(a,b,c,d)")
    print(qus[8])
    print(f"a = {ans[8][0]}\nb = {ans[8][1]}\nc = {ans[8][2]}\nd = {ans[8][3]}")
    guess = input("Enter answer :")
if guess == "c":
    score +=9
    print("Right answer\n*************************")
else:
    print("Wrong answer\n*************************")

print("Third Round score = ", score)
print("**********************************\n")
print("****Bonus Question****")

print(qus[9])
print(f"a = {ans[9][0]}\nb = {ans[9][1]}\nc = {ans[9][2]}\nd = {ans[9][3]}")
guess = input("Enter answer :")
while guess not in ("a", "b", "c", "d"):
    print("Try Again(a,b,c,d)")
    print(qus[9])
    print(f"a = {ans[9][0]}\nb = {ans[9][1]}\nc = {ans[9][2]}\nd = {ans[9][3]}")
    guess = input("Enter answer :")
if guess == "d":
    score +=18

print(f"Total score ={score}/100")
print("*****************GAME OVER*************************")



