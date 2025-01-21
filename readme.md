# Ty Zicos scrapper

Extract data from a given 'ville'

## Pourquoi

I wanted data to be available on more platforms

Je veux arrêter que Facebook ne serve qu'aux évènements, on peut faire mieux, on a déjà le Ty Zicos, qu'il soit mis en avant

### Comment

* avoir python (au moins 3 je crois, j'ai pas testé en dessous)
* installer au minimum flask et bs4 (beautifulsoup, un meilleur scrapper html)

lancer l'api
```
python app.py
```
puis faire une requête sur 127.0.0.1:5000 (par défault) qui retournera en json les concerts à venir pour une ville donnée en endpoint, comme par exemple Brest:
```
htttp://127.0.0.1:5000/brest
```
vous aurez les dates au format json, libres à vous de les exploirer

##### TODO

* convertir les dates en ISO
* gérer le géocage des lieux ?
* suggestions ?

## License

Démerdez-vous, bisous