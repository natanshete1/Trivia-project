import Answer
import Question

ans = Answer.l_Ans

qus = Question.l_Qus
n = len(qus)
score = 0
for i in range(n):
    print(qus[i])
    print(f"a = {ans[i][0]}\nb = {ans[i][1]}\nc = {ans[i][2]}\nd = {ans[i][3]}")
    guess = input("Enter answer")
    if guess not in ["Japan", "Noah", "Isaac Newton", "light bulb", "Aphrodite", "Los Angeles", "Jerusalem", "vintage",
                     "Persian", "Bourbon"]:
        print("worng")
    else:
        score += 9
print("score = ", score)
