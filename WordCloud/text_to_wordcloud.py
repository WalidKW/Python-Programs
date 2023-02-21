from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the content of the text file into a string variable
text = open('Data_Mining.txt', encoding="utf8").read()
# Note: To resolve the ('charmap' codec can't decode) error, use encoding="utf8" when reading the code.

# Create a WordCloud object with the desired parameters
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white")
# Generate the word cloud based on the text content
wordcloud.generate(text)

# Display the word cloud image using Matplotlib
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
