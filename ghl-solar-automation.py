#!/usr/bin/env python3
"""
GHL Solar Lead Automation Script
Automatiškai tvarko saulės leadus GoHighLevel CRM

Naudojimas:
    python3 ghl-solar-automation.py --action new_lead --phone +3706XXXXXXX --name "Jonas"
    python3 ghl-solar-automation.py --action check_followups
    python3 ghl-solar-automation.py --action daily_report

Autorius: Juodčkis (Akseler AI)
"""

import os
import sys
import json
import argparse
from datetime import datetime, timedelta
from typing import Optional, Dict, List

# Konfigūracija (užpildysi kai gausi credentials)
HIGHLEVEL_TOKEN = os.getenv("HIGHLEVEL_TOKEN", "")
HIGHLEVEL_LOCATION_ID = os.getenv("HIGHLEVEL_LOCATION_ID", "")

# CEO nustatymai
CEO_PHONE = os.getenv("CEO_PHONE", "+370XXXXXXXX")  # Užpildyk savo numeriu
CEO_EMAIL = os.getenv("CEO_EMAIL", "ceo@akseler.lt")  # Užpildyk savo email

# Tag'ai
TAG_NEW_LEAD = "solar-lead"
TAG_WARM = "new-lead-warm"
TAG_CONTACTED = "contacted"
TAG_PROPOSAL_SENT = "proposal-sent"
TAG_CUSTOMER = "customer-active"
TAG_URGENT = "urgent-followup"

# Pipeline'ai
PIPELINE_SOLAR = "Solar Sales"
STAGE_NEW_LEAD = "New Lead"
STAGE_PROPOSAL = "Proposal Sent"
STAGE_WON = "Won"


