def searcher():
    import time
    book = 'This is some text from some book'
    # here instead of time.sleep we are reading text from book which is taking time
    # i.e. time-consuming task
    time.sleep(4)

    while True:
        text = yield
        if text in book:
            print('Text is in book')
        else:
            print('Text is not in book')


search = searcher()
print('search started')
next(search)
print('Next method run')
search.send('This')
input('Press any key to continue')
search.send('Thes')
input('Press any key to continue')

