import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
    else:
        return None

def main():
    st.title("Wikipedia Web Scraper")
    st.markdown("---")

    url = st.text_input("Enter Wikipedia URL:", "https://en.wikipedia.org/wiki/Main_Page")
    if st.button("Scrape"):
        st.write(f"Scraping data from: {url}")
        soup = scrape_wikipedia(url)
        if soup:
            st.write(soup.prettify())
        else:
            st.error("Failed to fetch data. Please enter a valid URL.")

if __name__ == "__main__":
    main()
