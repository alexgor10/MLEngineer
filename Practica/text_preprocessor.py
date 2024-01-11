import re 
import string
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")

class TextPreprocessor:

    def __init__(self, remove_links=True, remove_hastags=True,
                  remove_characters=True,convert_to_lowercase=True, 
                  remove_emojis=True, remove_numbers=True,remove_stopwords_flag= True,
                  transform_stemmer=True, transform_lemmatizer=True
                  ):
        
        self.remove_links_flag = remove_links
        self.remove_hastags_flag = remove_hastags
        self.remove_characters_flag = remove_characters
        self.convert_to_lowercase_flag = convert_to_lowercase
        self.remove_emojis_flag = remove_emojis
        self.remove_numbers_flag = remove_numbers
        self.remove_stopwords_flag= remove_stopwords_flag
        self.transform_stemmer_flag = transform_stemmer
        self.transform_lemmatizer_flag = transform_lemmatizer

    def remove_characters(self, text):
        if isinstance(text, str):
            return re.sub(r'[^\w\s]', '', text)
        else:
            return text

    def remove_stopwords(self, text):
        if isinstance(text, list):
            stop_words = set(stopwords.words('english'))
            return ' '.join([word for word in text if word.lower() not in stop_words])

    def convert_to_lowercase(self, text):
        if isinstance(text, str):
            return text.lower()

    def remove_emojis(self, text):
        if isinstance(text, str):
            emoji_pattern = re.compile("["
                                       u"\U0001F600-\U0001F64F"  
                                       u"\U0001F300-\U0001F5FF"  
                                       u"\U0001F680-\U0001F6FF"  
                                       u"\U0001F1E0-\U0001F1FF"  
                                       "]+", flags=re.UNICODE)
            return emoji_pattern.sub(r'', text)

    def remove_extra_spaces(self, text):
        if isinstance(text, str):
            return re.sub(r'\s+', ' ', text).strip()

    def remove_numbers(self, text):
        if isinstance(text, str):
            return re.sub(r'\d+', '', text)

    def remove_users(self, text):
        if isinstance(text, str):
            return re.sub(r'@\S+', '', text)

    def remove_hastags(self, text):
        if isinstance(text, str):
            return re.sub(r'#\S+', '', text)

    def remove_links(self, text):
        if isinstance(text, str):
            return re.sub(r'http\S+', '', text)

    def tokenize_text(self, text):
        return word_tokenize(text)
    
    def transform_stemmer(self, text):
        if isinstance(text, str):
            # Initialize Python porter stemmer
            ps = PorterStemmer()

            # Remove punctuation
            example_sentence_no_punct = text.translate(str.maketrans("", "", string.punctuation))
            
            # Create tokens
            word_tokens = word_tokenize(example_sentence_no_punct)

            # Perform stemming
            return ' '.join([ps.stem(word) for word in word_tokens])
        else:
            return text


    def transform_lemmatizer(self, text):
        if isinstance(text, str):
            # Initialize wordnet lemmatizer
            wnl = WordNetLemmatizer()

            # Remove punctuation
            example_sentence_no_punct = text.translate(str.maketrans("", "", string.punctuation))
            
            word_tokens = word_tokenize(example_sentence_no_punct)

            # Perform lemmatization
            return ' '.join([wnl.lemmatize(word) for word in word_tokens ])
        else:
            return text

    def preprocess_text(self, text):
        if self.remove_links_flag:
            text = self.remove_links(text)
        if self.remove_hastags_flag:
            text = self.remove_hastags(text)
        if self.remove_characters_flag:
            text = self.remove_characters(text)
        if self.remove_stopwords_flag:
            text = self.remove_stopwords(text.split())
        if self.convert_to_lowercase_flag:
            text = self.convert_to_lowercase(text)
        if self.remove_emojis_flag:
            text = self.remove_emojis(text)
        if self.remove_numbers_flag:
            text = self.remove_numbers(text)
        if self.transform_stemmer_flag:
            text = self.transform_stemmer(text)
        if self.transform_lemmatizer_flag:
            text = self.transform_lemmatizer(text)
        return text

    
