from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

# Read the content of the text file into a string variable
text = open('Data_Mining.txt', encoding="utf8").read()
# Note: To resolve the ('charmap' codec can't decode) error, use encoding="utf8" when reading the code.

# Stopwords are words that are frequently excluded from text analysis because they have no significant meaning.
stop_words = set(stopwords.words('english'))
# removing all words in the original text variable that are in the stopwords list.
cleaned_text = [word for word in text.split() if word not in stop_words]

# Create a WordCloud object with the desired parameters
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white")
# Generate the word cloud based on the text content
wordcloud.generate(" ".join(cleaned_text))

# Display the word cloud image using Matplotlib
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
