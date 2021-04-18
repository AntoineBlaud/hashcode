def main():
    letters = list(input())
    letters_set = sorted(list(set(letters)), key = letters.index)
    best = -1
    best_letter = letters[0]
    for letter in letters_set:
        indice = [i for i, x in enumerate(letters) if x == letter]
        if len(indice) < 2:
            continue
        current = max(tuple([indice[i + 1]-indice[i] for i in range(len(indice) - 1)])) - 1
        best_letter = letter if current > best else best_letter
        best = max(best, current)
    return best_letter, str(best)


if __name__ == '__main__':
    print(' '.join(main()))
