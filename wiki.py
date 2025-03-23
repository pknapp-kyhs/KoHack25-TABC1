import requests
import webbrowser


def search_wikipedia(search_term):
    url = "https://en.wikipedia.org/w/api.php"

    # Set up parameters for the API request
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': search_term,
        'format': 'json'
    }

    # Make the request to the Wikipedia API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        search_results = data['query']['search']

        # Check if there are any results
        if len(search_results) > 0:
            print("Search results for '" + search_term + "':\n")
            for i in range(len(search_results)):
                title = search_results[i]['title']
                preview = search_results[i]['snippet']
                print(str(i + 1) + ". Title: " + title)
                print("   Preview: " + preview + "\n")

            # Ask the user to select an article
            article_number = input("Enter the number of the article you want to open: ")

            # Convert the input to an integer
            article_number = int(article_number) - 1

            # Check if the number is valid
            if article_number >= 0 and article_number < len(search_results):
                article_title = search_results[article_number]['title']
                article_url = "https://en.wikipedia.org/wiki/" + article_title.replace(" ", "_")
                webbrowser.open(article_url)
                print("Opening article: " + article_url)
            else:
                print("Invalid selection. Please try again.")
        else:
            print("No results found for '" + search_term + "'.")
    else:
        print("Failed to search. Status code: " + str(response.status_code))


def get_user_search_query():
    search_query = input("What would you like to search on Wikipedia? ")
    return search_query


# Main program
if __name__ == "__main__":
    user_query = get_user_search_query()
    search_wikipedia(user_query)