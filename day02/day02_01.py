def password_is_valid(policy, password):
    occurences, character = policy.split()
    minOccur, maxOccur = occurences.split("-")
    if character not in password:
        return False
    else:
        minOccur, maxOccur = [int(occur) for occur in occurences.split("-")]
        number_occurences = password.count(character)
        if number_occurences >= minOccur and number_occurences <= maxOccur:
            return True
        else:
            return False


def count_valid_passwords(file):
    count = 0
    with open(file) as f:
        for line in f:
            policy, password = line.split(":")
            if password_is_valid(policy, password):
                count += 1
    return count


if __name__ == "__main__":
    print(count_valid_passwords("input.txt"))
