# Akseler Lead Scoring & Prioritizacijos Sistema

**ADHD-friendly versija:** Viskas vienoje vietoje, spalvota, greitai skaitoma.

---

## 🎯 Kodėl Tai Svarbu

Ne visi leadai vienodi. Kai kuriems reikia skambinti DABAR, kitus galima palikti rytojui. Ši sistema padeda per 30 sekundžių nuspręsti kas svarbu.

**Rezultatas:** Daugiau laiko geriausiems leadams = daugiau pardavimų.

---

## 📊 Lead Scoring Formulė (0-100 taškų)

### Demografiniai (30 taškų max)

| Kriterijus | Taškai | Kodėl |
|------------|--------|-------|
| Namo savininkas | +15 | Nuosavybė = gali įsirengti |
| Gyvena >3 metus | +10 | Stabilumas, ilgalaikė vertė |
| Elektros sąskaita >€100/mėn | +15 | Aiškus taupymo potencialas |
| Elektros sąskaita €50-100/mėn | +8 | Vidutinis potencialas |
| Amžius 35-65 | +10 | Sprendimų priėmėjai |

### Elgesio Signalai (40 taškų max)

| Kriterijus | Taškai | Kodėl |
|------------|--------|-------|
| Užpildė formą per 24h | +15 | Aukštas interesas |
| Atsakė į pirmą žinutę | +15 | Įsitraukęs |
| Paklausė apie kainą | +10 | Pirkimo signalas |
| Nurodė konkretų adresą | +10 | Rimtas ketinimas |
| Atsisiuntė PDF/infopaketą | +8 | Dėmesys detalėms |
| Aplankė svetainę 2+ kartus | +7 | Tyrinėja opcijas |

### Būsenos Indikatoriai (30 taškų max)

| Kriterijus | Taškai | Kodėl |
|------------|--------|-------|
| "Skubu / Reikia greitai" | +15 | Skubumo faktorius |
| Paminėjo konkurentą | +12 | Aktyviai lygina |
| Klausė apie finansavimą | +10 | Pirkimo pasirengimas |
| Nurodė telefoną (ne tik email) | +8 | Pasiekiamas |
| Referral iš esamo kliento | +20 | 🌟 Aukščiausias signalas |

### Dedukcijos (minus taškai)

| Kriterijus | Taškai | Kodėl |
|------------|--------|-------|
| Nuomininkas / Butas | -20 | Neįmanoma įsirengti |
| "Tik domiuosi" | -10 | Žemas interesas |
| Neatsako 72h+ | -15 | Šąla |
| Elektros sąkaita <€30 | -15 | Nėra ROI |
| Atmetė 2+ kartus | -25 | Neįdomu |

---

## 🚦 Prioriteto Kategorijos

### 🔥 HOT (80-100 taškų)
**Veiksmas:** Skambinti PER 1 VALANDĄ

**Požymiai:**
- Namo savininkas + aukšta sąskaita + skubu
- Referral iš kliento
- Klausia apie kainą IR finansavimą

**Scriptas:**
> "Labas [Vardas], aš [Tavo vardas] iš Akseler. Gavau jūsų užklausą apie saulės elektrines. Matau, kad sąskaitos yra ~€XXX - ar turite 5 minučių dabar sukalbėti apie potencialų taupymą?"

### ⚡ WARM (50-79 taškų)
**Veiksmas:** Skambinti ŠIANDIEN

**Požymiai:**
- Namo savininkas + vidutinė sąskaita
- Atsakė į žinutę bet nežada skubėti
- Klausia informacijos, lygina variantus

**Scriptas:**
> "Sveiki [Vardas], dėkoju už susidomėjimą. Noriu suprasti jūsų situaciją geriau - koks jūsų pagrindinis tikslas: sumažinti sąskaitas ar energetinis savarankiškumas?"

### ❄️ COLD (20-49 taškų)
**Veiksmas:** Įtraukti į nurture seką (email/WhatsApp)

**Požymiai:**
- "Tik domiuosi"
- Maža sąskaita
- Neatsako į pirmą kontaktą

