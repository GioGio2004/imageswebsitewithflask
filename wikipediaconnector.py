import wikipedia

def search_wikipedia(query):
    try:
        # Search for the query on Wikipedia
        results = wikipedia.search(query)

        if not results:
            return None

        # Get the first result and fetch the page content
        page = wikipedia.page(results[0])
        title = page.title
        summary = page.summary

        return {
            'title': title,
            'summary': summary
        }

    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation pages
        suggestions = e.options[:5]  # Get the first 5 suggestions
        return {
            'error': 'Disambiguation',
            'suggestions': suggestions
        }

    except wikipedia.exceptions.PageError:
        return {
            'error': 'Page not found'
        }

info = "girogi is doing something" 