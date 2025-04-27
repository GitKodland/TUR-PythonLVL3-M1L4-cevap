import aiohttp
import random

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.img = None
        self.name = None

    async def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['forms'][0]['name']
                else:
                    return "Pikachu"

    async def info(self):
        if not self.name:
            self.name = await self.get_name()
        return f"Pokémonunuzun ismi: {self.name}"

    async def show_img(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:  #  HTTP oturumu açmak
            async with session.get(url) as response:  # Pokémon verilerini almak için bir GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması
                    img_url = data['sprites']['front_default']  #  Pokémonun URL'sini alma
                    return img_url  # Resmin URL'sini döndürme
                else:
                    return None  # İstek başarısız olursa None döndürür
