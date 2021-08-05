def main():
    def sum(x):
        if x <= 1:
            return x
        else:
            return x + sum(x-1)

    print(sum(10))

main()
