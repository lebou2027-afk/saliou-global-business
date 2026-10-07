# SALIOU GLOBAL BUSINESS - Déploiement

## Option 1 : Render (recommandé)

1. Créez un compte Render.
2. Connectez votre dépôt GitHub.
3. Cliquez sur "New +" puis "Blueprint".
4. Sélectionnez le dépôt `saliou-global-business`.
5. Render lira automatiquement `render.yaml`.
6. Ajustez l'URL du frontend vers le backend après le premier déploiement.

### Valeurs à vérifier

- Backend: `saliou-backend.onrender.com`
- Frontend: `saliou-frontend.onrender.com`
- Dans le frontend, l'environnement `VITE_API_URL` doit pointer vers le backend.

## Option 2 : Railway

1. Connecter le dépôt GitHub
2. Ajouter le service backend avec `backend/`
3. Ajouter le service frontend avec `frontend/`
4. Définir `VITE_API_URL` au bon endpoint backend

## Option 3 : Docker local

```bash
docker-compose up --build
```

## Variables essentielles

- `OPENAI_API_KEY` (optionnel)
- `VITE_API_URL`
