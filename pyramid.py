
def pyramid(n):
    for w in range(n):
        no_of_stars = 2 * (w + 1) - 1
        spaces = " " * (n - w - 1)
        stars = "*" * no_of_stars
        print(spaces + stars)

if __name__ == '__main__':
    pyramid(40)
