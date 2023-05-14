import sys

raiting_id = int(sys.argv[1])
imdb = {
    111161: [{"rating": 8}, {"rating": 9}, {"rating": 10}, {"rating": 9}, {"rating": 10}],
    68646: [{"rating": 8}, {"rating": 10}, {"rating": 9}, {"rating": 9}, {"rating": 9}],
    468569: [{"rating": 10}, {"rating": 10}, {"rating": 8}, {"rating": 8}],
    71562: [{"rating": 9}, {"rating": 9}, {"rating": 10}],
    167260: [{"rating": 8}, {"rating": 7}, {"rating": 9}, {"rating": 9}, {"rating": 8}, {"rating": 9}]
}

last_raiting = imdb[raiting_id][-1]["rating"]
print(last_raiting)
