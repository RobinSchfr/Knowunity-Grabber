import requests


def main():
    while True:
        url = input('Enter your knowunity link here: ')
        if isInvalidURL(url):
            print('Invalid URL!')
        else:
            break
    response = requests.get(url)
    content = response.text
    title = getString('"title":', content)
    url = getString('"contentUrl":', content)
    pages = getString('"pageCount":', content)
    print('\n', '#' * 100, f'\nTitle: {title}\nURL  : {url}\nPages: {pages}\n', '#' * 100, '\n', sep='')
    repeat = input('New request? (Y/N) ')
    if repeat.lower() == 'y':
        main()
    else:
        print('Program closed...')


def isInvalidURL(url):
    if not url.startswith('https://knowunity.de/knows/'):
        return True
    response = requests.get(url)
    content = response.text
    if content.count('Seite nicht gefunden') > 3:
        return True
    else:
        return False


def getString(searchString, stringToSearch):
    stringLen = len(searchString)
    if searchString == '"pageCount":':
        firstPos = stringToSearch.find(searchString) + stringLen
        secondPos = stringToSearch.find(',', firstPos)
    else:
        firstPos = stringToSearch.find(searchString) + stringLen + 1
        secondPos = stringToSearch.find('"', firstPos)
    return stringToSearch[firstPos:secondPos]


if __name__ == '__main__':
    main()