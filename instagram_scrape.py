from instascrape import Hashtag, Profile, Post

# Set your session ID here
SESSIONID = (
    "5636912793%3ANCwlpbl54Iae2S%3A13%3AAYf_c9ToT1KatZakT-nzONJS5FaHv5vQp-UCccfXAw"
)

# Instantiate the scraper objects
user_post = Post("https://www.instagram.com/p/C9xMiNGxHOM/")

# Set the headers with the session ID
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "cookie": f"sessionid={SESSIONID};",
}

# Scrape their respective data
user_post.scrape(headers=headers)

# Print the data
print(user_post)
user_post.to_csv("data/data.csv")
