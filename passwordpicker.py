import random
import string

lis=list(string.ascii_letters)
punc=list(string.punctuation)

pas=random.choice(lis)+random.choice(string.ascii_uppercase)+random.choice(lis)+random.choice(punc)+str(random.randint(1000,10000))


ps=list(pas)
random.shuffle(ps)

password=""

for x in ps:
  password=password + x
print(password)
