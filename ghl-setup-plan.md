# GHL Setup Planas - Akseler

**Sukurta:** 2026-02-10 02:06 AM
**Status:** Laukia CEO veiksmų

---

## 🔑 Žingsnis 1: Private Integration Sukūrimas

### Instrukcijos:
1. Eiti į **app.gohighlevel.com**
2. Perjungti į **Sub-Account** (Akseler)
3. **Settings** (apačioje kairėje) → **Private Integrations**
   - Jei nematote: Settings → Labs → įjungti Private Integrations
4. **"Create new Integration"**
5. Pavadinimas: **"Juodčkis AI Assistant"**
6. Pažymėti VISUS scopes (kad galėčiau dirbti pilnai):
   - `contacts.readonly`, `contacts.write`
   - `conversations.readonly`, `conversations.write`
   - `calendars.readonly`, `calendars.write`
   - `opportunities.readonly`, `opportunities.write`
   - `workflows.readonly`, `workflows.write`
   - `invoices.readonly`, `invoices.write`
   - `payments.readonly`, `payments.write`
   - `products.readonly`, `products.write`
   - `locations.readonly`, `locations.write`
   - `users.readonly`, `users.write`
   - `forms.readonly`, `forms.write`
   - `voice-ai.readonly`, `voice-ai.write`
   - Ir kiti...

7. **Kopijuoti tokeną** (rodomas tik kartą!)

---

## 📍 Žingsnis 2: Location ID

1. Settings → **Business Info**
2. Location ID nurodytas General Information
3. Arba URL: `app.gohighlevel.com/v2/location/{LOCATION_ID}/...`

---

## ⚙️ Žingsnis 3: Environment Variables

```bash
export HIGHLEVEL_TOKEN="jūsų-tokenas-čia"
export HIGHLEVEL_LOCATION_ID="jūsų-location-id"
```

Pridėti į `~/.bashrc` arba `.env` failą workspace root'e.

---

## 🧪 Žingsnis 4: Testas

Paleisti: `python3 scripts/ghl-api.py test_connection`

---

## 💡 Greitos Galimybės (kai bus setup)

### Automation Ideas:
1. **Lead Scoring** - automatiškai vertinti leadus pagal veiksmus
2. **Follow-up Sequences** - sukurti pasirinktinius workflow
3. **Calendar Optimization** - rasti geriausius laikus susitikimams
4. **Voice AI** - sukonfigūruoti AI agentą skambučiams
5. **Invoice Automation** - automatiniai priminimai ir sekimas
6. **Contact Enrichment** - papildyti kontaktus iš išorinių šaltinių
7. **Pipeline Analytics** - analizuoti konversijas tarp etapų

### Solar Lead Specific:
- Automatinis DAL (daylight analysis) scoring
- Geografinis lead prioritetavimas
- Orų integracija (debesuota = geresnis laikas skambinti)

---

## 📚 Resursai

- **Skill docs:** `/data/.openclaw/workspace/skills/highlevel/`
- **API helper:** `scripts/ghl-api.py`
- **Setup wizard:** `scripts/setup-wizard.py`
- **Official docs:** https://marketplace.gohighlevel.com/docs/

---

## ⏳ Laukiama

CEO nustato environment variables, tada galiu pradėti pilną integraciją.
