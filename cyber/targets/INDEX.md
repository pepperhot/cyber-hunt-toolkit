# INDEX DES SCOPES — base de lookup

> Fichier de reference central. Quand une URL/cible est donnee, on la matche d'abord dans la
> **table de lookup** ci-dessous, puis on applique la fiche du programme correspondant
> (`~/cyber/targets/<programme>.md` : header obligatoire + intensite autorisee + regles).
> Source de verite = la page officielle de chaque programme. Reverifier le scope avant une session.

---

## 1. TABLE DE LOOKUP (host → programme)

| Host / pattern | Programme | In-scope ? | Intensite max autorisee |
|---|---|---|---|
| `<host-ou-pattern>` | `<programme>` | ✅ / ❌ / ⚠️ | `<recon+scan+PoC / manuel cible / lecture passive>` |

## 2. CONVENTION
- ✅ in-scope  •  ❌ out of scope  •  ⚠️ conditions (lecture passive seule, pas d'auto massive, etc.)
- Une entree par asset/pattern. Les exclusions explicites (`/legacy/*`, sous-domaines hors scope) ont leur propre ligne ❌.
- Ajouter un programme = creer `~/cyber/targets/<programme>.md` (voir `_TEMPLATE-scope.md`) PUIS referencer ses hosts ici.
- En cas de non-correspondance ou d'ambiguite d'une cible dans cette table -> verdict UNCLEAR, remontee a l'orchestrateur, jamais de test par defaut.
