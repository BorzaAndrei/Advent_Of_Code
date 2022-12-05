def build_set(a_answers):
    answers_set = set()
    for answer in a_answers:
        for letter in answer:
            answers_set.add(letter)
    return answers_set


def count_all_yes(a_answers):
    answers_dict = {}
    for answer in a_answers:
        for letter in answer:
            if letter not in answers_dict:
                answers_dict[letter] = 1
            else:
                answers_dict[letter] += 1
    count = 0
    for letter in answers_dict:
        if answers_dict[letter] == len(a_answers):
            count += 1
    return count


with open("input/6.txt") as r:
    answers = []
    final_sum = 0
    for line in r.readlines():
        if line == '\n':
            # final_sum += len(build_set(answers))
            final_sum += count_all_yes(answers)
            answers = []
        else:
            answers.append(line.strip())
    print(final_sum)
