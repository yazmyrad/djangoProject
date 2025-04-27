import json
titles = ['food','travel','healthfitness','lifestyle', 
          'fashionbeauty','photography','personal', 'DIYcraft',
            'parenting', 'music', 'business', 'artdesign','bookwriting',
            'personalfinance',
            'interiordesign',
            'sports',
            'news',
            'movie',
            'religion',
            'political'
            ]
dictionary =  {
    "model": "study.categories",
    "pk": 0,
    "fields": {
    "name": ""
    }
}
outfile = open("category.json", "w") 
for index, title in enumerate(titles):
    dictionary['pk'] = index + 1
    dictionary['fields']['name'] = f"{title}"
    json.dump(dictionary, outfile)
outfile.close()