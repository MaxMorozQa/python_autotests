import requests

token = '26be1bafbbd45619ef039b9bd6ad389f'

add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-type' : 'application/json',
                                                                               'trainer_token' : token},
                                                                               json = { "name" : "Гринч",
                                                                                       "photo": "https://dolnikov.ru/pokemons/albums/003.png"})
print(add_pokemon_response.text)

response = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-type' : 'application/json', 
                                                                                            'trainer_token' : token},
                                                                                            json = {"pokemon_id": "9868",
                                                                                                    "name": "Курганец",
                                                                                                    "photo": "https://dolnikov.ru/pokemons/albums/008.png"})
print(response.text)  

pokeboll_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers = {'Content-type' : 'application/json',
                                                                                                    'trainer_token' : token},
                                                                                                    json = { 
                                                                                                             "pokemon_id": "9868"
                                                                                                           })
