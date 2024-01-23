pip install seo-keyword-research-tool
import streamlit as st
from SeoKeywordResearch import SeoKeywordResearch

# Title for the app
st.title('SEO Keyword Research Tool')

# User inputs
query = st.text_input('Enter your query', 'horse racing results')
api_key = st.text_input('Enter your API key', 'd5f2ec8438d02a5985bc7156cbe93abe1452e33dcdffa3ef5a264bcee5440f86')
lang = st.text_input('Language', 'en')
country = st.text_input('Country', 'us')
domain = st.text_input('Domain', 'google.com')

# Button to perform search
if st.button('Search'):
    keyword_research = SeoKeywordResearch(
        query=query,
        api_key=api_key,
        lang=lang,
        country=country,
        domain=domain
    )
    auto_complete_results = keyword_research.get_auto_complete()
    related_searches_results = keyword_research.get_related_searches()
    related_questions_results = keyword_research.get_related_questions()

    data = {
        'auto_complete': auto_complete_results,
        'related_searches': related_searches_results,
        'related_questions': related_questions_results
    }

    # Displaying results
    st.write('Auto Complete Results:', auto_complete_results)
    st.write('Related Searches:', related_searches_results)
    st.write('Related Questions:', related_questions_results)

    # Save results to CSV
    if st.button('Save to CSV'):
        keyword_research.save_to_csv(data)
        st.success('Data saved to CSV')

    # Optional: Print data on the console
    # keyword_research.print_data(data)
