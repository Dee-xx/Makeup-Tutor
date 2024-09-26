def makeup_quiz():
    name= input('What is your name? ')
    print("Welcome"+ name+ " !")
    print(" Today we are going recommend makeup products for you based on your answers")
    score = 0
    print("Answer the following questions with yes or no.")
    q1 = input("Is your face round").lower()
    if q1 == "yes":
        score += 1
    q2 = input("Do you have dark cicles or eye bags").lower()
    if q2 == "yes":
        score += 1
    q3= input("Are you darkskinned")
    if q3=="yes":
        score+= 1
    q2 = input("Do you like blush?").lower()
    if q2 == "yes":
        score += 1

    if score == 4:
        return "Use an orange color corrector before applying your foundation. You should use a foundation that is your exact shade. Place your contour directly above your cheekbones and blend it. Then add your blush directly above your contour."
    elif score == 3:
        return "Use an orange color corrector before applying your foundation. You should use a foundation that is your exact shade. Place your contour directly above your cheekbones and blend it."
    elif score== 2:
        return "You should use your foundation that is your exact shade"
    else:
        return"Sorry, We are unable to give you any makeup recommendations at the moment"

print(makeup_quiz())