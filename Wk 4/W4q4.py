list1=["Saif","Ali","MCA",3]
list2=[1,25.9,"Computer","Science"]

for i,j in zip(list1,reversed(list2)):
    print(f"List1 item: {i}, List2 item : {j}")