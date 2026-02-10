# Client Scenarios - Found in Production

**Source:** Newo platform (Hospitality/Ginklu Klubas)  
**Found:** 2026-02-10  
**Connected to:** CAMainFlow

---

## 🎬 SCENARIOS

### Scenario 1: "Make a Regular Reservation via Link"

**Purpose:** Handle reservations for parties smaller than the large-group threshold

**Flow:**
1. Collect dates and guest counts
2. Use required code-phrase to check Availability section
3. Confirm a slot
4. Gather guest's name, phone, and required details
5. Send booking link via required SMS code-phrase
6. Guide guest through self-scheduling
7. Confirm completion
8. If booked: provide warm thanks and check-in notes
9. Close conversation

---

### Scenario 2: "Make a Large Group Reservation via Email"

**Purpose:** Handle large group reservations (above threshold)

**Flow:**
1. Collect guest count
2. Collect name
3. Collect preferred date/time
4. Collect phone
5. Collect email
6. Collect venue-specific questions
7. Based on channel and business hours:
   - Connect user with manager, OR
   - Forward details and text summary
8. Close conversation

---

### Scenario 3: "Relaying Message to the Manager"

**Purpose:** Forward messages to manager/staff

**Flow:**
1. Collect specific message user wants to relay
2. Use available context when possible
3. If not enough context: reconfirm or gather user's name and phone
4. Inform them you'll pass the message along
5. Note that any scheduling changes aren't final until human confirms
6. Close conversation

---

### Scenario 4: "Answering Questions"

**Purpose:** General Q&A using BusinessContext and AdditionalInformation

**Rules:**
- Reply in up to 10 words for service-type queries
- Offer fuller details when requested
- Give only general pricing guidance (exact figures require consultation)
- Direct discount/referral inquiries to the office
- After responding: close interaction according to Finish Conversation scenario

---

### Scenario 5: "Regular Transfer"

**Purpose:** Transfer to human agent

**Phone:**
- Transfer caller following CALL TRANSFERRING rule in ExplicitConstraints

**Chat:**
- Provide manager's escalation phone number from ExplicitConstraints
- Offer further assistance

---

### Scenario 20: "Finish Conversation"

**Purpose:** Properly close any interaction

**Flow:**
1. Politely conclude interaction
2. Warmly thank the user
3. Address any remaining requests
4. Ask if there's anything else you can help with
5. If it's a booking: add enthusiastic note about upcoming appointment

---

### Scenario 2 (Alternative): "Scheduling Appointment via Agent"

**Purpose:** Agent-guided appointment scheduling

**Flow:**
1. Confirm services
2. Gather preferred date/time
3. Use required phrase to check availability
4. Present options from AvailabilityForTheUserRequestedDateTime section
5. Collect name, phone, and email
6. After user approval: use required submission phrase
7. Wait for booking confirmation (or report system error)
8. Close conversation

---

## 📊 SUMMARY

| Scenario | Purpose | Key Actions |
|----------|---------|-------------|
| 1 | Regular Reservation via Link | Self-service booking with guidance |
| 2 | Large Group via Email | Manual handling, manager connection |
| 3 | Relay Message | Manager escalation |
| 4 | Answer Questions | Q&A with constraints |
| 5 | Transfer | Human handoff |
| 20 | Finish Conversation | Proper closure |
| 2 (Alt) | Agent Scheduling | Full-service booking |

---

## 🔗 RELATED PROCEDURES

These scenarios reference:
- **procedure_common_gather_name** - Name collection
- **procedure_common_gather_phone_number** - Phone collection
- **procedure_common_gather_email** - Email collection
- **procedure_common_gather_availability_hospitality** - Availability checking

---

## 🎯 KEY PATTERNS

1. **Channel Awareness:** Different flows for phone vs chat
2. **Business Hours Check:** Large groups handled differently based on hours
3. **Required Code Phrases:** Specific phrases for system actions
4. **Context Usage:** BusinessContext and AdditionalInformation for answers
5. **Confirmation Steps:** Always confirm before finalizing
6. **Proper Closure:** Every scenario ends with Finish Conversation

---

**Status:** FOUND - Real production scenarios  
**Next:** Need to find corresponding Intent Type Map and Procedures JSON
