
secret_word = "giraffe"
guess = ""
count = 0
limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if count < limit:
        guess = input("enter guess: ")
        count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("you Lost")
print("you got it!")