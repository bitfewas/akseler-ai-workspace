# Akseler AI Voice + CRM Integracijos Planas
*Visa ko ko reikia vienoje vietoje - nuo nulio iki veikiančios sistemos*

**Sukurta:** 2026-02-10 07:06 AM  
**Statusas:** Paruošta diegimui (laukiama GHL credentials)

---

## 🎯 Vienos Eilutės Santrauka

**Newo AI Voice Agent** atsako į skambučius, kvalifikuoja leadus, rezervuoja susitikimus → **GoHighLevel CRM** saugo kontaktus, veda pipeline, siunčia SMS/follow-up → **Tu** gauni užpildytą kalendorių ir šiltus leadus.

---

## 📋 Diegimo Checklist

### Fazė 1: GHL Paruošimas (30 min)
- [ ] Gauti API Token iš CEO
- [ ] Gauti Location ID
- [ ] Patikrinti ar veikia `ghl-test-suite.py`
- [ ] Sukurti Custom Fields Akseler

### Fazė 2: Newo Voice Setup (1-2h)
- [ ] Sukonfigūruoti telefono numerį
- [ ] Įkelti Akseler voice persona
- [ ] Sudėti tool calling (calculator, booking)
- [ ] Testinis skambutis

### Fazė 3: Integracija (30 min)
- [ ] Suvesti GHL credentials į Newo
- [ ] Įjungti real-time sync
- [ ] Testinis end-to-end flow

### Fazė 4: Go Live (15 min)
- [ ] Perjungti telefoną į production
- [ ] Įjungti monitoring
- [ ] Paleisti

---

## 🔧 GHL Paruošimo Instrukcijos

### 1. Gauti Credentials

CEO turi nueiti į:
```
https://app.gohighlevel.com/
→ Settings → Business Profile → API Keys
```

Reikalingi duomenys:
```bash
HIGHLEVEL_TOKEN="verslo_api_raktas_ka_64_simboliu"
HIGHLEVEL_LOCATION_ID="location_id_ka_20_simboliu"
```

### 2. Custom Fields Sukūrimas

Eiti į: `Settings → Custom Fields → Add Field`

| Lauko pavadinimas | Tipas | Paskirtis |
|-------------------|-------|-----------|
| `solar_roof_type` | Text | Stogo tipas |
| `solar_monthly_bill` | Number | Elektros sąskaita |
| `solar_house_size` | Text | Namo dydis |
| `solar_qualification_score` | Number | Lead score (0-100) |
| `lead_source` | Text | Iš kur atėjo |

### 3. Pipeline Sukūrimas

Eiti į: `Opportunities → Pipelines → Create Pipeline`

**Pipeline pavadinimas:** "Solar Leads"

**Stage'ai:**
1. **New Lead** (automatinis)
2. **Qualified** (po voice call)
3. **Appointment Set** (kai užrezervuota)
4. **Showed** (pasirodė)
5. **Proposal Sent** (pasiūlymas)
6. **Won** (laimėta!)
7. **Lost** (prarasta)

### 4. Workflow'ai

Jau sukurti `ghl-workflows.md` - CEO gali importuoti.

---

## 🎙️ Newo Voice Konfigūracija

### Voice Persona Template

```
Tu esi Akseler solar konsultantas. Būdas:
- Profesionalus bet draugiškas
- Aiškiai paaiškini naudą
- Nieko nepraleidi - visada paklausinėji
- Kalbi lėtai ir aiškiai (voice)

Tavo tikslas:
1. Pasveikinti ir sužinoti vardą
2. Kvalifikuoti leadą (3 klausimai)
3. Pasiūlyti susitikimą
4. Užrezervuoti laiką

Niekada:
- Neparduodi tiesiogiai telefonu
- Nežadi kainų be pamatavimo
- Nepalieki be next step
```

### Tool Calling Schema

**calculator.nsl** jau turi:
```javascript
// Saulės skaičiuoklės tool
{
  "name": "calculate_solar_savings",
  "parameters": {
    "monthly_bill": "number",
    "roof_type": "string",
    "house_size": "string"
  },
  "returns": {
    "estimated_savings": "number",
    "payback_years": "number",
    "system_size_kw": "number"
  }
}
```

**booking integration:**
```javascript
// CABookingManagementFlow
{
  "name": "check_availability",
  "parameters": {
    "date": "string",
    "duration_minutes": "number"
  }
}
{
  "name": "book_appointment",
  "parameters": {
    "contact_name": "string",
    "contact_phone": "string",
    "date_time": "string",
    "notes": "string"
  }
}
```

---

## 🔄 Duomenų Srautas (Data Flow)

```
[Skambutis ateina]
    ↓
[Newo Voice AI]
    ↓
┌─────────────────────────────────────┐
│  1. Greeting + Vardo išsiaiškinimas │
│  2. Kvalifikacija (CAAssessmentFlow)│
│  3. Skaičiuoklė (calculator)        │
│  4. Booking (CABookingManagement)   │
└─────────────────────────────────────┘
    ↓
[GHL CRM]
    ↓
┌─────────────────────────────────────┐
│  • Kontaktas sukurta/atnaujintas    │
│  • Custom fields užpildyti          │
│  • Pipeline stage = "Qualified"     │
│  • Task sukurtas follow-up          │
│  • SMS priminimas užprogramuotas    │
└─────────────────────────────────────┘
    ↓
[CEO gauna:]
    • Užpildytą kalendorių
    • Kvalifikuotą leadą CRM
    • Priminimus apie susitikimus
```

