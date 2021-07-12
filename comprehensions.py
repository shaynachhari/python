# list comprehension

lst = []
for i in range(21):
    if i%2 == 0:
        lst.append(i)

print(lst)

lst = [i for i in range(21) if i % 2 == 0]
print(lst)

# dictionary comprehension
dic = {i: f"item{i}" for i in range(20) if i%2 == 0}
print(dic)
dic = {0: 'item0', 2: 'item2', 4: 'item4', 6: 'item6', 8: 'item8', 10: 'item10', 12: 'item12', 14: 'item14', 16: 'item16', 18: 'item18'}
new_dic = {s: n for n, s in dic.items()}
print(new_dic)

# set comprehension
sett = {i for i in dic.values()}
print(sett)

# tuple comprehension not exists
# generator making
tup = (i for i in range(21) if i%2==1)
print(tup._next_())
print(tup._next_())
print(next(tup))# list comprehension

