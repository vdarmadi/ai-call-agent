from vocode import AgentUpdateParams, WebhookUpdateParams, EventType, HttpMethod, PromptUpdateParams, \
    EndConversationActionParams
from vocode.client import Vocode

vocode_client = Vocode(
    token=""
)

initial_message = "Hello, thank you for calling. My name is John. How can I assist " \
                  "you today?"

webhook_url = ""
webhook = None
if webhook_url:
    webhook = WebhookUpdateParams(
        subscriptions=[EventType.EVENT_PHONE_CALL_ENDED],
        url=webhook_url,
        method=HttpMethod.POST,
    )

prompt_content = "Act as a call agent at a clinic." \
                 "1. Collect patient's name and date of birth." \
                 "2. Collect insurance information - Payer name and ID." \
                 "3. Ask if they have a referral, and to who." \
                 "4. Collect chief medical complaint/reason they are coming in." \
                 "5. Collect other demographics like address." \
                 "6. Collect contact information." \
                 "7. Offer up best available providers: " \
                 "Choose randomly from Doctor Alexander, Doctor George or Doctor Bill for providers." \
                 "8. Offer up best available times: " \
                 "Choose times randomly from September 19th 10am, September 26th 11am or October 3rd 2pm." \
                 "9. Do not end conversation until you have collected all information."

prompt = PromptUpdateParams(content=prompt_content)

# Just default voice due to performance issue with ElevenLabs and Play.ht voice.
voice_id = '88a79ab6-6e87-4706-93db-74e842a287d2'

end_call_action = vocode_client.actions.create_action(
    request=EndConversationActionParams(
        type="action_end_conversation",
    )
)

number = vocode_client.numbers.update_number(
    phone_number="", inbound_agent=AgentUpdateParams(initial_message=initial_message,
                                                     webhook=webhook,
                                                     prompt=prompt,
                                                     voice=voice_id,
                                                     actions=[end_call_action]
                                                     )
)
