import os
import sys
import urllib.request


def main():
    if len(sys.argv) < 2:
        print("Missing challenge number\nUsage: %s challenge_number" % sys.argv[0])
        raise SystemExit

    challenge_number = str(sys.argv[1])
    path = os.getcwd() + "\\" + challenge_number + "\\"
    input_name = "input"

    # create challenge dir
    if not os.path.exists(challenge_number):
        os.makedirs(challenge_number)

    # get challenge input
    req = urllib.request.Request(
        "https://adventofcode.com/2018/day/%s/input" % challenge_number,
        headers={"Cookie": "session=X"}
    )

    input_text = urllib.request.urlopen(req, timeout=15).read().decode("utf-8")
    if not os.path.exists(path + input_name):
        with open(os.getcwd() + "\\" + challenge_number + "\\input", "w") as f:
            f.write(input_text)
            f.close()

    # create 1.py file
    if not os.path.exists(path + "1.py"):
        with open(path + "1.py", "w") as f:
            f.write("with open(\"input\") as f:\n\tfor line in f.readlines():\n\t\tpass")
            f.close()


if __name__ == '__main__':
    main()
