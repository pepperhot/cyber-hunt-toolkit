# Base de connaissance de la flotte
Boucle (après CHAQUE cible) :
1. reporter-learn -> lessons.md (marché / raté / idée)
2. findings confirmés -> findings-log.md
3. pattern récurrent -> playbooks/
4. vuln hors nuclei -> custom-nuclei/
5. cyber-builder relit ce dossier avant chaque mission.

Sous-dossiers :
- cwe/   : référentiel CWE (index.json + raw/ source MITRE)
- cve/   : CVE importées par produit (NVD)
- playbooks/, custom-nuclei/ : tactiques et templates maison
Règle : aucun secret (mot de passe, token, cookie) dans ce dossier.