class GHLClient:
    """GoHighLevel API klientas"""
    
    def __init__(self, token: str, location_id: str):
        self.token = token
        self.location_id = location_id
        self.base_url = "https://rest.gohighlevel.com/v1"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    
    def _request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """Bazinis API užklausos metodas"""
        import requests
        
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method == "GET":
                response = requests.get(url, headers=self.headers, timeout=30)
            elif method == "POST":
                response = requests.post(url, headers=self.headers, json=data, timeout=30)
            elif method == "PUT":
                response = requests.put(url, headers=self.headers, json=data, timeout=30)
            else:
                raise ValueError(f"Nepalaikomas metodas: {method}")
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ API klaida: {e}")
            return {"error": str(e)}
    
    # === CONTACT METHODS ===
    
    def get_contact_by_phone(self, phone: str) -> Optional[Dict]:
        """Rasti kontaktą pagal telefono numerį"""
        # GHL API: GET /contacts/?phone={phone}
        result = self._request("GET", f"/contacts/?phone={phone}")
        contacts = result.get("contacts", [])
        return contacts[0] if contacts else None
    
    def create_contact(self, first_name: str, phone: str, **kwargs) -> Dict:
        """Sukurti naują kontaktą"""
        data = {
            "firstName": first_name,
            "phone": phone,
            "tags": [TAG_NEW_LEAD],
            "source": kwargs.get("source", "automation"),
            "locationId": self.location_id
        }
        
        if "email" in kwargs:
            data["email"] = kwargs["email"]
        if "last_name" in kwargs:
            data["lastName"] = kwargs["last_name"]
        if "address" in kwargs:
            data["address1"] = kwargs["address"]
        
        return self._request("POST", "/contacts/", data)
    
    def update_contact(self, contact_id: str, **kwargs) -> Dict:
        """Atnaujinti kontaktą"""
        return self._request("PUT", f"/contacts/{contact_id}", kwargs)
    
    def add_tag_to_contact(self, contact_id: str, tag: str) -> Dict:
        """Pridėti tag'ą kontaktui"""
        return self._request("POST", f"/contacts/{contact_id}/tags", {"tags": [tag]})
    
    def remove_tag_from_contact(self, contact_id: str, tag: str) -> Dict:
        """Pašalinti tag'ą iš kontakto"""
        return self._request("DELETE", f"/contacts/{contact_id}/tags/{tag}")
    
    # === PIPELINE METHODS ===
    
    def get_pipelines(self) -> List[Dict]:
        """Gauti visus pipeline'us"""
        result = self._request("GET", f"/pipelines/?locationId={self.location_id}")
        return result.get("pipelines", [])
    
    def create_opportunity(self, contact_id: str, pipeline_id: str, 
                          stage_id: str, name: str, value: float = 0) -> Dict:
        """Sukurti opportunity (deal)"""
        data = {
            "contactId": contact_id,
            "pipelineId": pipeline_id,
            "stageId": stage_id,
            "name": name,
            "status": "open",
            "monetaryValue": value,
            "locationId": self.location_id
        }
        return self._request("POST", "/opportunities/", data)
    
    def move_opportunity_stage(self, opportunity_id: str, stage_id: str) -> Dict:
        """Perkelti opportunity į kitą stage"""
        return self._request("PUT", f"/opportunities/{opportunity_id}", {
            "stageId": stage_id
        })
    
    def close_opportunity(self, opportunity_id: str, status: str = "won") -> Dict:
        """Uždaryti opportunity (won/lost)"""
        return self._request("PUT", f"/opportunities/{opportunity_id}", {
            "status": status
        })
    
    # === TASK METHODS ===
    
    def create_task(self, contact_id: str, title: str, due_date: str,
                   assigned_to: str, priority: str = "medium") -> Dict:
        """Sukurti užduotį"""
        data = {
            "contactId": contact_id,
            "title": title,
            "dueDate": due_date,
            "assignedTo": assigned_to,
            "priority": priority,
            "locationId": self.location_id
        }
        return self._request("POST", "/tasks/", data)
    
    def get_due_tasks(self, date_from: str, date_to: str) -> List[Dict]:
        """Gauti artėjančias užduotis"""
        result = self._request("GET", 
            f"/tasks/?locationId={self.location_id}&startDate={date_from}&endDate={date_to}")
        return result.get("tasks", [])
    
    # === SMS METHODS ===
    
    def send_sms(self, contact_id: str, message: str, template_id: Optional[str] = None) -> Dict:
        """Siųsti SMS kontaktui"""
        data = {
            "contactId": contact_id,
            "message": message,
            "locationId": self.location_id
        }
        if template_id:
            data["templateId"] = template_id
        
        return self._request("POST", "/sms/send", data)
    
    def send_sms_to_phone(self, phone: str, message: str) -> Dict:
        """Siųsti SMS pagal telefono numerį"""
        # Pirma randam kontaktą, tada siunčiam
        contact = self.get_contact_by_phone(phone)
        if contact:
            return self.send_sms(contact["id"], message)
        else:
            # Jei kontakto nėra - sukuriam ir siunčiam
            print(f"⚠️ Kontaktas nerastas, kuriu naują...")
            contact = self.create_contact("Naujas Lead", phone)
            return self.send_sms(contact.get("id"), message)
    
    # === SEARCH METHODS ===
    
    def search_contacts_by_tag(self, tag: str, limit: int = 100) -> List[Dict]:
        """Ieškoti kontaktų pagal tag'ą"""
        result = self._request("GET", 
            f"/contacts/?locationId={self.location_id}&tag={tag}&limit={limit}")
        return result.get("contacts", [])
    
    def get_recent_contacts(self, hours: int = 24) -> List[Dict]:
        """Gauti neseniai sukurtus kontaktus"""
        since = (datetime.now() - timedelta(hours=hours)).isoformat()
        result = self._request("GET", 
            f"/contacts/?locationId={self.location_id}&startAfter={since}")
        return result.get("contacts", [])


