# 🚀 GHL Greito Naudojimo Cheat Sheet

**Kauliukas:** 69 (Badaujantis tikslas)  
**Sukurta:** 2026-02-10 02:36 AM

---

## ⚡ Dažniausios Komandos (kopijuoti ir naudoti)

### 1. Kontaktai
```bash
# Ieškoti kontakto
python3 skills/highlevel/scripts/ghl-api.py search_contacts "Vardenis"
python3 skills/highlevel/scripts/ghl-api.py search_contacts "+3706"

# Sukurti kontaktą
python3 skills/highlevel/scripts/ghl-api.py create_contact '{"firstName":"Vardenis","lastName":"Pavardenis","email":"vardenis@example.com","phone":"+37061234567"}'

# Atnaujinti kontaktą
python3 skills/highlevel/scripts/ghl-api.py update_contact "CONTACT_ID" '{"tags":["VIP","Solar"]}'
```

### 2. Pokalbiai (SMS/Email)
```bash
# Išsiųsti žinutę
python3 skills/highlevel/scripts/ghl-api.py send_message "CONTACT_ID" "Sveiki! Gaunate pasiūlymą dėl saulės elektrinės."

# Peržiūrėti pokalbius
python3 skills/highlevel/scripts/ghl-api.py list_conversations
```

### 3. Kalendorius
```bash
# Kalendorių sąrašas
python3 skills/highlevel/scripts/ghl-api.py list_calendars

# Laisvi laikai
python3 skills/highlevel/scripts/ghl-api.py get_free_slots "CALENDAR_ID" "2026-02-10" "2026-02-17"
```

### 4. Pipelines (Opportunities)
```bash
# Peržiūrėti galimybes
python3 skills/highlevel/scripts/ghl-api.py list_opportunities

# Pridėti kontaktą prie workflow
python3 skills/highlevel/scripts/ghl-api.py add_to_workflow "CONTACT_ID" "WORKFLOW_ID"
```

### 5. Sąskaitos ir Produktai
```bash
# Produktų sąrašas
python3 skills/highlevel/scripts/ghl-api.py list_products

# Sąskaitų sąrašas
python3 skills/highlevel/scripts/ghl-api.py list_invoices
```

---

## 🎯 CEO Specifiniai Use Cases

### Saulės Lead'o Apdorojimas
```bash
# 1. Sukurti kontaktą iš lead'o
python3 skills/highlevel/scripts/ghl-api.py create_contact '{"firstName":"Jonas","lastName":"Jonaitis","email":"jonas@example.com","phone":"+37060000000","tags":["Solar Lead","Website"],"customFields":[{"key":"sistemos_galia","value":"10kW"},{"key":"adresas","value":"Vilnius"}]}'

# 2. Išsiųsti pasveikinimo SMS
python3 skills/highlevel/scripts/ghl-api.py send_message "CONTACT_ID" "Ačiū už domėjimąsi saulės elektrine! Netrukus susisieksime su pasiūlymu."

# 3. Pridėti prie nurture workflow
python3 skills/highlevel/scripts/ghl-api.py add_to_workflow "CONTACT_ID" "WORKFLOW_ID"
```

### Follow-up po Susitikimo
```bash
# Ieškoti kontakto
python3 skills/highlevel/scripts/ghl-api.py search_contacts "Jonas"

# Atnaujinti statusą ir pridėti pastabą
python3 skills/highlevel/scripts/ghl-api.py update_contact "CONTACT_ID" '{"tags":["Susitikimas Įvyko","Hot Lead"]}'
```

---

## 📊 Custom API Užklausos

Jei reikia kažko neįprasto:
```bash
# Bet koks API endpoint
python3 skills/highlevel/scripts/ghl-api.py custom_request "GET" "/contacts/" ""
python3 skills/highlevel/scripts/ghl-api.py custom_request "POST" "/contacts/" '{"firstName":"Test"}'
```

---

## 🔧 Pagalba

- **Test connection:** `python3 skills/highlevel/scripts/ghl-api.py test_connection`
- **Visos komandos:** `python3 skills/highlevel/scripts/ghl-api.py` (be argumentų)
- **Setup wizard:** `python3 skills/highlevel/scripts/setup-wizard.py`

---

**Statusas:** ✅ Paruošta naudojimui kai bus credentials
