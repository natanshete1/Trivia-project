import Answer
import Question

ans = Answer.l_Ans
ans_dic = Answer.real_ans
ans2 = ans_dic.values()
ans2_list = list(ans2)

qus = Question.l_Qus
n = len(qus)
score = 0
print(ans2_list)
for i in range(n):
    print(qus[i]) # present qustion
    print(f"a = {ans[i][0]}\nb = {ans[i][1]}\nc = {ans[i][2]}\nd = {ans[i][3]}") # show options
    guess = input("Enter answer :") # get player input
    while guess not in ("a", "b", "c", "d"): # check valid input
        print("Try Again(a,b,c,d)")
        print(qus[i])
        print(f"a = {ans[i][0]}\nb = {ans[i][1]}\nc = {ans[i][2]}\nd = {ans[i][3]}")
        guess = input("Enter answer :")
    if guess == ans2_list[i] : # Compar if answer is correct
        score += 9
        print("Right answer\n*************************")
    else:
        print("\nWrong answer\n*************************")
    if i in (2,5):
        print("Round score = ", score)
        print("**********************************\n")
        print("***************Next Round********************")
    if i == 9 and guess == ans2_list[i] :
        score +=9

print("Final score = ", score)
