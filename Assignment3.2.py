'''
Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
'''

subs = ["Americans", "Indians"]
verb = ["Play", "watch"]
obj = ["Baseball", "cricket"]

for sub in subs:
    for v in verb:
        for o in obj:
            print("{} {} {}".format(sub, v, o))
