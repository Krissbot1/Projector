# **You have 100 cats.**
#
# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on.
# You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1).
# Every time you stop at a cat, you either put a hat on it if it doesn’t have one on,
# or you take its hat off if it has one on.
# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# 3. The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# 4. You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.
#
# Optional: Make function that can calculate hat with any amount of rounds and cats.
#
# Here you should write an algorithm, after that, try to make pseudo code.
# Only after that start to work. Code is simple here, but you might struggle with algorithm.
# Therefore, don`t try to write a code from the first attempt.


def hats_in_cats(cats: int, rounds: int):
    '''Takes number of cats without hats and number of rounds in which it
      will put hats on those cats following certain rules:
      1. The first round, it stops at every cat, placing a hat on each one.
      2. The second round, it only stops at every second cat (#2, #4, #6, #8, etc.).
      3. The third round, it only stops at every third cat(#3, #6, #9, #12, etc.).
      4. It continues this process until it's made 100 rounds around the cats
      (e.g., it only visits the 100th cat). Outputs  cats in hats with print()
      Calculates the total number of iterations as bonus.
      '''

    cats_and_hats = [False, ] * cats
    iterations = 0
    for round_ in range(rounds):
        for each_cat in range(round_, len(cats_and_hats), round_ + 1):
            if cats_and_hats[each_cat]:
                cats_and_hats[each_cat] = False
            else:
                cats_and_hats[each_cat] = True
            iterations += 1

    count_cats = 0
    for cat in range(len(cats_and_hats)):
        if cats_and_hats[cat]:
            print(f'The cat #{cat + 1} is in the hat')
            count_cats += 1
    print(f'Total number of cats in hats: {count_cats}')
    print(f'Number of iterations: {iterations}')
    print(f'Maximum of possible iterations: {cats * rounds}')


hats_in_cats(100, 100)
