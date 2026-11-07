---
id: "E01"
type: epic
title: "🗂️ Epic 01 – Compatibilité des serveurs personnalisés"
status: "Terminé"
labels:
  - "🗂️ epic"
  - "area:generation"
---

# 🗂️ Epic 01 – Compatibilité des serveurs personnalisés

## Contexte

rdgen génère des clients RustDesk destinés à plusieurs variantes de serveurs. Les capacités d'authentification d'un serveur officiel OSS diffèrent de celles d'un serveur Pro ou d'un fork spécialisé.

## Objectif

Produire des clients dont les adaptations de compatibilité sont explicites, limitées au serveur ciblé et vérifiées pendant la génération.

## Travail à réaliser

- [x] Créer la feature de compatibilité du compte API avec le rendezvous OSS.
- [x] Vérifier les implications de sécurité du jeton de compte.
- [x] Prévoir l'arrêt explicite du build si une future version devient incompatible.
- [x] Documenter la décision et les limites du mode OSS.

## Critères d'acceptation (DoD)

- [x] Toutes les features enfants sont terminées ou explicitement reportées.
- [x] La décision de sécurité liée au jeton est documentée.
- [x] Les transformations de source échouent explicitement si leur ancre devient incompatible.
- [x] Les dépendances bloquantes du premier livrable sont résolues.

## Relations

- **Parent** : Aucun, cette issue est un epic.
- **Enfants** :
  - F01.1 — ✨ Compatibilité du compte API avec hbbs OSS

## Dépendances

- **Bloqué par** : Aucun.
- **Bloque** : Aucun.
