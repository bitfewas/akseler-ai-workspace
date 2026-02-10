# 🔧 GoHighLevel - Paruošimo Dokumentas

**Sukurta:** 2026-02-10 02:21 AM  
**Statusas:** Laukia CEO veiksmų

---

## ✅ Ką Padariau Šiame Cikle

Kadangi kauliukas buvo **68** (badaujantis tikslas 60-79), dirbau su GHL pasiruošimu:

1. **Peržiūrėjau SKILL.md** - supratau visas 39 API galimybes
2. **Patikrinau scripts/** - setup-wizard.py ir ghl-api.py paruošti
3. **Patikrinau aplinkos kintamuosius** - abu tušti (laukia konfigūracijos)
4. **Sukūriau šį dokumentą** - žingsnis po žingsnio instrukcijos

---

## 🚀 Ko Reikia Nustatymui

### 1. HIGHLEVEL_TOKEN (Private Integration)

**Kaip gauti:**
1. Eiti į app.gohighlevel.com
2. Perjungti į Sub-Account (arba likti Agency view)
3. Settings → Private Integrations
   - Jei nematyti: Settings → Labs → Private Integrations ON
4. "Create new Integration"
5. Įvesti pavadinimą (pvz. "Claude AI Assistant")
6. **Pažymėti VISUS scopes** (contacts, conversations, calendars, opportunities, etc.)
7. Copy token (rodomas tik kartą!)

### 2. HIGHLEVEL_LOCATION_ID

**Kaip gauti:**
1. Sub-account Settings → Business Info
2. Location ID matomas General Information
3. ARBA pažiūrėti URL: `/location/{ID}/`

---

## 🎯 Greita Peržiūra: Ką Galėsime Daryti

| Funkcija | Nauda CEO |
|----------|-----------|
| **Contacts** | Automatinis lead'ų valdymas |
| **Conversations** | SMS/Email/WhatsApp iš vienos vietos |
| **Calendars** | Susitikimų rezervacija be vargo |
| **Opportunities** | Pipeline valdymas, pasiūlymai |
| **Workflows** | Automatizacijos kūrimas |
| **Invoices** | Sąskaitų siuntimas |
| **Voice AI** | AI agentai telefonu |

---

## 📝 Greitas Nustatymas (kai bus credentials)

```bash
# 1. Nustatyti kintamuosius
export HIGHLEVEL_TOKEN="your-token-here"
export HIGHLEVEL_LOCATION_ID="your-location-id"

# 2. Paleisti wizard
python3 /data/.openclaw/workspace/skills/highlevel/scripts/setup-wizard.py

# 3. Test connection
python3 /data/.openclaw/workspace/skills/highlevel/scripts/ghl-api.py test_connection

# 4. Quick win - pirmi 5 kontaktai
python3 /data/.openclaw/workspace/skills/highlevel/scripts/ghl-api.py search_contacts
```

---

## 🔮 Kitas Žingsnis

Kai CEO suteiks token ir location ID, galiu:
- Paleisti setup wizard
- Test connection
- Pradėti kurti automations
- Optimizuoti workflows

---

**Paruošta:** ✅  
**Laukia:** CEO credentials
