# CAMainFlow Skill Analysis

## Apžvalga

**CAMainFlow** yra pagrindinis Newo pokalbių agento (ConvoAgent) flow, valdantis visą vartotojo pokalbio gyvavimo ciklą. Flow apibrėžtas YAML faile (`CAMainFlow.yaml`), o logika įgyvendinta skill'uose dviejų tipų failuose: `.nsl` ir `.nslg`.

---

## Architektūros Supratimas

### Flow Struktūra

```
CAMainFlow/
├── CAMainFlow.yaml          # Flow aprašas - skill registracija
└── skills/
    ├── *.nsl                # NSL (NScript Language) template'ai
    └── *.nslg               # Guidance template'ai
```

### Skill Registracija (YAML)

Kiekvienas skill registruojamas su šiais parametrais:

```yaml
skills:
  - title: ""                      # Opcionalus pavadinimas
    idn: SkillName                 # Unikalus skill identifikatorius
    prompt_script: path/to/file    # Kelias į skill failą
    runner_type: guidance|nsl      # Vykdymo variklis
    model:
      model_idn: gemini25_flash    # Naudojamas modelis
      provider_idn: google         # Modelio tiekėjas
    parameters:                    # Skill parametrų apibrėžimas
      - name: paramName
        default_value: ""
```

### Runner Tipai

| Runner | Aprašymas | Naudojimas |
|--------|-----------|------------|
| `guidance` | Turi `{{StartNotInterruptibleBlock()}}` ir `{{StopNotInterruptibleBlock()}}` | Kai reikia užtikrinti atominį vykdymą |
| `nsl` | Paprastesnis Jinja2-style template | Kai nereikia specialių guidance funkcijų |

---

## Sintaksės Pattern'ai

### 1. Kintamųjų Nustatymas

**NSL stilius (Jinja2):**
```nsl
{% set user_id = user_id or GetUser().id | string %}
{% set conversation_channel = session_get_conversation_channel(integration_idn=integration_idn, user_id=user_id) %}
```

**Guidance stilius (Mustache-like):**
```nslg
{{Set(name="user_id", value=GetUser(field="id"))}}
{{Set(name="time_zone", value=_getTimeZoneSkill(userId=userId))}}
```

### 2. Sąlygos (Conditionals)

**NSL:**
```nsl
{% if not last_convo_actor_id.strip() %}
    {{Return(val="")}}
{% endif %}

{% if base_instruction.strip() %}
    {% set fast_prompt = prompt_fast_compile(...) %}
{% else %}
    {% set fast_prompt = GetState(name="fast_prompt") %}
{% endif %}
```

**Guidance:**
```nslg
{{#if IsEmpty(text=userId)}}
  {{Set(name="userId", value=GetUser(field="id"))}}
{{/if}}

{{#if pm_prefix_should_be_set != 0}}
    {{Set(name="postfix", value="PM")}}
{{/if}}

{{#if not IsEmpty(text=common_phone_numbers)}}
    {{!-- kodas --}}
{{/if}}
```

### 3. Funkcijų/Funkcinių Kvietimų Šablonai

**Built-in funkcijos:**
```nslg
{{GetUser(field="id")}}
{{GetActor(field="externalId")}}
{{GetCustomerAttribute(field="project_business_time_zone")}}
{{GetPersonaAttribute(id=user_id, field="working_hours_status")}}
{{GetState(name="user_reply_buffer")}}
{{GetDatetime(format="time", timezone=time_zone, weekday=False)}}
{{IsEmpty(text=variable)}}
{{IsSimilar(val1=value1, val2="null", threshold=0.8)}}
{{Concat(string1, string2, ...)}}
{{Stringify(value)}}
```

**Skill kvietimai (kaip funkcijos):**
```nslg
{{_getTimeZoneSkill(userId=userId)}}
{{_utilsCreatePhoneActorsSkill(userId=user_id, phoneNumber=detected_phone_number_with_country_code)}}
{{_userMessageFastReplySkill(
  callAnalyzeConversationSkill="True",
  callManageTaskSkill="True",
  userId=user_id,
  integrationIdn=integration_idn
)}}
```

### 4. Sistemos Įvykių Siuntimas

