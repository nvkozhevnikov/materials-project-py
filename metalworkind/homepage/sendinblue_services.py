from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

import config

def subscribe_doi(email):
    """ Подписаться double opt in в sendinblue.com. Инструкция https://developers.sendinblue.com/reference/createdoicontact"""

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = config.SENDINBLUE_API_KEY

    api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(configuration))
    create_doi_contact = sib_api_v3_sdk.CreateDoiContact(email=email,
                                                         include_list_ids=[config.SENDINBLUE_LIST_ID],
                                                         template_id=1,
                                                         redirection_url="https://metalworkind.com")
    try:
        api_instance.create_doi_contact(create_doi_contact)
    except ApiException as e:
        print("Exception when calling ContactsApi->create_doi_contact: %s\n" % e)

def send_transactional_email(data):
    """ Описание API - https://developers.sendinblue.com/reference/sendtransacemail """

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = config.SENDINBLUE_API_KEY

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = data['subject']
    html_content = f"<html><body>{data['message']}</body></html>"
    to = [{"name": config.SITE_NAME, "email": config.SENDINBLUE_ADMIN_ADDRESS}]
    sender = {"email": data['email'], "name": data['name']}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content,
                                                   sender=sender, subject=subject)

    try:
        api_instance.send_transac_email(send_smtp_email)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)