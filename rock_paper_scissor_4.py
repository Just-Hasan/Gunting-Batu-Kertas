# User and computer input their choice
# If the user's choice and the computer's choice are the same, then it's a tie
# rock, paper, scissor rule is r>s,s>p,p>r
import random
print("Rock Paper Scissor Boom!")


def contestant():
    user = input(
        "'Press'\n'R' For Rock\n'P' For Paper\n'S' For Scissor\nSo...What's it gonna be : ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return(
            f"It's a tie both you and the computer choses {user} and {computer}")

    if is_win(user, computer):
        return (f"You won cuz you chose {user} and the computer choses {computer}")

    return f'bruh...you lost to machine, the machine chose {computer} and you chose {user}'


def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True


print(contestant())
