# Newo → Akseler: AI Voice Agent Pritaikymo Gidas 🌞

**Sukurta:** 2026-02-10 05:36 AM  
**Remiasi:** 27 detaliomis Newo CAMainFlow skill analizėmis  
**Tikslas:** Paruoštas AI receptionist sprendimas solar leads apdorojimui

---

## 🎯 Executive Summary

Newo.ai CAMainFlow yra 133-skillų voice AI orkestravimo sistema. Šis gidas parodo, kaip pritaikyti jos komponentus Akseler solar lead apdorojimui.

**Galimybės:**
- 🤖 24/7 AI receptionist skambučiams
- 📱 Automatinis SMS follow-up
- 📊 Lead kvalifikacija be žmogaus
- 📅 Kalendoriaus rezervacijos susitikimams
- 🔄 Cross-channel atmintis (skambutis → SMS → Chat)

---

## 🏗️ Architektūros Pritaikymas

### 1. DUAL RUNNER Sistema
```
┌─────────────────────────────────────────────────────────────┐
│  AKSeler AI RECEPTIONIST                                    │
│  ┌─────────────┐    ┌─────────────┐                        │
│  │  guidance   │    │    nsl      │                        │
│  │  (sudėtingi │◄──►│  (paprasti  │                        │
│  │   klausimai)│    │   atsakymai)│                        │
│  └─────────────┘    └─────────────┘                        │
└─────────────────────────────────────────────────────────────┘
```

**Pritaikymas:**
- **Guidance runner:** Sudėtingi techniniai klausimai apie solar (kW, skaičiavimai)
- **NSL runner:** Paprasti klausimai (kada susitikti, kaina, vieta)

---

## 📞 Voice Call Flow (Solar Lead)

### Scenarijus: Naujas skambutis
```
1. SVEIKINIMAS (v2v_greet_user)
   └── "Labas, čia Akseler saulės energetikos konsultantas."
       "Su kuo turiu garbę kalbėti?"

2. INFORMACIJOS RINKIMAS (CAAssessmentFlow)
   ├── Vardas
   ├── Adresas (saulės skaičiavimui)
   ├── Mėnesio elektros sąskaita
   ├── Stogas (tipas, amžius)
   └── Tikslas (ekonomija/nepriklausomybė/EC)

3. KVALIFIKACIJA (Scoring sistema)
   ├── Sąskaita >€50/mėn? (+30 taškų)
   ├── Stogas tinkamas? (+25 taškų)
   ├── Savininkas (ne nuomininkas)? (+20 taškų)
   ├── Sprendimas per 3 mėn? (+15 taškų)
   └── Regionas (artimas biurui)? (+10 taškų)

4. REZULTATAS
   ├── Score ≥70: 🟢 Aukštos kokybės lead → Kalendorius
   ├── Score 40-69: 🟡 Vidutinis → Nurūšiavimas
   └── Score <40: 🔴 Nekvalifikuotas → Švietimas/SMS
```

---

## 📊 CAAssessmentFlow Pritaikymas

### Solar Lead Scoring Template
```yaml
assessment_type: SOLAR_LEAD_QUALIFICATION
questions:
  - id: q1
    text: "Koks Jūsų vardas?"
    type: text
    required: true
    
  - id: q2
    text: "Koks Jūsų adresas?"
    type: address
    required: true
    validation: geocode_address
    
  - id: q3
    text: "Kokia Jūsų vidutinė mėnesio sąskaita už elektrą?"
    type: number
    unit: EUR
    scoring:
      - range: [0, 30]
        points: 0
        note: "Per maža sąnauda"
      - range: [30, 50]
        points: 15
      - range: [50, 100]
        points: 30
      - range: [100, 999]
        points: 40
        
  - id: q4
    text: "Ar esate namo savininkas?"
    type: boolean
    scoring:
      - value: true
        points: 20
      - value: false
        points: 0
        action: "sms_info_for_renters"
        
  - id: q5
    text: "Koks Jūsų stogo tipas?"
    type: choice
    options:
      - "Dvišlaitis metalinis"
      - "Dvišlaitis čerpinis"
      - "Plokščias"
      - "Laužtas/kitoks"
    scoring:
      - option: "Dvišlaitis metalinis"
        points: 25
      - option: "Dvišlaitis čerpinis"
        points: 20
      - option: "Plokščias"
        points: 15
      - option: "Laužtas/kitoks"
        points: 10
        
  - id: q6
    text: "Kada planuojate įsireigyti saulės elektrinę?"
    type: choice
    options:
      - "Artimiausius 1-3 mėnesius"
      - "Per 6 mėnesius"
      - "Per metus"
      - "Tik domiuosi"
    scoring:
      - option: "Artimiausius 1-3 mėnesius"
        points: 15
      - option: "Per 6 mėnesius"
        points: 10
      - option: "Per metus"
        points: 5
      - option: "Tik domiuosi"
        points: 0
```

