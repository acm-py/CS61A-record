def search(query, ranking= lambda: r: -r.stars):
    result = [r for r in Restaurants.all if query in r.name]
    return sort(result, ranking)

class Restaurants:
    all = []
    def __init__(self, name, stars,reviews):
        self.name, self.stars = name, stars
        self.reviews = reviews
        Restaurants.all.append(self)

    def similar(self, k, similarity):
        """Return the k most similar Restaurants to SELF, using SIMILARITY for comparison
        """
        others = list(Restaurants.all)
        others.remove(self)
        # 我写的错误版本
        #return sorted(others,key = lambda similarity: similarity)
        different = lambda r: -similarity(self, r)
        return sorted(others,key = different)[:k]
    def __repr__(self):
        return '<' + self.name + '>'


result = search('Thai')
for r in result:
    print(r, 'is similar to', rr.similar(3))