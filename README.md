# AI Call Agent Project

![image info](./ai-call-agent.png)

1. `ai-call-agent/requirements.txt`
   1. contains packages used by this project
   2. creating environment
      1. install `python3`, `venv`, `pip`
      2. run `python3 -m venv ai-call-agent_env`
      3. run `source ai-call-agent_env/bin/activate`
      4. run `pip install -r ai-call-agent/requirements.txt`
2. `ai-call-agent/vocode_config.py`
   1. a script to configure Vocode AI agent for the first time.
   2. run this using `python vocode_config.py`
3. `ai-call-agent/clinic/*` and `ai-call-agent/manage.py`
   1. this is a Django web project containing 1 webhook API endpoint to be called by Vocode.
   2. the entry point for the API endpoint is `ai-call-agent/clinic/phoneagent/views.py`
   3. `ai-call-agent/clinic/phoneagent/parser.py` contains parser logic for doctor name and appointment time extraction.
   4. `ai-call-agent/clinic/phoneagent/notification.py` is the module to send sms notication via Twilio.
   5. `ai-call-agent/clinic/urls.py` contains endpoint paths configuration.
   6. `ai-call-agent/clinic/settings.py` contains parameters and env variables.
   7. run server by executing `python manage.py runserver` on the root dir.


