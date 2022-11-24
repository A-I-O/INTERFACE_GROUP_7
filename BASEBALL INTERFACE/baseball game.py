if __name__ == '__main__':
    scores = [5, 6, 0, 2]
    score = input(
        "Enter the scores as:\n(Complete) for correct complete score\n(D) for hitting a homeran\n(catch) if the opponent catches the ball\n(miss)if the player misses all the 7 chances\n(miss) for when misses the seven chances\n")
    if (score == 'Complete'):
        scores.append(5)
        print(scores)
    if (score == "catch"):
        scores.append('C')
        scores.pop(-3 and -2)
        print(scores)
    if (score == "miss"):
        scores.append(2)
        print(scores)
    if (score == 'D'):
        scores.append('D')
        scores.append(scores[-4])
        scores.append(scores[-4])
        print(scores)

