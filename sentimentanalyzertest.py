import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import warnings
nltk.download('vader_lexicon')
print(nltk.__version__)

sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores("\nThis is a really horrible day! \n\n"))
print(sia.polarity_scores("\nThis is a really great day! \n\n"))
print(sia.polarity_scores("\nThis is a repetetive day! \n\n"))
warnings.filterwarnings("ignore", category=UserWarning)
