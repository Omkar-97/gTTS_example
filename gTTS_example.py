"""
Sample representation of google text to speech (gTTS) library
"""

def get_candy():
    import os
    from gtts import gTTS
    import sys

    with open("chat.txt", "w+") as f:
        sys.stdout = f
        print("me: I want candies")
        print("shopkeeper: How many candies do you want?")
        n = int(input())
        w_cnt = n
        temp = 0
        while w_cnt > 0:
            if w_cnt % 3 == 0:
                temp += 1
            w_cnt -= 1
        print("me: I want {} candies".format(n))
        print("shopkeeper: Sure, it will cost you around {}$".format(n))
        print("me: Ok, that's fine\nany offers going on?")
        if n >= 3:
            print("shopkeeper: If you return me back {} wrappers, I will give you {} candies free".format(temp*3, temp))
            print("me: Awesome, then I will get total of {} candies".format(n+temp))
            print("shopkeeper: Exactly")
        else:
            print("shopkeeper: Sorry, no offers you will get only {} candies".format(n))
    f.close()
    with open("chat.txt") as fp:
        text = fp.read()
        if text:
            myobj = gTTS(text=text, lang="en-us", slow=False)
            myobj.save("sample.mp3")
            myobj.save("sample.wav")
        fp.close()
    os.system("start sample.mp3")


if __name__ == '__main__':
    get_candy()