**Veiksmas:**
- Siųsti edukacinį turinį
- Priminti po savaitės
- Nešvaistyti laiko skambučiams kol neužkais

### 🗑️ DISQUALIFIED (0-19 taškų)
**Veiksmas:** Archyvuoti su žyme "Netinkamas"

**Požymiai:**
- Nuomininkas / bute gyvena
- Atmetė kelis kartus
- Neįmanomas adresas

**Nedarome:** Nešiukšlinti laiko veltui.

---

## 🎮 Rapid Scoring Tool

Naudok šitą pokalbiuose (sukopijuok į notes):

```
┌─────────────────────────────────────┐
│  AKSELER LEAD SCORE (30 sek.)       │
├─────────────────────────────────────┤
│ □ Savininkas (+15)    □ >€100 (+15) │
│ □ >3 metų (+10)       □ 35-65m (+10)│
│ □ Forma 24h (+15)     □ Atsakė (+15)│
│ □ Kaina? (+10)        □ Adresas (+10)│
│ □ Skubu? (+15)        □ Referral (+20)│
│                                     │
│ □ Butas (-20)         □ Šąla (-15)  │
│ □ Tik domisi (-10)    □ <€30 (-15)  │
├─────────────────────────────────────┤
│ REZULTATAS: ___/100 = 🔥/⚡/❄️/🗑️   │
└─────────────────────────────────────┘
```

---

## 📱 GHL Automation Setup

### 1. Custom Fields Sukūrimas

Eiti į: Settings → Custom Fields → Add Field

| Field Name | Type | Values |
|------------|------|--------|
| `lead_score` | Number | 0-100 |
| `lead_category` | Text | HOT / WARM / COLD / DISQUALIFIED |
| `homeowner` | Text | Yes / No / Unknown |
| `monthly_bill` | Number | € amount |
| `urgency_level` | Text | High / Medium / Low |

### 2. Scoring Workflow

**Trigger:** New Lead Created

**Actions:**
1. Wait 5 minutes (kad užpildytų formą)
2. Calculate `lead_score` pagal formos laukus
3. Set `lead_category` pagal score:
   - 80-100 → HOT
   - 50-79 → WARM
   - 20-49 → COLD
   - 0-19 → DISQUALIFIED
4. Add tag: `lead-score-calculated`

**HOT Lead Path:**
- Assign to CEO (you)
- Send Slack/SMS notification: "🔥 HOT Lead: [Name] - [Phone]"
- Create task: "Skambinti per 1 valandą"
- Add tag: `priority-hot`

**WARM Lead Path:**
- Assign to CEO
- Create task: "Skambinti šiandien"
- Add tag: `priority-warm`

**COLD Lead Path:**
- Enroll in nurture campaign
- Task: "Įtraukti į email seką"
- Tag: `nurture-sequence`

### 3. Score Update Workflow

**Trigger:** Lead Activity (reply, page visit, etc.)

**Actions:**
1. Recalculate score
2. If score increases by 20+ points:
   - Upgrade category
   - Send notification: "⚡ Lead [Name] įšilo! Naujas score: [X]"
   - Create follow-up task

---

## 📊 Savaitės Prioriteto Ritualas (5 min)

**Kada:** Pirmadienis 9:00 AM

### Checklist:
```
□ Atidaryti GHL → Contacts → Filter by "HOT"
□ Peržiūrėti kiekvieną HOT leadą - ar yra užduotys?
□ Patikrinti WARM leads - kas gali tapti HOT šią savaitę?
□ Peržiūrėti COLD nurture sekos statistiką
□ Ar kas nors atšilo? (score padidėjo)
□ Ar reikia kviesti komandos narį padėti?
```

---

## 🎯 Realūs Pavyzdžiai

### Pavyzdys 1: 🔥 HOT Lead
**Duomenys:**
- Jonas, 45m, namo savininkas (+15)
- Elektros sąskaita €150/mėn (+15)
- Užpildė formą vakar (+15)
- Paklausė "Kiek kainuoja?" (+10)
- Nurodė adresą Kaune (+10)
- Telefonas pateiktas (+8)

