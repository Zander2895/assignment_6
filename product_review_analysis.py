#Frist exercise
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "poor", "average"]

def highlighted(reviews, keywords):
    highlighted = []
    for review in reviews:
        for keyword in keywords:
            if keyword in review:
                print(review.replace(keyword, keyword.upper()))
            elif keyword.capitalize() in review:
                print(review.replace(keyword.capitalize(), keyword.upper()))
highlighted(reviews, keywords)   

#Second exercise
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]

negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally(positive_words, negative_words, reviews):
    tally = []
    positive_counter = 0
    negative_counter = 0
    for review in reviews:
        review = review.lower()
        for positive_word in positive_words:
            if positive_word in review:
                print(positive_word)
                positive_counter += 1
        for negative_word in negative_words:
            if negative_word in review:
                print(negative_word)
                negative_counter += 1
    print(positive_counter, negative_counter)
tally(positive_words, negative_words, reviews)

