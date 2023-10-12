from instagrapi import Client

with open("credentials.txt", "r") as f:
    username, password = f.read().split()

# Logando no instagram
client = Client() # Instanciando o cliente API
client.login(username, password)

hashtag = "programming"

medias = client.hashtag_medias_recent(hashtag, 20)

for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"Liked post number {i+1} of hashtag {hashtag}")