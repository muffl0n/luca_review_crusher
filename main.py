from google_play_scraper import reviews

stopwords = ['esse', 'essen', 'lecker', 'food', 'kaffee', 'schenke', 'burger', 'pommes', 'wasser', 'werkstatt',
             'spätzle', 'abend', 'lokal', 'eis', 'waffeln', 'restaurant', 'geschmack', 'personal', 'service', 'höflich',
             'café', 'pizza', 'bier', 'schnitzel', 'ambiente', 'bäckerei', 'barkeeper', 'cocktails', 'tierpark']


def misleading_reviews(review):
    return any(stopword in review['content'].lower() for stopword in stopwords)


result, continuation_token = reviews(
    'de.culture4life.luca',
    lang='de',
    country='de',
    count=10000,
    filter_score_with=1
)

misleading_reviews = list(filter(misleading_reviews, result))

print(f'{len(misleading_reviews)}/{len(result)} misleading ({len(misleading_reviews) / len(result) * 100}%)')