```nslg
{{SendSystemEvent(eventIdn="extend_session", connectorIdn="system")}}

{{SendSystemEvent(
    eventIdn="prepare_rag_context_command",
    connectorIdn="system"
)}}

{{SendSystemEvent(
    eventIdn="urgent_message",
    connectorIdn="system",
    baseInstruction=message,
    uninterruptible="True"
)}}
```

### 5. State/Attribute Nustatymas

```nslg
{{SetState(name="user_reply_buffer", value=" ")}}
{{SetState(name="fast_prompt", value=" ")}}

{{SetPersonaAttribute(id=user_id, field="working_hours_status", value=" ")}}
{{SetPersonaAttribute(id=user_id, field="current_integration_idn", value=" ")}}

{{SetCustomerAttribute(field="project_attributes_setting_voice_integration_service", value="VAPI Integration")}}
```

### 6. Sistemos Prompt'as (Guidance)

```nslg
{{#system~}}
conversation.timezone: {{time_zone}}
conversation.channel: {{conversation_channel}}
conversation.day_of_week: {{current_week_day}}
conversation.time: {{current_hour}}:{{current_minute}}:{{current_second}}

{{working_hours_status}}
{{~/system}}
```

---

## Pagrindiniai Koncepcijų Pattern'ai

### 1. Nepertraukiamo Bloko Pattern

Naudojamas kai reikia užtikrinti, kad skill būtų įvykdytas visas be pertraukimų:

```nslg
{{StartNotInterruptibleBlock()}}

{{!-- visa logika čia --}}

{{StopNotInterruptibleBlock()}}
```

### 2. Early Return Pattern

```nslg
{{#if GetCustomerAttribute(field="some_setting") != "True"}}
    {{Return()}}
{{/if}}
```

```nsl
{% if not last_convo_actor_id.strip() %}
    {{Return(val="")}}
{% endif %}
```

### 3. JSON Duomenų Apdorojimas

```nslg
{{Set(name="current_hour_list", value=current_time.split(":"))}}
{{Set(name="current_hour_list", value=Stringify(current_hour_list))}}
{{Set(name="current_hour_list", value=current_hour_list.replace("'", '"'))}}
{{Set(name="current_hour", value=Stringify(GetItemsArrayByIndexesJSON(array=current_hour_list, indexes=0)))}}
{{Set(name="day_object", value=GetValueJSON(obj=working_hours_object, key=current_week_day))}}
```

### 4. Placeholder Pakeitimo Pattern

```nsl
{% set fast_prompt = fast_prompt.replace("<||last_user_message||>", GetState(name="user_reply_buffer")) %}
{% set fast_prompt = fast_prompt.replace("<||rag_placeholder||>", GetPersonaAttribute(id=user_id, field="rag")) %}
{% set cleaned_prompt = re.sub("<\|\|.*?\|\|>", "", fast_prompt.strip()) %}
```

### 5. Feature Flag Pattern

```nsl
{% if _utilsFeatureFlagIsActiveSkill(featureFlagName="multi_location") %}
    {{SetPersonaAttribute(id=user_id, field="multi_location_current_location", value="default")}}
{% endif %}
```

### 6. Temporal Session (Laikina Sesija) Pattern

Naudojamas telefonijos atvejais kai vyksta aktyvus pokalbis:

```nslg
{{Set(name="temporal_session_is_active", value=GetPersonaAttribute(id=user_id, field="temporal_session_is_active"))}}
{{#if temporal_session_is_active == "True"}}
    {{!-- Forward message to active call --}}
    {{Set(name="temporal_convo_actor_id", value=GetPersonaAttribute(id=user_id, field="temporal_convo_actor_id"))}}
    {{SendSystemEvent(...)}}}
    {{Return()}}
{{/if}}
```

---

## Duomenų Prieiga - Funkcijų Katalogas

### Vartotojo Duomenys

| Funkcija | Aprašymas |
|----------|-----------|
| `GetUser(field="id")` | Gauti vartotojo ID |
| `GetActor(field="externalId")` | Išorinis actor ID (pvz. tel. nr.) |
| `GetActor(field="integrationIdn")` | Integracijos identifikatorius |
| `GetActor(field="name")` | Actor pavadinimas |

### Customer/Projekto Nustatymai

