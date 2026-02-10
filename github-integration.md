# GitHub Integration - Konfigūracija

**Token sukurtas:** 2026-02-10  
**Username:** bitfewas  
**Token expiry:** 90 dienų (galioja iki ~2026-05-11)

---

## 🔐 Prieigos Teisės

Token leidžia:
- ✅ Skaityti visus public/private repozitorijus
- ✅ Kurti/redaguoti issues ir pull requestus
- ✅ Pushinti kodą (commit, branch, merge)
- ✅ Tvarkyti GitHub Actions workflows
- ✅ Skaityti organizacijos narystes

---

## 📁 Repozitorijos

### Prieinamos repozitorijos:

```
bitfewas/REPO_NAME - public/private - Aprašymas
```

*(Atnaujinti pagal realų sąrašą)*

---

## 🛠️ Naudojimas

### API užklausos pavyzdys:
```bash
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/user/repos
```

### Issues sąrašas:
```bash
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/OWNER/REPO/issues
```

### Naujas issue:
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/OWNER/REPO/issues \
  -d '{"title":"Title","body":"Description"}'
```

---

## 🔒 Saugumas

- Token saugomas `.env` faile (chmod 600)
- Nekommitinamas į git
- Galiojimas: 90 dienų
- **Niekam nerodyti tokeno!**

---

## Token Atnaujinimas

Kad token nebūtų rodomas šiame faile, jis saugomas atskirame `.env` faile.

Jei reikia atnaujinti:
1. Sukurti naują tokeną GitHub
2. Atnaujinti `.env` failą
3. Ištrinti seną tokeną GitHub pusėje