### Rezultatų Logika
```javascript
if (score >= 70) {
  // 🟢 Aukštos kokybės lead
  trigger("CABookingManagementFlow", {
    service: "on_site_consultation",
    priority: "high",
    duration_minutes: 60
  });
  send_sms_immediately(solar_preparation_checklist);
  
} else if (score >= 40) {
  // 🟡 Vidutinis lead
  trigger("CABookingManagementFlow", {
    service: "video_consultation",
    priority: "medium",
    duration_minutes: 30
  });
  
} else {
  // 🔴 Žemas lead
  send_sms(solar_education_series);
  add_to_nurture_campaign("solar_education");
}
```

---

## 📅 CABookingManagementFlow Pritaikymas

### Susitikimų Tipai
```yaml
booking_types:
  on_site_consultation:
    name: "Konsultacija vietoje"
    duration: 60
    buffer_before: 30
    buffer_after: 30
    requires:
      - roof_access
      - homeowner_present
    reminder_template: "on_site_reminder"
    
  video_consultation:
    name: "Vaizdo konsultacija"
    duration: 30
    buffer_before: 10
    buffer_after: 10
    requires:
      - google_meet_link
    reminder_template: "video_reminder"
    
  phone_followup:
    name: "Telefoninis aptarimas"
    duration: 15
    auto_schedule: true  // AI pasiūlo 3 laikus
    reminder_template: "phone_reminder"
```

### Kalendoriaus Integracija
```javascript
// Working hours pagal regioną
working_hours = {
  "Vilnius": {
    weekdays: "09:00-18:00",
    saturday: "10:00-14:00",
    sunday: "closed"
  },
  "Kaunas": {
    weekdays: "09:00-18:00",
    saturday: "10:00-14:00",
    sunday: "closed"
  }
};

// Susitikimo kūrimas
function create_solar_consultation(lead_data) {
  const slot = find_next_available(
    region = lead_data.region,
    duration = lead_data.consultation_type.duration,
    priority = lead_data.score > 70 ? "high" : "normal"
  );
  
  return {
    title: `Solar konsultacija - ${lead_data.name}`,
    start: slot.start,
    end: slot.end,
    location: lead_data.consultation_type === "on_site" 
      ? lead_data.address 
      : "Google Meet",
    attendees: [
      lead_data.phone,
      assign_consultant(lead_data.region, lead_data.score)
    ],
    reminders: [
      { before: "24h", channel: "sms" },
      { before: "2h", channel: "voice" }
    ]
  };
}
```

---

## 🧠 Cross-Channel Atmintis

### Naudotojo Kelias
```
Dieną 1: SKAMBUYS
├─ AI atsako, surenka info
├─ Score: 75 (aukštas)
├─ Užrezervuojamas susitikimas ketvirtadieniui
└─ SMS: patvirtinimas + paruošimo sąrašas

Dieną 2: SMS
├─ Klientas rašo: "O kiek kW man reikia?"
├─ AI mato istoriją (cross-channel memory)
├─ Atsako: "Pagal Jūsų €87 sąskaitą, rekomenduojame 
│   5kW sistemą. Detaliai aptarsime ketvirtadienį!"
└─ Jokių pasikartojančių klausimų

Dieną 3: SKAMBUYS (priminimas)
├─ AI: "Sveiki Petrai, primenu rytojaus susitikimą 14:00"
├─ Klientas: "Galima perskirti?"
├─ AI perbooking modifikuoja kalendorių
└─ SMS: naujas patvirtinimas
```

