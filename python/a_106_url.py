from urllib import request

def main():

    a = request.urlopen("https://gooogle.com")
    print(a.read())
# web scrapping 할 수 있다. 번거롭다.
# 웬만하면 bs4 beautiful soup4를 사용하자




if __name__ == "__main__":
        main()
