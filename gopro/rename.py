import os


def main():
    print("start!")

    SUPER_DIR = "E:\\M2\\result\\pool\\gopro\\pp\\"

    n = 5000

    for d in range(6, 11):
        for j in range(n,n+2):
            os.rename(SUPER_DIR + f"{d}\\pp_{j}.csv",
                      SUPER_DIR + f"{d}\\{j}.csv")

    print("fin.")


if __name__ == '__main__':
    main()
