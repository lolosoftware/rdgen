# ADR-001 — Séparer le token API du rendezvous OSS

## Statut

Accepté — 2026-11-07

## Contexte

RustDesk réutilise le jeton du compte API dans les demandes envoyées à `hbbs`. Lorsqu'une clé et un jeton sont présents, le client exige un échange `secure_tcp` avant l'envoi. Le serveur officiel OSS ne met pas en œuvre cet échange et n'autorise pas les connexions d'après ce jeton ; la connexion expire alors après 18 secondes. Le jeton reste toutefois nécessaire aux appels HTTPS du carnet d'adresses et du compte.

## Décision

Le générateur Windows expose un mode OSS explicite, activé par défaut, qui conserve la session API HTTP mais remplace localement le jeton par une chaîne vide dans `Client::_start` avant la préparation des demandes de rendezvous et de relais. La transformation utilise une ancre unique et arrête le build si la source RustDesk n'a plus la structure attendue.

## Alternatives considérées

### Utiliser le fork `lejianwen/rustdesk-server`

Ce fork implémente l'échange attendu, mais il est significativement en retard sur le serveur officiel et augmente la surface de code et de confiance à maintenir.

### Neutraliser globalement `secure_tcp` ou les tests de clé

Cette approche rétablit la connexion, mais affaiblit d'autres chemins de sécurité et peut permettre l'envoi accidentel d'un jeton en clair. Elle est rejetée.

### Rester déconnecté du compte API

Cette solution est sûre et fonctionne immédiatement, mais supprime le carnet d'adresses et les fonctions de compte recherchées par l'utilisateur.

## Conséquences positives

- Le serveur officiel OSS peut rester à jour sans fork serveur.
- Le token n'est jamais transmis à un serveur qui ne sait ni le protéger ni l'utiliser.
- Les appels HTTPS authentifiés de l'API restent fonctionnels.

## Conséquences négatives

- `hbbs` ne peut pas imposer une politique de type `MUST_LOGIN` avec ce mode.
- La transformation doit être revalidée lorsque la structure de `Client::_start` évolue.
- Le comportement n'est ajouté qu'au générateur Windows dans ce lot.

## Règles d'usage

Activer ce mode uniquement avec le serveur officiel OSS ou un serveur qui n'utilise pas le token de compte pour autoriser les connexions. Le désactiver avec RustDesk Server Pro, `MUST_LOGIN` ou tout serveur qui valide réellement ce token. Il est interdit de remplacer globalement `!key.is_empty()` ou de neutraliser `secure_tcp` pour obtenir le même résultat.

## Exemples de cas d'usage

```text
API HTTPS tierce + hbbs OSS officiel : option activée
RustDesk Server Pro ou hbbs avec MUST_LOGIN : option désactivée
```

## Références

- F01.1 — Compatibilité du compte API avec hbbs OSS
- T01.1 — Implémenter le mode rendezvous OSS sans token
- https://github.com/rustdesk/rustdesk/issues/16691
- https://github.com/rustdesk/rustdesk/pull/16700
