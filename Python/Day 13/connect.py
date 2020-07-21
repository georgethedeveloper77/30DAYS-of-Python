import requests
import pprint  # formatted
import pandas as pd #take list of objects n store incsv file

api_key = "eeebb04f5556add29722323025b77247"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZWViYjA0ZjU1NTZhZGQyOTcyMjMyMzAyNWI3NzI0NyIsInN1YiI6IjVmMTU4Y2IyZWNiZGU5MDAzNjc2YzAzZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.10aH6lB4RyrZ1GYWTM3pR-spjBKULbYMNVi77vd8Q0Y"

# HTTP requests  Methods
"""
GET  => grab data
POST => add/update data

PATCH
PUT
DELETE
"""

# whats our endpont (or a url)

# whats is the HTTP method that we need?


"""
Endpoint
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=eeebb04f5556add29722323025b77247
"""

movie_id = 500
api_version = 3
api_base_url = "https://api.themoviedb.org/3"
endpoint_path = f"/movie/{movie_id}"
# query strings...arguments   url parameters
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(endpoint)
# r = requests.get(endpoint) #json= {"api_key" : api_key})
# print(r.status_code)
# print(r.text)

# using v4
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}"
headers = {
    'Authorization': f'Bearer {api_key_v4}',   # various api
    'Content-Type': 'application/json;charset=utf-8'
}
# r = requests.get(endpoint, headers=headers) #json= {"api_key" : api_key})
# print(r.status_code)
# print(r.text)

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
searh_query = "Spiderman"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        # print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            # print(result['title'], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))
output = 'movies.csv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)


df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)