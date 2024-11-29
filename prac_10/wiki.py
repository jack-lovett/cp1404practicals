"""
CP1404 Practical 10
Wiki API
"""
import wikipedia
from wikipedia import PageError, DisambiguationError


def main():
    """Python Wiki main function."""
    print("Welcome to Python Wiki")
    search_phrase = input("Search phrase: ")
    while search_phrase != "":
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print("\nResults:")
            print("Title:", page.title)
            print("URL:", page.url)
            print("Summary:", page.summary)
        except PageError:
            print(f"Search phrase \"{search_phrase}\" does not match any pages.")
        except DisambiguationError as error:
            print(f"Search phrase \"{search_phrase}\" is too ambiguous. Try one of the options below.")
            print(error.options)
        search_phrase = input("Search phrase: ")
    print("Thank you.")


if __name__ == '__main__':
    main()
