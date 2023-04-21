# mongo-gsheet
 
todo list : 

- [x] Créer index de recherche textuel 
- [x]  -> problème car atm on doit purge puis remettre toutes la db = suppression de l'index de recherche a chaque fois = il faudrait reussir a append a la db. 
      _Enfaite c'est bon ca append bien, enfaite il faudrait reussir a delete tous les champs qui ont ete push dans la db avec app script comme ca append et on clean au fur et a mesure._

- [x] Connecter la nouvelle db au site live sur heroku avant demain (15/04/23) NON SUR AUTRE
- [x] 1 à 105
- [x] 105 à 210
- [x] 210 à 314
- [x] 300 à 400
- [x] 400 à fin

- [ ] script pour faire automatiquement et pas la main 

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
- [ ] integrer redis pour passer les queryset

- [ ] inclure les tests des differents bp
