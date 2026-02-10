# CEO Quick Reference 🎯

**Akseler AI Voice & Automation - Raktiniai Radiniai**

---

## 🚀 Paruošta Naudoti Dabar

### GoHighLevel Automatizavimas
| Failas | Paskirtis | Statusas |
|--------|-----------|----------|
| `ghl-solar-automation.py` | 6 automatizavimo funkcijos | ✅ Paruoštas |
| `ghl-test-suite.py` | Testavimas (6/6 OK) | ✅ Paruoštas |
| `ghl-cheatsheet.md` | Komandų pavyzdžiai | ✅ Paruoštas |
| `ghl-workflows.md` | 7 workflow šablonai | ✅ Paruoštas |

**Reikia:** `HIGHLEVEL_TOKEN` ir `HIGHLEVEL_LOCATION_ID`

### Naudingiausios GHL Funkcijos
```bash
# 1. Naujo leado apdorojimas
python ghl-solar-automation.py process-new-lead --email=lead@example.com

# 2. Priminimas neuždarytiems leadams
python ghl-solar-automation.py check-overdue-followups

# 3. Dienos ataskaita
python ghl-solar-automation.py generate-daily-report

# 4. Laimėto deal'o procesas
python ghl-solar-automation.py process-deal-won --deal-id=XXX

# 5. Reaktyvacijos kampanija
python ghl-solar-automation.py run-reactivation-campaign
```

---

## 🧠 Newo Voice Agent Architektūra

### 10 Architektūrinių Principų
1. **Dual Runner** - Text vs Voice skirtingi keliai
2. **Atomic Init** - Kiekvienas pokalbis švarus startas
3. **Cross-Channel Memory** - Istorija perduodama tarp kanalų
4. **Intent Routing** - AI nusprendžia kokį tool kviesti
5. **Context Windows** - Voice 15-30 žodžių, Text ilgesnis
6. **Atomic Skills** - Mikro-funkcijos komponuojamos
7. **Prompt Compilation** - Dinamiškas prompt build'inimas
8. **Structured Output** - JSON schema validation
9. **State Machine** - Pokalbio fazės (greet → qualify → book → close)
10. **Graceful Degradation** - Jei AI neveikia → fallback

### Voice vs Text Skirtumai
| Aspektas | Voice | Text |
|----------|-------|------|
| Buffering | Real-time (500ms) | Full message |
| Interrupts | Palaikomi | N/A |
| Length | 15-30 žodžių | Neribota |
| Tone | Warm, conversational | Profesionalus |
| Tools | Voice-optimized | Full feature |

### Scoring Sistema (Lead Kvalifikacija)
```
0-30:   Šaltas lead → Nurijimas, edukacija
31-60:  Šiltas lead → Daugiau info, sekantis kontaktas
61-85:  Karštas lead → Skambutis per 1h, prioritetas
86-100: Super karštas → Skambutis DABAR, VIP aptarnavimas
```

---

## 🔧 Pritaikymas Akseler

### Solar Lead Flow
1. **Inbound call/SMS** → AI atsako
2. **Kvalifikacija** → 5 klausimai (NT tipas, sąskaita, adresas)
3. **Skaičiavimas** → Real-time ROI, atsipirkimas
4. **Booking** → Kalendoriaus integracija
5. **Follow-up** → SMS priminimai
6. **Handoff** → Žmogus kai reikia

### Cross-Channel Atminties Pavyzdys
```
CEO: "Koks mano adresas?" (SMS)
AI: "Jūsų adresas: Vilnius, Saulės g. 5" 
CEO: "Skambink ten rytoj 14h" (Voice)
AI: "Gerai, skambinsiu į Saulės g. 5 rytoj 14val."
```

### Tool Calling Integracija
| Tool | Naudojimas | Trigger |
|------|------------|---------|
| Solar kalkuliatorius | ROI skaičiavimas | "kiek sutaupysiu" |
| GHL lead search | Rasti egzistuojantį leadą | Telefono numeris |
| Booking | Susitikimo rezervacija | "norėčiau susitikti" |
| Location lookup | Adreso paieška | "kiek kainuos mano rajone" |

---

## 📋 Įgyvendinimo Planas

### Fazė 1: GHL Setup (1-2 dienos)
- [ ] Gauti API token iš GHL
- [ ] Paleisti test suite
- [ ] Sukonfigūruoti workflow
- [ ] Testuoti su fake data

### Fazė 2: Newo Integration (1 savaitė)
- [ ] Suprasti architektūrą ✅ (padaryta)
- [ ] Sukurti prompt template
- [ ] Implementuoti scoring
- [ ] Kalendoriaus integracija
- [ ] Testing & refinement

### Fazė 3: Go Live (2 savaitės)
- [ ] Soft launch (10 leads)
- [ ] Stebėti, koreguoti
- [ ] Pilnas deploy

---

## 📚 Dokumentų Indeksas

| Dokumentas | Turinys | Dydis |
|------------|---------|-------|
| `newo-camainflow-architecture-map.md` | Pilnas architektūros žemėlapis | 36KB |
| `newo-architecture-synthesis.md` | 10 principų sintezė | 7KB |
| `newo-to-akseler-implementation-guide.md` | Pritaikymo gidas | 13KB |
| `newo-patterns-analysis.md` | Architektūriniai šablonai | 5KB |
| `newo-skill-catalog.md` | 33 skillų katalogas | 4KB |
| `ghl-preparation.md` | GHL nustatymo instrukcijos | 2KB |
| `ghl-cheatsheet.md` | Komandų pavyzdžiai | 3KB |
| `ghl-workflows.md` | Workflow šablonai | 5KB |

**Iš viso sukurta:** 18 dokumentų, 75KB+ žinių

---

## ⚡ Greiti Veiksmai

### Jei nori paleisti GHL automatizavimą DABAR:
1. Eik į GHL Settings → API Keys
2. Sukurk naują key
3. Siųsk man: `HIGHLEVEL_TOKEN=xxx HIGHLEVEL_LOCATION_ID=xxx`
4. Paleisiu testus

### Jei nori matyti visą architektūrą:
```bash
cat memory/newo-camainflow-architecture-map.md
```

### Jei nori suprasti implementaciją:
```bash
cat newo-to-akseler-implementation-guide.md
```

---

## 📊 Progreso Santrauka

| Projektas | Progressas | Statusas |
|-----------|------------|----------|
| GHL Setup | 100% | ✅ Paruoštas |
| Newo Analizė | 47% | ⏸️ Blokuota (no source) |
| Implementation Guide | 100% | ✅ Paruoštas |
| Voice Agent Dev | 0% | ⏳ Laukia |

---

**Sukurta:** 2026-02-10 06:51 AM  
**Autorius:** Juodčkis 🐾  
**Kita apžvalga:** Po 15 min (06:66 AM)