| Funkcija | Aprašymas |
|----------|-----------|
| `GetCustomerAttribute(field="...")` | Projekto lygio atributai |

### Persona Atributai (User-specifiniai)

| Funkcija | Aprašymas |
|----------|-----------|
| `GetPersonaAttribute(id=user_id, field="...")` | Gauti user-specific reikšmę |
| `SetPersonaAttribute(id=user_id, field="...", value="...")` | Nustatyti user-specific reikšmę |

### State (Sesijos Lygio)

| Funkcija | Aprašymas |
|----------|-----------|
| `GetState(name="...")` | Gauti sesijos state |
| `SetState(name="...", value="...")` | Nustatyti sesijos state |

### Įvykiai (Acts)

| Funkcija | Aprašymas |
|----------|-----------|
| `GetTriggeredAct(fields=["..."])` | Gauti trigger event duomenis |
| `CreateMessageAct(text=..., from="...", userActorId=...)` | Sukurti žinutės aktą |

---

## Integracijos Specializacijos

CAMainFlow turi atskirus skill'us skirtingoms kanalams:

| Skill | Kanalas | Aprašymas |
|-------|---------|-----------|
| `UserSMSReplySkill` | SMS | SMS žinučių apdorojimas |
| `UserPhoneReplySkill` | Phone (VAPI/Newo Voice) | Telefonijos žinučių apdorojimas |
| `UserTelegramReplySkill` | Telegram | Telegram žinučių apdorojimas |
| `UserAPIReplySkill` | API | API webhook žinučių apdorojimas |
| `UserSandboxReplySkill` | Sandbox | Testavimo aplinkos žinutės |
| `UserNewoChatReplySkill` | Newo Chat | Web chat žinučių apdorojimas |
| `UserProxyReplySkill` | Proxy | Proxy/peradresavimo žinutės |

---

## Pagalbiniai (Utility) Skill'ai

| Skill | Paskirtis |
|-------|-----------|
| `_getTimeZoneSkill` | Laiko juostos nustatymas |
| `_getWorkingHoursStatus` | Darbo valandų statuso tikrinimas |
| `_utilsCreatePhoneActorsSkill` | Telefono numerių actor'ų kūrimas |
| `_userMessageFastReplySkill` | Greito atsakymo generavimas |
| `_memoryCorrection` | Atminties korekcija |
| `_buildUserInformationSkill` | Vartotojo informacijos surinkimas |
| `_startNewSessionSkill` | Naujos sesijos pradžia |

---

## Sistemos Įvykių (System Events) Tipai

| Event ID | Paskirtis |
|----------|-----------|
| `extend_session` | Sesijos pratęsimas |
| `prepare_rag_context_command` | RAG konteksto paruošimas |
| `prepare_injecting_data` | Duomenų injektavimo paruošimas |
| `build_operating_phrase` | Darbo frazės generavimas |
| `urgent_message` | Skubaus pranešimo siuntimas |
| `convoagent_update_followup` | Follow-up timer atnaujinimas |
| `convoagent_enable_follow_up` | Follow-up įjungimas |
| `real_user_message` | Realaus vartotojo žinutės apdorojimas |
| `define_user_phone_number` | Vartotojo tel. nr. nustatymas |
| `send_external_reply` | Išorinio atsakymo siuntimas |

---

## Išvados

1. **Dualus sintaksės palaikymas**: NSL (Jinja2) ir Guidance (Mustache-like) sintaksės leidžia lanksčią skill rašymą pagal poreikius.

2. **Modulinė architektūra**: Skill'ai yra nepriklausomi vienetai, kurie gali kviečiami kaip funkcijos.

3. **State management**: Trys lygiai - State (sesijos), PersonaAttribute (user-specifiniai), CustomerAttribute (projekto lygio).

4. **Channel-agnostic**: Tas pats flow aptarnauja visus kanalus per specializuotus reply skill'us.

5. **Voice-to-voice integracija**: Yra specialus palaikymas OpenAI ir kitų voice-to-voice tiekėjų integracijai.

6. **Feature flag sistema**: Leidžia įjungti/išjungti funkcionalumą be kodo keitimų.

7. **Working hours awareness**: Sistema žino darbo valandas ir gali valdyti pokalbius pagal juos.
