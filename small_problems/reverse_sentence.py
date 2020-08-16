sent = "This is a sentence"
# expected  ecnetnes a si sihT
def rev(w):
    return w[::-1]

rev_sent = ""
for word in sent.split(" "):
    r = rev(word)
    # rev_sent = rev_sent + r + " "
    rev_sent = r + " " +rev_sent

print (rev_sent.strip())

