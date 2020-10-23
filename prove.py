from data import tours

id_tour = int(input())
tour = tours[id_tour]
for k in tour:
    if k == 'title':
        title = tour[k]
        print(str(title) + " ")
    if k == 'price':
        price = tour[k]
        print(str(price) + " ")
    if k == 'stars':
        stars = tour[k]
        print(str(stars) + " ")
    if k == 'country':
        country = tour[k]
        print(str(country))

# d_list = []
# for s in tours:
#     d_list.append(tours[s])
# print(d_list)


# tours_list = []
# for t in tours:
#     tours_list.append(tours[t])
# # for s in tours_list:
# #     if s == 3:
# #         print(tours_list[0])
# print(tours_list[0])
