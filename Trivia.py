a_options = ["China",
             "Japan",
             "Italy",
             "Korea"
             ]

b_options = ["Moses",
             "Noah",
             "Japheth",
             "Jacob"
             ]


c_options = ["Albert Einstein",
             "Isaac Newton",
             "Stephen Hawking",
             "Glilau Galilei"
             ]

d_options = ["Stove",
             "light bulb",
             "car",
             "calculator"
             ]

e_options = ["Aphrodite",
             "Deimos",
             "Pantheon",
             "Phobos"
             ]


f_options = ["California",""
            "Los Angeles",
            "New York",
            "Las Vegas"]

g_options =["Jerusalem",
           "Tel Aviv",
           "Hadera",
           "Herzliya"]

h_options = ["vintage",
            "olive harvest",
            "date harvest",
            "picking"]

i_options = ["Persian",
            "Banana",
            "Parsley",
            "Plum"]

j_bonos_options = ["Jordan Katzrin",
           "Chardonnay",
           "Cabernet Franc",
           "Bourbon"]


a = "Which country do you drink sake in?"
#
b = "In the Bible who built the ark"
#
c = "Who discovered gravity?"
#
d = "What Did Thomas Edison Invent?"
#
e = "The goddess of love in Greek mythology is called...?"
#
f="Question=Where in the US is Hollywood?"
#
g="Question=Where is the Knesset of Israel?"
#
h= "What is called grape picking?"
#
i="Which of the following is not a fruit?"
#
Bonos = "Which of the following is not a type of wine?"




l_Ans = [a_options,b_options,c_options,d_options,e_options,f_options,g_options,h_options,i_options,j_bonos_options]

l_Qus = [a,b,c,d,e,f,g,h,i,Bonos]
n = len(l_Qus)
score = 0
for i in range(3):
    print(l_Qus[i])
    print(f"a = {l_Ans[i][i]}\nb = {l_Ans[i][i+1]}\nc = {l_Ans[i][i+2]}\nd = {l_Ans[i][i+3]}")
    guess = input("Enter answer")
    if guess not in ["Japan","Noah","Isaac Newton","light bulb","Aphrodite",  "Los Angeles","Jerusalem","vintage","Persian","Bourbon"]:
        print("worng")
    else:
        score +=9
print(score)