class SolarLeadAutomation:
    """Saulės leadų automatizavimo logika"""
    
    def __init__(self):
        if not HIGHLEVEL_TOKEN or not HIGHLEVEL_LOCATION_ID:
            print("❌ Klaida: Trūksta HIGHLEVEL_TOKEN arba HIGHLEVEL_LOCATION_ID")
            print("💡 Nustatyk aplinkos kintamuosius arba redaguok šį script'ą")
            sys.exit(1)
        
        self.ghl = GHLClient(HIGHLEVEL_TOKEN, HIGHLEVEL_LOCATION_ID)
    
    # === DARBŲ FUNKCIJOS ===
    
    def process_new_lead(self, phone: str, name: str, **kwargs):
        """
        Apdoroti naują leadą
        
        Workflow:
        1. Sukurti kontaktą (arba atnaujinti)
        2. Pridėti tag'ą
        3. Siųsti pasveikinimo SMS
        4. Sukurti užduotį CEO
        5. Pridėti į pipeline
        """
        print(f"🔄 Apdoroju naują leadą: {name} ({phone})")
        
        # 1. Rasti ar sukurti kontaktą
        contact = self.ghl.get_contact_by_phone(phone)
        if contact:
            print(f"✅ Rastas esamas kontaktas: {contact.get('id')}")
            contact_id = contact["id"]
        else:
            print(f"📝 kuriu naują kontaktą...")
            result = self.ghl.create_contact(name, phone, **kwargs)
            contact_id = result.get("id")
            print(f"✅ Sukurtas kontaktas: {contact_id}")
        
        # 2. Pridėti tag'ą
        self.ghl.add_tag_to_contact(contact_id, TAG_WARM)
        print(f"🏷️ Pridėtas tag'as: {TAG_WARM}")
        
        # 3. Siųsti pasveikinimo SMS
        message = f"Labas {name}! 👋 Gavau Jūsų užklausą dėl saulės elektrinės. Skambinsiu per 15 min! - CEO, Akseler"
        self.ghl.send_sms(contact_id, message)
        print(f"📱 Išsiųstas SMS")
        
        # 4. Sukurti užduotį CEO
        due = (datetime.now() + timedelta(minutes=15)).isoformat()
        self.ghl.create_task(
            contact_id=contact_id,
            title=f"Paskambinti {name}",
            due_date=due,
            assigned_to="CEO",  # Pakeisk į savo GHL user ID
            priority="high"
        )
        print(f"📋 Sukurta užduotis (terminas: 15 min)")
        
        # 5. Sukurti opportunity pipeline'e
        # Note: Čia reikia turėti pipeline ID ir stage ID
        print(f"💡 Priminimas: rankiniu būdu pridėk į '{PIPELINE_SOLAR}' pipeline")
        
        print(f"\n✅ Leadas apdorotas sėkmingai!")
        return contact_id
    
    def check_overdue_followups(self):
        """
        Patikrinti vėluojančius follow-up
        
        Suranda kontaktus su tag 'new-lead-warm' be 'contacted'
        ilgiau nei 1 valandą
        """
        print("🔍 Tikrinu vėluojančius follow-up...")
        
        warm_leads = self.ghl.search_contacts_by_tag(TAG_WARM)
        overdue = []
        
        for lead in warm_leads:
            tags = lead.get("tags", [])
            if TAG_CONTACTED not in tags:
                # Patikrinam kada sukurtas
                created = lead.get("dateAdded", "")
                if created:
                    created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
                    if datetime.now().timestamp() - created_dt.timestamp() > 3600:  # 1 valanda
                        overdue.append(lead)
        
        if overdue:
            print(f"⚠️ Rasta {len(overdue)} vėluojančių leadų!")
            for lead in overdue:
                name = f"{lead.get('firstName', '')} {lead.get('lastName', '')}".strip()
                phone = lead.get("phone", "")
                print(f"  - {name} ({phone})")
                
                # Pridėti urgent tag
                self.ghl.add_tag_to_contact(lead["id"], TAG_URGENT)
                
            # Siųsti alert CEO
            alert_msg = f"🚨 {len(overdue)} leadų laukia skambučio jau >1 val!"
            # TODO: Siųsti push notification arba SMS CEO
            print(f"\n📱 Alert: {alert_msg}")
        else:
            print("✅ Visi leadai apdoroti laiku")
        
        return overdue
    
    def send_proposal_followup(self, contact_id: str, name: str):
        """Siųsti follow-up po pasiūlymo"""
        message = f"Sveiki {name}! Kaip Jums pasiūlymas? Gal norėtumėte aptarti detales? 📋 - CEO, Akseler"
        self.ghl.send_sms(contact_id, message)
        print(f"📱 Išsiųstas follow-up SMS kontaktui {name}")
    
    def mark_deal_won(self, contact_id: str, value: float = 0):
        """Pažymėti deal kaip laimėtą"""
        # Gauti opportunity
        # Uždaryti kaip 'won'
        # Pridėti customer tag
        # Siųsti sveikinimo SMS
        
        self.ghl.add_tag_to_contact(contact_id, TAG_CUSTOMER)
        self.ghl.remove_tag_from_contact(contact_id, TAG_PROPOSAL_SENT)
        
        contact = self.ghl._request("GET", f"/contacts/{contact_id}")
        name = contact.get("firstName", "Klientas")
        
        message = f"🎉 Sveikiname {name}! Jūsų saulės elektrinė bus įrengta netrukus. Paskambinsiu dėl montavimo datos. Džiaugiuosi bendradarbiavimu! ☀️"
        self.ghl.send_sms(contact_id, message)
        
        # Sukurti montavimo užduotį
        due = (datetime.now() + timedelta(days=1)).isoformat()
        self.ghl.create_task(
            contact_id=contact_id,
            title=f"Suplanuoti montavimą - {name}",
            due_date=due,
            assigned_to="CEO",
            priority="high"
        )
        
        print(f"✅ Deal pažymėtas kaip WON! Vertė: {value}€")
    
    def get_daily_report(self):
        """Gauti dienos ataskaitą"""
        print("📊 Dienos ataskaita")
        print("=" * 40)
        
        # Nauji leadai per 24h
        recent = self.ghl.get_recent_contacts(24)
        print(f"📥 Nauji leadai (24h): {len(recent)}")
        
        # Šilti leadai laukiantys
        warm = self.ghl.search_contacts_by_tag(TAG_WARM)
        print(f"🔥 Šilti leadai: {len(warm)}")
        
        # Pasiūlymai išsiųsti
        proposals = self.ghl.search_contacts_by_tag(TAG_PROPOSAL_SENT)
        print(f"📋 Pasiūlymai išsiųsti: {len(proposals)}")
        
        # Uždaryti deal'ai
        customers = self.ghl.search_contacts_by_tag(TAG_CUSTOMER)
        print(f"💰 Klientai: {len(customers)}")
        
        # Užduotys šiandien
        today = datetime.now().strftime("%Y-%m-%d")
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        tasks = self.ghl.get_due_tasks(today, tomorrow)
        print(f"📋 Užduotys šiandien: {len(tasks)}")
        
        return {
            "new_leads_24h": len(recent),
            "warm_leads": len(warm),
            "proposals_sent": len(proposals),
            "customers": len(customers),
            "tasks_today": len(tasks)
        }
    
    def bulk_reactivation(self, days_inactive: int = 30):
        """Masinė reaktyvacija neaktyvių leadų"""
        print(f"🔄 Renku neaktyvius leadus ({days_inactive} d.)...")
        
        # Surasti leadus be activity X dienų
        # Pridėti reactivation tag
        # Siųsti SMS
        
        message_template = "Sveiki! Praėjusį mėnesį domėjotės saulės elektrine. Ar vis dar aktualu? Kaina gali būti dar patrauklesnė! 📉 - CEO, Akseler"
        
        # Čia reikėtų implementuoti pagal GHL API capabilities
        print("💡 Naudok GHL workflow automatizavimui")


