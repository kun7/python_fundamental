book_list = ['Malcolm Galdwell', 'Andy Newman', 'Angela Duckworth', 'Mihaly Csikszentmihalyi']
print('\nShow the book list')
print(book_list)

for i in book_list:
    print(i)

print('\nShow the List of content')
print(book_list[0])
print(book_list[3])

book_list.append('William Atkins')
for i in range(0,len(book_list)):
    print(i)

#book_list.clear()
#print(book_list)

#ambil elemen ketiga
book_list[1] = 'Ramadhan said al Buthy'
book_list.pop(2)
print(book_list)

#ambil elemen terakhir
#book_list.pop()
#print(book_list)

#del book_list[0:-2]
#for i in range(0, len(book_list)):
    #print(book_list[i])

