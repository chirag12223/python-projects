import random
import string
if __name__=="__main__":
    s1=string.ascii_letters
    s2=string.digits
    s3=string.punctuation
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    T="NO"
    while T=="NO":
        print("Enter the length of the password required:")
        pwlen=int(input())
        random.shuffle(s)
        k=""
        for j in range(0,pwlen):
            k+=str(s[j])
        print(k)
        print("Are you satisfied?")
        T=input()#enter"NO"->if not satisfied