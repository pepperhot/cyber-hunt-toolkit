# Scope - <NOM DU PROGRAMME> (<plateforme: YesWeHack / autre>)

<Statut d'acces: public / prive (invitation acceptee, role Hunter confirme)>.
Source de verite = la page officielle du programme ; reverifier le scope avant CHAQUE session.

## IN SCOPE
- https://<asset-1> (<type: Web / API / Mobile / IoT / IA...>) - asset value <Low/Medium/High/Critical>
- https://<asset-2> (...) - <valeur>
- <wildcard autorise, ex: *.example.com, si explicitement couvert>

## OUT OF SCOPE
- Tout domaine/sous-domaine/asset non liste ci-dessus
- https://<exclusion-explicite-1>   (ex: /legacy/*, environnement de prod, sous-domaine tiers)
- <services tiers, assets d'autres entites, etc.>

## REGLE CRITIQUE - IDENTIFICATION DE L'ACTIVITE
- <Header/marqueur obligatoire impose par le programme, ex: suffixe User-Agent `...`>
- <Comptes de test: comment les obtenir, privileges, perimetre d'usage>

## Regles de test (obligatoire)
- <Rate limit / intensite max autorisee (recon+scan+PoC / manuel cible / lecture passive)>
- <Instance partagee avec d'autres chercheurs ? ne pas les gener, ne pas toucher leurs ressources>
- <Interdits explicites: DoS, degradation, bruteforce, scanners massifs, suppression/modif de ressources tierces>
- Pas de PII dans le rapport -> REDACT/OBFUSCATE dans tout PoC
- Identifiants/secrets exposes -> verifier la validite UNIQUEMENT, jamais exploiter
- Fuite d'info sensible -> decrire/lister, JAMAIS extraire/copier l'integralite

## Recompenses (indicatif)
- <Grille par asset value si connue : Low / Medium / High / Critical>

## Vulnerabilites qualifiantes
- <Liste, ou renvoi a la politique du programme>

## Non qualifiant (notable)
- <Pieges connus: ce que le programme rejette explicitement (ex: self-XSS, user enumeration, CVE sans PoC, "improper access control" generique...)>

## Notes
- <Premier a signaler = seul eligible ? Collaboration ? Specificites du programme.>
