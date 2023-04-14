print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don'tCchange the code above 👆

#Write your code below this line 👇
name1_lowercase=name1.lower()
name2_lowercase=name2.lower()
combined_name=name1_lowercase+name2_lowercase
 
t=(combined_name.count("t"))
r=(combined_name.count("r"))
u=(combined_name.count("u"))
e=(combined_name.count("e"))


l=(combined_name.count("l"))
o=(combined_name.count("o"))
v=(combined_name.count("v"))
e=(combined_name.count("e"))


first_digit=t+ r + u + e
second_digit=l + o + v + e
score_final=(str(first_digit) + str(second_digit))

if (int(score_final) <10) or (int(score_final)>90):
    print(f"Your score is {score_final}, you go together like coke and mentos.")
elif (int(score_final) >=40) and (int(score_final) <=50):
    print(f"Your score is {score_final}, you are alright together.")
else:
    print(f"Your score is {score_final}.")