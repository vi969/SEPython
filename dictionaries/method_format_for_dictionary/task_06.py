import sys

name_movie = sys.argv[1]
rating = float(sys.argv[2])
votes = int(sys.argv[3])

movie = {
    "name": name_movie,
    "rating": rating,
    "votes": votes
}

m_template = "{m[name]} ({m[rating]:.1f})"
m_template = m_template.format(m=movie)
print(m_template)