def main():
    parser = argparse.ArgumentParser(
        description="GHL Solar Lead Automation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Pavyzdžiai:
  # Naujas leadas
  python3 ghl-solar-automation.py --action new_lead --phone +37061234567 --name "Jonas"
  
  # Tikrinimas
  python3 ghl-solar-automation.py --action check_followups
  
  # Dienos ataskaita
  python3 ghl-solar-automation.py --action daily_report
        """
    )
    
    parser.add_argument("--action", required=True,
                       choices=["new_lead", "check_followups", "daily_report", 
                               "proposal_followup", "deal_won", "reactivation"],
                       help="Ką daryti")
    parser.add_argument("--phone", help="Telefono numeris")
    parser.add_argument("--name", help="Vardas")
    parser.add_argument("--email", help="El. paštas")
    parser.add_argument("--contact-id", help="GHL Contact ID")
    parser.add_argument("--value", type=float, help="Deal vertė (EUR)")
    
    args = parser.parse_args()
    
    # Inicializuoti automatizavimą
    auto = SolarLeadAutomation()
    
    # Vykdyti veiksmą
    if args.action == "new_lead":
        if not args.phone or not args.name:
            print("❌ Reikalingi: --phone ir --name")
            sys.exit(1)
        auto.process_new_lead(args.phone, args.name, email=args.email)
    
    elif args.action == "check_followups":
        auto.check_overdue_followups()
    
    elif args.action == "daily_report":
        auto.get_daily_report()
    
    elif args.action == "proposal_followup":
        if not args.contact_id or not args.name:
            print("❌ Reikalingi: --contact-id ir --name")
            sys.exit(1)
        auto.send_proposal_followup(args.contact_id, args.name)
    
    elif args.action == "deal_won":
        if not args.contact_id:
            print("❌ Reikalingas: --contact-id")
            sys.exit(1)
        auto.mark_deal_won(args.contact_id, args.value or 0)
    
    elif args.action == "reactivation":
        auto.bulk_reactivation()


if __name__ == "__main__":
    main()