**Score:** 15+15+15+10+10+8 = **73 → WARM** (beveik HOT!)

**Veiksmas:** Skambinti šiandien, pasiūlyti nemokamą auditą.

---

### Pavyzdys 2: 🔥 HOT Lead (su referral)
**Duomenys:**
- Petras, 52m, namo savininkas (+15)
- Elektros sąskaita €120/mėn (+15)
- Užpildė formą šiandien (+15)
- "Skubu, vasarą noriu turėti" (+15)
- Referral iš Jono (+20)

**Score:** 15+15+15+15+20 = **80 → HOT**

**Veiksmas:** Skambinti PER VALANDĄ. Paminėti Jono rekomendaciją!

---

### Pavyzdys 3: ❄️ COLD Lead
**Duomenys:**
- Ona, 28m, bute gyvena (-20)
- Elektros sąskaita €35/mėn (-15)
- "Tik domiuosi" (-10)

**Score:** -45 → **DISQUALIFIED**

**Veiksmas:** Archyvuoti. Galima siųsti bendrą info, bet nešvaistyti laiko.

---

## 🔧 GHL + Newo Integracija

Kai Newo voice agent užbaigia pokalbį:

### Data Flow:
```
Newo Voice Call
       ↓
[Extract scoring data]
       ↓
GHL API Update:
- homeowner: "Yes/No"
- monthly_bill: €XX
- urgency_level: "High/Medium/Low"
- notes: "AI analizė..."
       ↓
Auto-recalculate score
       ↓
Re-categorize if needed
       ↓
Notify CEO if upgraded to HOT
```

### Newo Scoring Questions:
Voice agent gali užduoti:
- "Ar esate namo savininkas?"
- "Kokia jūsų vidutinė mėnesio elektros sąskaita?"
- "Ar planuojate įsirengti artimiausius 3-6 mėnesius?"
- "Ar buvote rekomenduoti?"

Atsakymai automatiškai atnaujina GHL score.

---

## 📈 KPIs sekti

Savaitės metrikos:

| Metrika | Tikslas | Kaip matuoti |
|---------|---------|--------------|
| HOT leads / savaitę | 5-10 | GHL contacts with `priority-hot` tag |
| HOT → susitikimas | >60% | Meetings booked from HOT leads |
| WARM → HOT conversion | >20% | Score increases 50→80+ |
| Atsakymo laikas (HOT) | <2h | Task completion time |
| Nurture atšilimas | >10% | COLD → WARM per mėnesį |

---

## ⚡ Greita Pradžia (Next 24h)

### Šiandien (10 min):
1. Sukurti custom fields GHL (žr. aukščiau)
2. Nukopijuoti scoring tool į telefono notes
3. Peržiūrėti esamus leads - rankiniu būdu priskirti kategorijas

### Rytoj (15 min):
1. Sukurti scoring workflow GHL
2. Testuoti su vienu nauju leadu
3. Sudėti HOT leads į kalendorį

### Savaitgalis (10 min):
1. Peržiūrėti savaitės rezultatus
2. Pakoreguoti kriterijus jei reikia
3. Planuoti kitą savaitę

---

## 🎁 Bonus: "Lead Temperature" Daily Report

GHL Automation kurti kasdien 8:00 AM:

**Email Subject:** "🌡️ Lead Temperatūra - [Data]"

**Content:**
```
Labas,

Šiandienos leadų suvestinė:

🔥 HOT (skambinti per 1h): [X]
   → [Vardas1] [Telefonas]
   → [Vardas2] [Telefonas]

⚡ WARM (skambinti šiandien): [Y]
   → [Vardas3] [Telefonas]

❄️ COLD (nurture sekoje): [Z]

📊 Savaitės HOT leadų konversija: [XX]%

Juodčkis 🐾
```

---

## TL;DR (Jeigu tik viena mintis)

> **Namo savininkas + didelė sąskaita + skubumas = skambinti DABAR. Visa kita = pagal eilę.**

Naudok scoring tool, automatizuok GHL, fokusuok laiką į HOT leads.

---

*Sukurta: 2026-02-10*
*Versija: ADHD-friendly (v1.0)*
