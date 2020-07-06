import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\CQRS-kata")
from src.app.adapters.repositories import FakeEventStoreRepository
from src.app.model.events import Event
from datetime import datetime
from dataclasses import dataclass
import json


@dataclass
class EventTest(Event):
    ref:str

    def to_dict(self):
        return {'event':str(type(self)), 'ref':self.ref, 'ocurred_on':self.ocurred_on}


def test_event_store_keep_events():
    assert len(FakeEventStoreRepository.list_all())==0
    ev=EventTest("evento-1")
    FakeEventStoreRepository.add(ev)
    print(FakeEventStoreRepository.list_all())
    assert len(FakeEventStoreRepository.list_all())==1    
    FakeEventStoreRepository.clear()


