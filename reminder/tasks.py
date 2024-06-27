import datetime

from celery import shared_task

from .models import Person, Event



def send_congrats_email(email, message):
    # Sett up email setting for sending email
    pass


def send_congrats_sms(token, phone_number, message):
    # Sett up SMS setting for sending SMS
    pass



@shared_task
def send_congrats_task():
    today = datetime.date.today()
    persons = Person.objects.filter(congrats_birth=True, birth_date=today)
    if persons.exists():
        for person in persons:
            if person.send_type == "EM":
                send_congrats_email(person.email, person.message)
            elif person.send_type == "PN":
                send_congrats_sms(person.user_rel.token, person.phone_number, person.message)
            elif person.send_type == "BO":
                send_congrats_email(person.email, person.message)
                send_congrats_sms(person.user_rel.token, person.phone_number, person.message)
            else:
                continue


def send_congrats_email_queue(emails, message):
    for email in emails:
        # Send email one by one
        pass


def send_congrats_sms_queue(token, phone_numbers, message):
    for phone_number in phone_numbers:
        # Send sms one by one with token
        pass


@shared_task
def event_send_task():
    today = datetime.date.today()
    events = Event.objects.filter(send_massage_time=today)
    if events.exists:
        for event in events:
            phone_numbers = []
            emails = []
            if event.send_type == "EM":
                for person in event.persons_rel:
                    emails.append(person.email)
                send_congrats_email_queue(emails, event.message)
            elif event.send_type == "PN":
                for person in event.persons_rel:
                    phone_numbers.append(person.phone_number)
                send_congrats_sms_queue(event.user_rel.token, phone_numbers, event.message)
            elif event.send_type == "BO":
                for person in event.persons_rel:
                    emails.append(person.email)
                    phone_numbers.append(person.phone_number)
                send_congrats_email_queue(emails, event.message)
                send_congrats_sms_queue(event.user_rel.token, phone_numbers, event.message)
            else:
                continue