---

## 🎭 Voice Design Solar AI

### 15/30 Žodžių Taisyklė
```
❌ Blogai: "Na, žiūrėkite, dėl tos saulės elektrinės, kurią 
minėjote, mums reikėtų pažiūrėti Jūsų stogą, sąskaitas, 
kryptį, metrų kiekį, ir tada galėtume pasakyti kainą..."
(29 žodžių, per ilgas, painu)

✅ Gerai: "Kokia Jūsų vidutinė mėnesio sąskaita už elektrą?"
(9 žodžių, aišku, vienas klausimas)

✅ Detalės (max 30): "Pagal €85 sąskaitą, 5kW sistema 
sutaupytų apie €600 per metus. Stogas tinkamas. 
Kada galėčiau atvykti įvertinti?"
(19 žodžių, konkretu)
```

### Fonetiniai Pataisymai
```yaml
business_phonetic_name: "AK-se-ler"
common_terms:
  kW: "kilovatų"
  EC: "Energetikos centras"
  Garantija: "ga-ran-TI-ja"
  Inverteris: "in-VER-te-ris"
```

---

## 🔄 Tool Calling Integracija

### Solar Skaičiuoklė (Tool)
```javascript
{
  "name": "calculate_solar_savings",
  "description": "Apskaičiuoja sutaupymus pagal sąskaitą ir adresą",
  "parameters": {
    "monthly_bill_eur": 85,
    "address": "Gedimino pr. 1, Vilnius",
    "roof_type": "metal",
    "priority": "savings"  // arba "independence" arba "EC"
  }
}

// Grąžina AI:
"Petrai, pagal Jūsų €85 sąskaitą, rekomenduoju 5kW sistemą. 
Tai sutaupytų apie €680 per metus. EC kompensuotų €3000. 
Įmoka nuo €45/mėn. Domina susitikimas?"
```

### Lead Kūrimas (GoHighLevel)
```javascript
{
  "name": "create_ghl_lead",
  "description": "Sukuria leadą GoHighLevel CRM",
  "parameters": {
    "name": "Petras Petraitis",
    "phone": "+37060012345",
    "address": "Gedimino pr. 1, Vilnius",
    "score": 78,
    "monthly_bill": 85,
    "roof_type": "metal",
    "consultation_booked": "2026-02-15T14:00:00",
    "tags": ["high_quality", "on_site_scheduled", "vilnius"]
  }
}
```

---

## 📱 SMS Templates

### Po Skambučio (aukštas score)
```
Labas [Vardas]! 👋

Dėkoju už pokalbį. Jūsų susitikimas:
📅 [Data], [Laikas]
📍 [Adresas]

Paruoškite:
✅ Paskutinės 3 mėn. sąskaitos
✅ Stogo dokumentai (jei yra)
✅ Klausimų sąrašas

Klausimų? Atsakykite į šį SMS.
Akseler Saulės 🌞
```

### Nurūšiavimas (žemas score)
```
Labas [Vardas]!

Ačiū, kad domitės saulės energija. 
Siunčiu naudingos informacijos:
📊 Skaičiuoklė: [link]
📖 Gidas: [link]

Kai būsite pasiruošę, paskambinkite 
arba atsakykite čia.

Akseler Saulės 🌞
```

---

## 🎯 Implementacijos Planas

### 1 FAZĖ: Pagrindas (1-2 sav.)
- [ ] Voice agent pagrindas (VAPI/OpenAI Realtime)
- [ ] Sveikinimas + 3 pagrindiniai klausimai
- [ ] Lead kūrimas GHL
- [ ] SMS follow-up

### 2 FAZĖ: Kvalifikacija (2-3 sav.)
- [ ] CAAssessmentFlow integracija
- [ ] Scoring sistema (0-100)
- [ ] Automatinis nurūšiavimas
- [ ] Cross-channel atmintis

