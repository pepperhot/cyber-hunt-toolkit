# Prompt d'installation — Cyber Hunt Toolkit

> Colle le bloc ci-dessous dans une session **Claude Code ouverte a la racine du dossier `toolkit/`** (ce kit).
> Il installe la flotte de subagents + l'arborescence de travail, puis verifie. Il n'execute aucune action offensive.

---

```
Tu installes une flotte de subagents de chasse aux vulnerabilites sur programmes bug bounty AUTORISES
(YesWeHack). Le dossier courant (le kit) contient `agents/` et `cyber/`. Procede ainsi, etape par etape,
sans rien tester d'offensif toi-meme :

## 1. Pre-vol
- Confirme que le dossier courant contient `agents/*.md` (31 fichiers) et `cyber/` (targets, knowledge, runs).
- Cibles d'installation : `~/.claude/agents/` (subagents) et `~/cyber/` (travail).
- Si des fichiers existent deja a ces emplacements, N'ECRASE RIEN : liste les conflits et attends mon accord.

## 2. Installer les agents
- Copie `agents/*.md` vers `~/.claude/agents/`.
- Verifie que chaque fichier a un frontmatter valide (`name`, `description`, `tools`, et `model` si present)
  et que les 31 `name:` sont uniques.

## 3. Installer l'arborescence de travail
- Copie le contenu de `cyber/` vers `~/cyber/` (targets/, knowledge/, runs/).
- `~/cyber/knowledge/` doit contenir : README.md, coverage-log.md, findings-log.md, patterns.md, lessons.md,
  playbooks/, custom-nuclei/, cve/, cwe/.
- `~/cyber/targets/` doit contenir : README.md, _TEMPLATE-scope.md, INDEX.md.
- N'ajoute AUCUN secret (mot de passe, token, cookie) dans `~/cyber/knowledge/`.

## 4. Contrat de chemins (a respecter, les agents en dependent)
- Scope d'un programme : `~/cyber/targets/<programme>.md`  (+ lookup `~/cyber/targets/INDEX.md`)
- Memoire partagee     : `~/cyber/knowledge/coverage-log.md`, `patterns.md`, `findings-log.md`
- Sorties d'un run      : `~/cyber/runs/<programme>-<date>/`

## 5. Verification
- `ls ~/.claude/agents/*.md | wc -l`  doit donner 31.
- Les 31 `name:` sont uniques (aucun doublon).
- Affiche l'arbre de `~/cyber/` sur 2 niveaux.
- Rappelle-moi qu'AUCUN programme reel n'est encore configure. Pour en ajouter un :
  copier `~/cyber/targets/_TEMPLATE-scope.md` vers `<programme>.md`, le remplir depuis la page officielle
  du programme, puis referencer ses hosts dans `~/cyber/targets/INDEX.md`.

## 6. Regles de conduite de la flotte (a ne jamais contourner)
- Agir uniquement sur une cible explicitement IN SCOPE d'un programme autorise.
  Hors scope ou ambigu -> verdict OUT_OF_SCOPE / UNCLEAR, STOP, aucune action.
- Preuve minimale, non destructive. Aucune donnee personnelle/financiere reelle de tiers
  lue, copiee ou conservee.
- Comptes de test uniquement. Pas de DoS, bruteforce massif, exfiltration, persistance, mouvement lateral.
- Arret immediat si erreurs en serie, ralentissement visible, ou acces a des donnees tierces.
- meta-agent et cyber-builder ne creent AUCUN outil offensif : documentation et configuration seulement.

## 7. Utilisation (une fois un programme configure)
- Lancer une mission : invoque le subagent `orchestrateur` avec une cible autorisee.
  Il verifie le scope via `compliance-gate`, delegue recon -> hunters -> validateur -> dedup-check
  -> exploit-poc / evidence-capture -> reporter-ywh, et consolide l'etat dans le dossier du run.

Ton role ici est UNIQUEMENT d'installer et de verifier. Ne cree aucun nouvel agent ni outil offensif.
```
