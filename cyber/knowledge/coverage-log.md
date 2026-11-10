# Coverage log (memoire partagee entre hunters)

Format par ligne, une ligne par vecteur teste (positif OU negatif):
date|programme|stack|vecteur|resultat

Pas de caractere `|` dans un champ libre (vecteur/resultat) -- separe plusieurs elements internes avec `;`. Une ligne qui ne respecte pas 5 champs separes par `|` est a considerer invalide/illisible par les hunters suivants, donc a corriger.

Regles d'usage:
- `stack` = la techno telle qu'identifiee par recon (tech-detect de live.txt) ou fournie explicitement par l'utilisateur -- pas une estimation personnelle du hunter.
- Chaque hunter grep ce fichier sur la `stack` de la cible courante AVANT de tester. Un vecteur deja documente "non concluant" sur la MEME stack et une version/config equivalente n'est pas retente sans raison nouvelle explicite (version differente, config specifique, ou point d'entree non couvert par l'entree existante) -- cette raison doit pouvoir etre formulee en une phrase si on la demande.
- Chaque hunter ajoute une ligne apres CHAQUE vecteur teste, meme si le resultat est negatif/non concluant -- c'est justement ce qui a de la valeur pour les prochains runs.
- Distinct de ~/cyber/knowledge/patterns.md (reporter-learn): patterns.md est curé et pédagogique pour les findings CONFIRMES; coverage-log.md est la trace brute de couverture, positive ou négative, pour tout vecteur testé.

<!-- EXEMPLE (a retirer une fois les premieres vraies entrees ajoutees):
2026-10-18|acme-corp|django-rest|IDOR UUID sur /api/v1/invoices/{id}|non concluant: UUID v4 non previsible
2026-10-18|acme-corp|nginx;cloudflare|XSS reflechi sur ?q=|non concluant: WAF bloque <script> et onerror
-->
