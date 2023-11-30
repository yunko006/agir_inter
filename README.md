
<h1 align="center">
  <br>
  <img src="https://agir-competences.herokuapp.com/static/img/logo.png" alt="Agir" width="200">
  <br>
  Profil des Intervenants
  <br>
</h1>

<h4 align="center">Outil pour rechercher et sélectionner des intervenants pour des missions à l’international.</h4>

##

## Features principales

* Connexion à une base de donnée NoSQL.
* Permet de faire une recherche en "champs libre" sur la base de donnée.
  - Montre les résultats en fonction du score de recherche.
* Permet de faire une recherche "avancée" en recherchant précisément les critères de recherche et les spécificité. 
  - Affiche les résultats en faisant une combinaison des éléments de recherches.
* Permet de voir la fiche des intervenants.
* Différentes permissions en fonction des utilisateurs :
	- Certains peuvent faire des recherches, modifier une fiche, et enregistrer de nouveaux intervenants.
	- D'autres peuvent uniquement voir leur fiche et la modifier.
* Permet de voir tous les intervenants en fonction de leurs départements. 



## Credits

Ce projet utilise les packages open source suivants :

- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [bootstrap-flask](https://bootstrap-flask.readthedocs.io/en/stable/)
- [Redis](https://redis.io/)
- [mongodb](https://www.mongodb.com/fr-fr)
- [flask-mongoengine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)
- [flask-login](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)
- [flask-bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/)


## todo
 
- [x] Créer index de recherche textuel 
- [x]  -> problème car atm on doit purge puis remettre toutes la db = suppression de l'index de recherche a chaque fois = il faudrait reussir a append a la db. 
      _Enfaite c'est bon ca append bien, enfaite il faudrait reussir a delete tous les champs qui ont ete push dans la db avec app script comme ca append et on clean au fur et a mesure._

- [x] Connecter la nouvelle db au site live sur heroku avant demain (15/04/23) NON SUR AUTRE
- [x] 1 à 105
- [x] 105 à 210
- [x] 210 à 314
- [x] 300 à 400
- [x] 400 à fin

- [x] script pour faire automatiquement et pas la main 

- [x] rajouter autres langues : 

- [x] créer un text index sur tous les champs : { "$ etoile etoile": "text" }
- [x] host le site sur un truc :render
- [x] rajouter une page de login = bp auth (16/04)
- [x] rajouter authorization en fonction des rôles
- [ ] créer un mini admin pour créer et supp des comptes utlisateurs
- [x] refaire combinaison html avec htmx pour avoir un bouton qui add des fields, et pas en avoir 8 statics 
- [x] refaire utils.py pour marcher avec des fields simple, ex : ()
- [x] implementer flask login
- [x] fixer le probleme dans les roles
- [ ] moyen de delete les rows en trop
- [ ] fix l'affichage des resultats de la combinaison

- [ ] inclure les tests des differents bp

## License

Apache-2.0 license

---