### 3 FAZĖ: Booking (3-4 sav.)
- [ ] CABookingManagementFlow
- [ ] Kalendoriaus integracija
- [ ] Priminimai (24h, 2h)
- [ ] Perbooking valdymas

### 4 FAZĖ: Optimizacija (4-6 sav.)
- [ ] Tool calling (solar skaičiuoklė)
- [ ] V2V balso tobulinimas
- [ ] A/B testavimas
- [ ] Analytics dashboard

---

## 💰 Prognozuojamas Poveikis

| Metrika | Dabar | Su AI | Pagerėjimas |
|---------|-------|-------|-------------|
| Lead atsakymo laikas | 4-8 val | 24/7 | +∞ |
| Pirmo kontakto trukmė | 30 min | 5 min | 83% greičiau |
| Kvalifikuotų leadų dalis | ? | +40% | geresnis filtras |
| Konsultantų laikas | 100% | 60% | 40% sutaupyta |
| Nepasiekiamų klientų | 30% | 5% | +83% pasiekiamumas |

---

## 🔗 Integracijos

### Būtinos:
- **VAPI/OpenAI Realtime** - Voice infrastruktūra
- **GoHighLevel** - CRM (jau naudojama)
- **Google Calendar** - Susitikimų valdymas
- **Twilio** - SMS siuntimas

### Rekomenduojamos:
- **Make/Zapier** - Workflow automatizavimas
- **Google Maps API** - Stogo analizė
- **PVsyst/SolarEdge** - Skaičiavimai

---

## 📝 Pavyzdinis Pokalbis

**AI:** Labas, čia Akseler saulės energetikos konsultantas. Su kuo turiu garbę kalbėti?

**Klientas:** Labas, aš Jonas iš Vilniaus. Norėčiau pasiteirauti apie saulės elektrinę.

**AI:** Labas Jonai! Džiaugiuosi, kad skambinate. Kad galėčiau geriau patarti, kelis klausimus:
Kokia Jūsų vidutinė mėnesio sąskaita už elektrą?

**Klientas:** Na, apie šimtą eurų.

**AI:** Supratau, €100. Ar esate namo savininkas?

**Klientas:** Taip, savininkas.

**AI:** Puiku. Kokiu adresu?

**Klientas:** Žirmūnų gatvė 45.

**AI:** Ačiū. Pagal Jūsų €100 sąskaitą, rekomenduoju 6kW sistemą. Tai sutaupytų apie €900 per metus. 
Ar Jūsų stogas dvišlaitis, plokščias ar kitoks?

**Klientas:** Dvišlaitis, čerpės.

**AI:** Puikiai tinka. Ar planuojate įsireigyti artimiausius 3 mėnesius?

**Klientas:** Taip, galvoju kovo mėnesį.

**AI:** Puiku! Jūsų situacija labai gera saulės elektrinei. Siūlau susitikti vietoje - apžiūrėsiu stogą, atsakysiu į klausimus, pateiksiu tikslią kainą. Turiu laisvą ketvirtadienį 14 valandą arba šeštadienį 11 valandą. Kuris laikas Jums tinkamesnis?

**Klientas:** Ketvirtadienį gerai.

**AI:** Puiku! Užrezervuoju ketvirtadienį, vasario 13-ąją, 14 valandą, Žirmūnų g. 45. Gausite SMS patvirtinimą su paruošimo sąrašu. Iki pasimatymo!

**[Automatiškai:]**
- Sukurtas leadas GHL (score: 85/100)
- Kalendoriaus rezervacija
- SMS išsiųstas
- Priminimas suplanuotas 24h

---

## 🐾 Sukurta Autonomiškai

**Autorius:** Juodčkis 🐾  
**Duomenys:** 27 Newo CAMainFlow skill analizės  
**Laikas:** 05:36 AM, Tuesday Feb 10  
**Statusas:** Paruošta CEO peržiūrai

---

*Šis gidas sukurtas remiantis detalia Newo.ai CAMainFlow architektūros analize. Jis parodo, kaip enterprise-grade voice AI sistemą pritaikyti konkrečiam Akseler verslo atvejui.*
