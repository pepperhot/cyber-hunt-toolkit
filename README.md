# Cyber Hunt Toolkit — flotte de subagents YesWeHack (scope-gated)

Kit **portable** d'une flotte de subagents de chasse aux vulnerabilites sur programmes
**bug bounty autorises** (YesWeHack & assimiles). Il regroupe les **agents** et les **methodes de recherche**,
PAS les comptes rendus ni les donnees de programmes privees.

## Contenu
- `agents/` — **31 definitions de subagents** (frontmatter `name/description/tools[/model]` + role & methode). A installer dans `~/.claude/agents/`.
- `cyber/` — l'arborescence de travail, a installer dans `~/cyber/` :
  - `targets/` — le **gate de scope** : `README.md`, `_TEMPLATE-scope.md`, `INDEX.md` (table de lookup vide).
  - `knowledge/` — memoire partagee **vide / templatee** : `README.md`, `coverage-log.md`, `findings-log.md`, `patterns.md`, `lessons.md`, `playbooks/_TEMPLATE-playbook.md`, `custom-nuclei/`, `cve/`, `cwe/` (referentiel CWE generique public).
  - `runs/` — vide ; un sous-dossier par run (`<programme>-<date>/`).
- `INSTALL-PROMPT.md` — prompt a coller dans Claude Code pour installer/activer la flotte.

## Ce qu'il n'y a PAS (volontairement)
Aucune fiche de programme reel, aucun run, aucune entree reelle de `coverage-log` / `findings-log` /
`lessons` / `monitor-log`. Le kit s'installe "a blanc" : tu ajoutes tes programmes autorises via
`cyber/targets/_TEMPLATE-scope.md`.

## Les 31 agents (par groupe)
| Groupe | Agents |
|---|---|
| Meta / build | `meta-agent` → `cyber-builder` |
| Orchestration + garde-fous | `orchestrateur`, `compliance-gate`, `dedup-check` |
| Reconnaissance | `recon`, `js-recon`, `cve-matcher`, `scanner` |
| Chasseurs web | `web-auth`, `xss-hunter`, `idor-hunter`, `cors-clickjack`, `logic-abuse`, `secret-hunter` |
| Chasseurs API | `api-rest`, `graphql-hunter`, `ssrf-hunter` |
| Chasseurs specialises | `payment-logic`, `mobile-apk`, `llm-prompt-injection`, `cloud-misconfig`, `iot-router` |
| Validation / preuve | `validateur`, `exploit-poc`, `evidence-capture`, `chain-builder` |
| Rapports | `reporter-ywh`, `reporter-learn`, `triage-writer`, `vps-manager` |

## Pipeline d'un run
```
compliance-gate (GO/BLOCK)
  -> recon + js-recon + cve-matcher
  -> chasseurs metier (selon le type de cible)
  -> VALIDATEUR (pivot qualite : rien ne part sans lui)
  -> dedup-check -> exploit-poc -> evidence-capture
  -> chain-builder (combine les findings confirmes)
  -> reporter-ywh (+ reporter-learn)   |   triage-writer (relances)   |   vps-manager (cleanup)
```

## Contrat de chemins (chemins absolus referencés par les agents)
- Scope d'un programme : `~/cyber/targets/<programme>.md` (+ lookup `~/cyber/targets/INDEX.md`)
- Memoire partagee : `~/cyber/knowledge/coverage-log.md`, `patterns.md`, `findings-log.md`
- Sorties d'un run : `~/cyber/runs/<programme>-<date>/`

> Les agents sont livres **tels quels** (etat courant). Quelques references heritees pointent vers
> `scope/<programme>.md` ; le chemin canonique retenu est `~/cyber/targets/<programme>.md`.

## Regles de conduite (non negociables)
- Agir uniquement sur une cible explicitement **IN SCOPE** d'un programme autorise. Hors scope / ambigu → `OUT_OF_SCOPE` / `UNCLEAR`, STOP.
- Preuve minimale, **non destructive**. Aucune donnee personnelle/financiere reelle de tiers lue, copiee ou conservee.
- **Comptes de test uniquement.** Pas de DoS, bruteforce massif, exfiltration, persistance, mouvement lateral.
- Arret immediat si erreurs en serie, ralentissement visible, ou acces a des donnees tierces.

## Installation
Voir **`INSTALL-PROMPT.md`**.

## Licence
MIT — voir [`LICENSE`](LICENSE). Usage strictement sur des programmes et cibles **autorises**.
