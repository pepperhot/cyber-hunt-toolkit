# targets/ — fiches de scope (le "gate" du systeme)

Chaque programme autorise = un fichier `<programme>.md` ici, derive de sa page officielle (YesWeHack, etc.).
`INDEX.md` = table de lookup host → programme, consultee EN PREMIER quand une cible est donnee.

## Le gate de scope (regle centrale de la flotte)
Avant TOUT test, on lit la fiche du programme concerne et on rend un verdict :

- **IN_SCOPE** — la cible figure explicitement dans `## IN SCOPE`. Le test peut demarrer.
- **OUT_OF_SCOPE** — la cible est absente du scope, ou listee en `## OUT OF SCOPE`. L'agent s'arrete, aucun test lance.
- **UNCLEAR** — la cible est ambigue (ni clairement incluse ni exclue). Remontee a l'orchestrateur ; jamais testee par defaut.

Le gate renvoie TOUJOURS trois choses : **verdict**, **ligne du scope citee**, **raison**.
Ainsi, en cas de blocage, on voit exactement quelle regle s'applique.

## Ajouter un programme
1. Copier `_TEMPLATE-scope.md` vers `<programme>.md`.
2. Remplir IN SCOPE / OUT OF SCOPE / header obligatoire / regles depuis la page officielle du programme.
3. Referencer les hosts dans `INDEX.md`.

> Ce kit est livre SANS aucun programme reel. Les fiches que tu ajoutes ici sont tes donnees ;
> elles ne font pas partie du systeme distribuable.