---

## 📊 Kvalifikacijos Scoring

**CAAssessmentFlow** naudoja šią logiką:

```
Bazinis balas: 50 taškų

+30 taškų jei:
  ✓ Mėnesinė sąskaita > €100
  ✓ Nuosavas namas
  ✓ Stogas geros būklės

+20 taškų jei:
  ✓ Planuoja renovaciją
  ✓ Domisi > 3 mėn
  ✓ Rekomendacija

-20 taškų jei:
  ✓ Butas (ne namas)
  ✓ Nuomoja
  ✓ Sąskaita < €50

Rezultatas:
80-100 = Karštas lead (skambinti šiandien)
60-79 = Šiltas lead (siųsti pasiūlymą)
<60 = Šaltas lead (į nurture kampaniją)
```

---

## 📝 Voice Script Pavyzdys

**[Skambutis priimtas]**

> "Labas! Čia Akseler, aš Juodčkis. Girdžiu, domitės saulės elektrine?"

**[Taip]**

> "Puiku! Norėčiau užduoti kelis klausimus, kad geriau suprasčiau jūsų situaciją. Pirmiausia - kiek maždaug mokate už elektrą per mėnesį?"

**[€150]**

> "Aha, tai tikrai verta žiūrėti. Gyvenate nuosavame name ar bute?"

**[Nuosavame]**

> "Puiku! Ir paskutinis klausimas - jūsų stogas kokio tipo? Čerpės, metalas, šiferis?"

**[Čerpės]**

> "Supratau. Tai toks namas puikiai tinka. Galiu apskaičiuoti preliminarią naudą - mano skaičiavimais, su €150 sąskaita per mėnesį sutaupytumėte apie €1200 per metus. Atsipirkimas būtų maždaug per 6-7 metus, o sistema dirbtų 25+ metus.

> Dabar norėčiau pasiūlyti nemokamą konsultaciją su mūsų specialistu. Jis atvažiuos, apžiūrės stogą, ir paruoš tikslų pasiūlymą. Kuris laikas jums būtų patogesnis - rytinis ar popietinis?"

**[Popietinis]**

> "Puiku! Turiu laisvą ketvirtadienį 14:00 arba penktadienį 16:00. Kuris geriau?"

**[Ketvirtadienis]**

> "Užrezervuota! Ketvirtadienį 14:00. Dar kartą - jūsų vardas?"

**[Jonas]**

> "Ačiū, Jonas. Gausite SMS priminimą dieną prieš. Lauksime jūsų!"

---

## 🚀 Greito Starto Komandos

Kai CEO duos credentials, paleisti:

```bash
# 1. Testuoti ar GHL veikia
cd /data/.openclaw/workspace
python3 ghl-test-suite.py

# 2. Įrašyti credentials į .env
echo "HIGHLEVEL_TOKEN=gaunu_iscio" >> .env
echo "HIGHLEVEL_LOCATION_ID=ir_šią" >> .env

# 3. Paleisti automatizavimą
python3 ghl-solar-automation.py --mode=process-new-leads

# 4. Nustatyti cron kasdieniam paleidimui
python3 ghl-solar-automation.py --setup-cron
```

---

## 📈 Metrikos Sekimas

**Ką sekti GHL:**

| Metrika | Targetas | Kur matyti |
|---------|----------|------------|
| Lead → Qualified | >60% | Pipeline stats |
| Qualified → Appointment | >40% | Stage conversion |
| Appointment → Showed | >70% | Calendar |
| Showed → Won | >30% | Revenue |
| Average deal size | >€8000 | Opportunities |

**Ką sekti Newo:**

| Metrika | Targetas | Kur matyti |
|---------|----------|------------|
| Call answer rate | >80% | Dashboard |
| Avg call duration | >3 min | Analytics |
| Booking success | >50% | Conversion |
| Customer satisfaction | >4.5/5 | Feedback |

---

## 🆘 Troubleshooting

**Problema:** Newo neperduoda į GHL  
**Sprendimas:** Patikrinti API key, location ID, ar workflow įjungtas

**Problema:** Kalendoriuje nėra laisvų laikų  
**Sprendimas:** Patikrinti GHL Calendar nustatymus, working hours

**Problema:** Leadai nepažymimi "Qualified"  
**Sprendimas:** Patikrinti scoring thresholds CAAssessmentFlow

**Problema:** SMS neina  
**Sprendimas:** Patikrinti GHL SMS credits, phone verification

---

## 📞 Kontaktai ir Resursai

**Šalia guli:**
- `ghl-cheatsheet.md` - greitos komandos
- `ghl-workflows.md` - 7 workflow pavyzdžiai  
- `ghl-solar-automation.py` - Python scriptas
- `newo-to-akseler-implementation-guide.md` - detalus voice setup
- `newo-architecture-synthesis.md` - architektūros principai

**CEO turi padaryti:**
1. Gauti GHL credentials
2. Perduoti man API key + Location ID
3. Sudėti Custom Fields
4. Sukurti Pipeline

**Aš galiu padaryti:**
1. Visa kita automatizuoti
2. Nustatyti workflow'us
3. Testuoti end-to-end
4. Stebėti ir optimizuoti

---

## ✅ Next Step

**CEO:** Duoti GHL API Token ir Location ID. Tada paleidžiam per 15 min.

**Arba:** Jei nori pirma testiniu režimu - galiu sukurti test environment su fake data.

---

*Sukurta Juodčkio | Akseler AI Partneris*
