import re
import sys

# Finds desired strings and replaces them with the desired replacement.
# Place text that would be acted upon in toFindReplace.txt before doing anything, or else this will not work.
def main():
    toFR = open("toFindReplace.txt", "r")
    replaced = open("Replaced.txt", "w")

    s = list(toFR.read()) # store the entirety of the text in a string.
    print ("".join(s))

    print ("What phrase would you like to replace? (Hit Enter to Quit)")
    toFind = raw_input()
    while (toFind != ""):
        print ("What would you like to replace that phrase with?")
        toReplaceWith = raw_input()

        r = re.compile(toFind)

        replaced.close()
        for i in range(0, len(r.findall("".join(s)))):

            m = r.search("".join(s))
            if m:
                st = m.start()
                end = m.end()
                lentrp = len(toReplaceWith)

                dif = (st + lentrp) - end
                print (len(s))
                for i in range(len(s), end):
                    s[i+dif] = s[i]

                print (len(s))

                for i in range(0, lentrp):
                    s[st+i] = toReplaceWith[i] 

                replaced = open("Replaced.txt", "w")
                replaced.write("".join(s))
                replaced.close()

        print ("What phrase would you like to replace? (Hit enter to quit)")
        toFind = raw_input()

def replace(s, r, f, trp):
    m = r.search(s)
    if m:
        st = m.start

        s = s[:m.start()] + s[m.end():]
        f.write(s)

if __name__ == "__main__":
    main()