#!/Users/amod/venv/bin/python

'''f = open("/Users/Amod/image.jpg","rb")
print(f.read())
f.close()'''
'''f1 = open("/Users/Amod/image.jpg", "a")
for line in f.readlines():
    f1.writelines(line.split(":")[0])
# print(f.read())

f.close()
'''
x =[]
y = []
try:
    with open("/Users/Amod/Documents/FL_insurance_sample.csv") as f:
        #print(f.read())
        #print(len(f.read()))
        for i in f.readlines():
            x.append((i.split(sep=',')[2]))

        print(set(x))

        '''
        for k in x:
            if k not in y:
                y.append(k)
                # print(k)
        '''

        # print(len(y))
    f.close()
except IOError:
    print("There")
except Exception as e:
    print(e)
