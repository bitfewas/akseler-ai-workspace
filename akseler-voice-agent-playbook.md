# Akseler Voice Agent Playbook
## 🎙️ Saulės Energijos Voice Agent Žaidimo Vadovas

**Versija:** 1.0  
**Sukurta:** 2026-02-10  
**Paskirtis:** Detalus voice agent naudojimas Akseler lead generavimui

---

## 📋 Turinys

1. [Voice Agent Principai](#principai)
2. [Skriptų Biblioteka](#skriptai)
3. [Objection Handling](#objections)
4. [Scenarijų Flow](#scenarijai)
5. [Quality Checklist](#quality)

---

<a name="principai"></a>
## 🎯 Voice Agent Principai

### Voice vs Text Diferenciacija

| Aspektas | Voice | Text (SMS/WhatsApp) |
|----------|-------|---------------------|
| **Greitis** | 130-150 WPM | Skaitymo tempas |
| **Ilgis** | Max 30 žodžių | Max 160 simbolių |
| **Tonas** | Šiltas, energingas | Profesionalus, tiesus |
| **Pauzės** | 0.5-1s tarp sakinių | N/A |
| **Pakartojimai** | Svarbūs dalykai 2x | Vieną kartą |

### Newo Pattern'ai Voice Kontekste

```
✅ Atomic Voice Blocks
   - Vienas blokas = viena mintis
   - Max 2 sakiniai
   - Aiški pabaiga (laukiu atsakymo)

✅ Dual Runner Architecture
   - Runner 1: Klausymas + intent nustatymas
   - Runner 2: Atsakymo generavimas
   - Context sharing tarp jų

✅ Voice Buffering
   - Realtime transcription
   - 0.5s silence = end of turn
   - Interrupt handling
```

---

<a name="skriptai"></a>
## 📝 Skriptų Biblioteka

### 1. Pradinis Skambutis (Cold Call)

```
TRUKMĖ: 45-60 sekundžių
Tikslas: Sudominti + gauti susitikimą
```

**Skriptas:**

```
"Labas [Vardas], čia Akseler. 
Skambinu dėl jūsų namo [Adresas].

Pastebėjau, kad saulės elektrinė 
galėtų jums sutaupyti apie 
[XX] eurų per metus.

Ar turėtumėte 2 minutes 
pasikalbėti?"
```

**Fallback (jei neužfiksuoja vardo):**

```
"Labas, čia Akseler. 
Skambinu dėl saulės energijos 
jūsų name [Adresas].

Ar tai geras metas pasikalbėti 
2 minutes?"
```

---

### 2. Warm Lead (Gauta užklausa)

```
TRUKMĖ: 3-5 minutės
Tikslas: Kvalifikuoti + užrezervuoti laiką
```

**Skriptas:**

```
"Labas [Vardas], čia Akseler. 
Ačiū už susidomėjimą saulės energija.

Iš karto pasakysiu - 
kad padaryčiau jums pasiūlymą,
man reikia kelių detalių.

Pirmiausia - kokia jūsų 
saskaitos už elektrą 
vidutiniškai per mėnesį?"
```

**Po atsakymo:**

```
"Puiku. Tai reiškia, kad 
sistema apie [X] kW 
būtų optimali.

Atsipirkimas - maždaug 
[Y] metų. Po to - 
tik santaupos.

Gal galėtume susitikti 
ketvirtadienį ar penktadienį?
Turiu laisvų vietų 
14:00 arba 16:00."
```

---

### 3. Follow-up (Po pasiūlymo)

```
TRUKMĖ: 2-3 minutės
Tikslas: Uždaryti dealą
```

**Skriptas:**

```
"Labas [Vardas], čia Akseler.
Skambinu dėl saulės projekto.

Ar turėjote laiko 
peržiūrėti pasiūlymą?

[LAUKTI ATSAKYMO]

[JEI TAIP]
"Ką manote? Ar liko 
klausimų apie įrangą 
finansavimą?"

[JEI NE]
"Suprantu, visko daug. 
Trumpai - esmė tokia:
įsirengiate už [X] EUR,
sutaupote [Y] EUR per metus.
Atsipirkimas [Z] metai.

Ar galėčiau atsakyti 
į kokį nors klausimą dabar?"
```

---

### 4. Objection - "Brangu"

```
TRUKMĖ: 1-2 minutės
Tikslas: Reframe į investiciją
```

**Skriptas:**

```
"Suprantu, [X] EUR 
nemenka suma.

Bet pažiūrėkime kitaip.

Dabar mokate 
[Y] EUR/mėn už elektrą.

Su saulės sistema 
mokėtumėte apie 
[Z] EUR/mėn.

Skirtumas - [W] EUR 
į jūsų kišenę kiekvieną mėnesį.

Tai ne išlaidos. 
Tai investicija į mažesnes sąskaitas.

Be to, turime 
[finansavimo pasirinkimą].
Ar apie jį kalbėjome?"
```

---

### 5. Objection - "Paskui pagalvosiu"

```
TRUKMĖ: 1-2 minutės
Tikslas: Urgency be spaudimo
```

**Skriptas:**

```
"Žinoma, apsvarstyti 
verta.

Tik pasakysiu - 
dabar saulės modulių kainos 
krito 30% per metus.

Bet kompensacijos iš 
valstybės mažėja.

Šiemet dar galite 
gauti [X] EUR paramą.
Kitąmet - gal mažiau.

Nesiūlau skubėti be 
galvos. Siūlau tiesiog 
susitikti, aptarti.

Jei ne dabar - 
kitą savaitę. Bet 
kompensacija lieka 
šiam etapui.

Ką manote?"
```

---

### 6. Appointment Confirmation

```
TRUKMĖ: 30-45 sekundės
Tikslas: Patvirtinti susitikimą
```

**Skriptas:**

```
"Labas [Vardas], čia Akseler.
Skambinu patvirtinti rytojaus 
susitikimą [Laikas].

Adresas teisingas: [Adresas]?

Puiku. Mūsų specialistas 
[Name] atvyks su 
skaičiuokle ir pavyzdžiais.

Trukmė - apie 30 minučių.

Ar reikia pakeisti laiką?"
```

---

<a name="objections"></a>
## 🛡️ Objection Handling Framework

### 1. L.E.A.R.N. Metodas

```
L - Listen (Išklausyti)
E - Empathize (Empatija)
A - Ask (Klausti)
R - Reframe (Pertvarkyti)
N - Next step (Kitas žingsnis)
```

**Pavyzdys:**

```
Klientas: "Brangu"

L: [Išklausyti visą]
E: "Suprantu, [X] EUR rimta suma"
A: "Ar galvojote apie 
   mėnesines sąnaudas 
   elektrai?"
R: "Tai ne išlaidos, 
   o investicija į mažesnes 
   sąskaitas"
N: "Gal susitinkame, 
   apskaičiuoju tiksliau?"
```

### 2. Dažniausios Objections

| Objection | Atsakymo esmė |
|-----------|---------------|
| "Brangu" | Investicija, ne išlaidos. ROI parodyti. |
| "Reikia pagalvoti" | Urgency (kompensacijos), bet be spaudimo |
| "Ne laikas" | Kai geriau? Įrašyti follow-up. |
| "Nedirbame su telemarketingu" | "Suprantu. Tai ne pardavimas telefonu - o informacija. Jei nedomina, 10 sekundžių ir baigiam." |
| "Jau turime pasiūlymą" | „Puiku! Gal galiu pasakyti, kuo mes kitokie? Tada palyginsite.“ |
| "Namas ne mūsų" | „Ar nuomojate? Gal žinote savininką?“ |

---

<a name="scenarijai"></a>
## 🎬 Scenarijų Flow

### Scenarijus A: Sėkmingas Call → Susitikimas

```
1. GREETING (5s)
   → Labas + prisistatymas + priežastis

2. PERMISSION (5s)
   → „Ar geras metas?"

3. VALUE PROP (15s)
   → Sutaupymai + atsipirkimas

4. QUALIFY (30s)
   → Sąskaitos dydis → sistemos dydis

5. CLOSE (15s)
   → „Gal susitinkame [diena] [laikas]?"

6. BOOK (10s)
   → Patvirtinti adresą + kontaktą

7. CLOSE (5s)
   → Padėkoti + priminti
```

### Scenarijus B: Objection Handling

```
1. HEAR (5s)
   → Leisti pasakyti visą objection

2. ACKNOWLEDGE (3s)
   → „Suprantu..."

3. QUESTION (10s)
   → „Ar galvojote apie...?"

4. REFRAME (15s)
   → Pertvarkyti perspektyvą

5. ASK AGAIN (10s)
   → Pakartoti close

6. IF NO → BOOK FOLLOW-UP
```

### Scenarijus C: No Answer → Voicemail

```
„Labas, čia [Vardas] iš Akseler.
Skambinu dėl saulės elektrinės
jūsų name [Adresas].

Turėjau pasiūlymą, kuris galėtų
jums sutaupyti [X] EUR per metus.

Galite man paskambinti
[tel. numeris] arba
parašyti „SAULĖ“ į šį numerį
ir aš paskambinsiu.

Ačiū, iki!"

TRUKMĖ: 20-25 sekundės
```

---

<a name="quality"></a>
## ✅ Quality Checklist

### Prieš Skambutį

- [ ] Lead info peržiūrėta (vardas, adresas, šaltinis)
- [ ] Preliminarus skaičiavimas paruoštas
- [ ] Kalendorius atidarytas
- [ ] Skriptas akiratyje (neatsiversti!)

### Skambučio Metu

- [ ] Įvardintas klientas per 3 sekundes
- [ ] Pasakyta priežastis per 10 sekundžių
- [ ] Paklausta permission (ar geras metas)
- [ ] Value prop per 20 sekundžių
- [ ] Klausimai užduoti (qualify)
- [ ] Close bandytas (ask for appointment)
- [ ] Įrašytas rezultatas

### Po Skambučio

- [ ] Rezultatas užfiksuotas (booked/no answer/not interested)
- [ ] Jei booked → siųsti confirmation SMS
- [ ] Jei no answer → suplanuoti follow-up
- [ ] Jei not interested → pažymėti reason
- [ ] Update GHL

---

## 📊 Voice Agent Metrics

### Sekti Kasdien

| Metrika | Target | Kaip matuoti |
|---------|--------|--------------|
| **Pick-up rate** | >30% | Atsiliepę / Iš viso skambučių |
| **Qualification rate** | >40% | Kvalifikuoti / Atsiliepę |
| **Booking rate** | >20% | Susitikimai / Atsiliepę |
| **Avg call duration** | 2-4 min | Geras balansas |
| **Objection handling** | >60% | Pavyko įveikti / Bandyti |

### Weekly Review

- Top 3 objections (kas dažniausiai)
- Top 3 veikiantys skriptai
- Conversion by lead source
- A/B test results

---

## 🔧 Voice Agent Settings

### Newo Konfigūracija

```yaml
voice_settings:
  speed: 1.0  # Normal speed
  pitch: 0    # Natural
  volume: 100
  
interruption_handling:
  enabled: true
  sensitivity: medium
  
pauses:
  between_sentences: 0.5s
  after_question: 1.0s
  
languages:
  primary: lt
  fallback: en
```

---

## 📚 Papildomi Resursai

- `ghl-cheatsheet.md` - GHL komandos
- `newo-patterns-practical-guide.md` - Architektūros pattern'ai
- `akseler-complete-integration-plan.md` - Pilnas diegimo planas

---

**Paskutinis atnaujinimas:** 2026-02-10 07:36 AM  
**Sekantis žingsnis:** Testuoti skriptus realiuose skambučiuose
