import random


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def monti_hall_test():
    with_change = 0
    without_change = 0
    for i in range(1, 1001):
        variants = [1, 2, 3]
        correct_answer = random.randrange(1, 4)
        choose_variant = random.randrange(1, 4)
        delete_variant = random.randrange(1, 4)
        while delete_variant == correct_answer or delete_variant == choose_variant:
            delete_variant = random.randrange(1, 4)
        variants.remove(delete_variant)
        variants.remove(choose_variant)
        new_choose_variant = variants[0]
        if new_choose_variant == correct_answer:
            with_change += 1
        if choose_variant == correct_answer:
            without_change += 1
    print("Шанс победить, если изменить выбор: " + toFixed(with_change / 1000 * 100, 1), "Шанс победить, если не поменять выбор: " + toFixed(without_change / 1000 * 100, 1))


monti_hall_test()
