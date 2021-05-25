# Support

<img src="https://github.com/cleitonleonel/support/blob/master/img/support.ico?raw=true" alt="Your image title" width="250"/>

**Confgurando ambiente:**

``sudo apt-get install x11vnc -y``

**Ativando ngrok**
- Após isso acesse https://dashboard.ngrok.com/signup, crie uma conta, acesse https://dashboard.ngrok.com/get-started/setup e obtenha o token para execução do ngrok.


- Ao iniciar pela primeira vez esse token será solicitado, então fique atento.


- OBS:
  
    - Não será necessário o download do ngrok, isso será feito na primeira inicialização do módulo.

**Instalando com pip:**

``
pip3 install git+https://github.com/cleitonleonel/support.git
``

## Uso:
- Suporte remoto simples com x11vnc + ngrok:

``
python3 -m support.py
``

## Desenvolvido por:

Cleiton Leonel Creton ==> cleiton.leonel@gmail.com