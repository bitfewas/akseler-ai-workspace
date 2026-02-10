# HEARTBEAT.md - Autonominis Darbas

**Sistema aktyvuota:** Automatiškai dirbu kas 15 minučių be papildomų nurodymų.

---

## 🚨 Kritiniai (kiekvienas heartbeat)

- [ ] Patikrinti ar yra naujų žinučių nuo CEO
- [ ] Jei yra - atsakyti per 30 sekundžių
- [ ] Jei ne - tęsti autonominį darbą

---

## 🔄 Pagrindinis Darbas (kas 15 min)

### Žingsniai:
1. **Skaityti PULSE.md** - ką dariau anksčiau
2. **Mesti kauliuką** - pasirinkti režimą (00-99)
3. **Atlikti darbą** - pagal režimą
4. **Išsaugoti rezultatą** - į failą
5. **Atnaujinti PULSE.md** - užfiksuoti progresą
6. **Pranešti CEO** - jei verta dėmesio (≤3 eilutės)

---

## 🎯 Darbo Režimai (pagal kauliuką)

| Kauliukas | Režimas | Ką darau |
|-----------|---------|----------|
| 00-19 | 🚀 Didelis žingsnis | Radikaliai naujas požiūris į Newo/Newo analizę |
| 20-39 | 🎲 Atsitiktinis gilusis | Ištirti naują įrankį/koncepciją iš clawhub.com |
| 40-59 | 🏃 Relay tęsimas | Tęsti Newo file analizę (einamasis: 33/133) |
| 60-79 | 📈 Badaujantis tikslas | GHL optimizacija (dar nepradėta) |
| 80-99 | 🎁 Staigmena CEO | Sukurti ką nors naudingo ko nesitiki |

---

## 📊 Progreso Sekimas

**Newo Analizė:**
- Progress: 33/133 file'ų (24.81%)
- Sekantis: CAMainFlow likę skillai
- Rasta: Automation sistema (LFUTriggerFlow, OCWCallDispatcher)

**GHL Optimizacija:**
- Status: Laukia pradžios
- Galimybės: Voice agentai, automatizavimas

---

## 🛡️ Saugos Taisyklės

- Nesiųsti pranešimų 23:00-08:00
- Vienas pranešimas ≤3 eilutės
- Jei CEO rašo - nutraukti autonominį darbą ir atsakyti

---

## Cron Nustatymai

```json
{
  "schedule": "every 15 minutes",
  "action": "run goal-heartbeat engine",
  "target": "autonomous work"
}
```
