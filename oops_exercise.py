class Library:
    def __init__(self, book_list, name):
        self.bookList = book_list
        self.name = name
        self.lend_dict = {}

    def displayBooks(self):
        print(f'We have following books in our library: {self.name}')
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book: user})
            print('Book database has been updated')
        else:
            print(f'Book is already being used by {self.lend_dict[book]}')

    def addBook(self, book):
        self.bookList.append(book)
        print('Book has been added to the book list')

    def returnBook(self, book):
        self.lend_dict.pop(book)
        print('Book has been removed from the book list')


if __name__ == '__main__':
    hiral = Library(['Python', 'Java', 'C++', 'Flutter', 'Kotlin', 'Android', 'HTML', 'Javascript', 'machine Learning'],
                    'Hiral Library')

    while True:
        print(f'Welcome to the {hiral.name}. Enter your choice to continue')
        print('1. Display Books')
        print('2. Lend a Book')
        print('3. Add a Book')
        print('4. Return a Book')

        user_choice = input()

        if user_choice not in ['1', '2', '3', '4']:
            print('Please enter valid option')
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            hiral.displayBooks()

        elif user_choice == 2:
            book2 = input('Enter the book name you want to lend: ')
            name2 = input('Enter your name: ')
            hiral.lendBook(name2, book2)

        elif user_choice == 3:
            book2 = input('Enter the book name you want to add: ')
            hiral.addBook(book2)

        elif user_choice == 4:
            book2 = input('Enter the book name you want to return: ')
            hiral.returnBook(book2)

        else:
            print('Invalid input')



        user_choice2 = ''
        print('Press q to quit or c to continue')
        while user_choice2 != 'q' and user_choice2 != 'c':
            user_choice2 = input()

            if user_choice2 == 'q':
                exit()
            elif user_choice2 == 'c':
                continue
            else:
                print('Invalid input')
