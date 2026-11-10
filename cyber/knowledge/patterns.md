# Patterns reutilisables inter-runs

But: contrairement a lessons.md (recit pedagogique par challenge), ce fichier est
une liste COURTE et CONSULTABLE de patterns qui ont deja marche, indexee pour qu'un
hunter puisse verifier en quelques secondes avant de tester a l'aveugle. Alimente
par reporter-learn a la fin de chaque run confirme. Consulte par les agents "metier"
(web-auth, idor-hunter, ssrf-hunter, xss-hunter, api-rest, graphql-hunter, etc.)
au debut de leur chaine, avant de lancer leurs tests.

## Format d'une entree (5 lignes max, scannable)
- **Signal** : ce qui a mis la puce a l'oreille
- **A marche** : la technique/payload qui a paye
- **A rate** : variante testee sans succes (pour ne pas la reprendre a l'aveugle)
- **Stack/contexte** : techno concernee
- **Source** : programme / run

Regle: n'ajouter une entree QUE pour un finding CONFIRME (jamais un REJETE/DOUTE).

<!-- EXEMPLE (a retirer une fois les premieres vraies entrees ajoutees):
### SSRF via import d'avatar par URL
- Signal : champ "photo de profil" accepte une URL distante
- A marche : 169.254.169.254/latest/meta-data/iam/ renvoie le role IAM
- A rate : file:// et gopher:// filtres cote serveur
- Stack : AWS EC2 ; Node/Express
- Source : <programme> / <run>
-->
