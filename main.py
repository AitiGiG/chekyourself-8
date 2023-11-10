"==check-1=="
# class Auto:
#     def ride(self):
#         print('Riding on a ground')
# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto,Boat):
#     pass
# obj = Amphibian()
# obj.ride()
# obj.swim() 
"===chek-2=="
# class ContactList(list):
#     def __init__(self, list_):
#         self.list_ = list_
#     def search_by_name(self , tit):
#         similar =[]
#         for i in self.list_:
#             if tit in i :
#                 similar.append(i)
#         return similar
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))