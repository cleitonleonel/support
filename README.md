# Support

<img src="https://github.com/cleitonleonel/support/blob/master/img/support.ico?raw=true" alt="Your image title" width="250"/>

**Confgurando ambiente:**

``sudo apt-get install x11vnc -y``

**Ativando ngrok**
- Após terminar a instalação de x11vnc acesse https://dashboard.ngrok.com/signup, crie uma conta, acesse https://dashboard.ngrok.com/get-started/setup e obtenha o token para execução do ngrok.


- Ao iniciar pela primeira vez esse token será solicitado, então fique atento.


- OBS:
  
    - Não será necessário o download do ngrok, isso será feito na primeira inicialização do módulo.

**Configure o Gmail para permitir aplicativos de terceiro**

- Precisamos habilitar sua conta do Gmail para receber conexões de programas externos.
- Abra seu navegador e acesse sua conta do Gmail.
- Em nosso exemplo, a seguinte URL foi inserida no Navegador:
http://gmail.google.com

- Na tela de login, digite seu nome de usuário e senha do Gmail.
![](https://github.com/cleitonleonel/support/blob/master/img/g_login.png)

- Após o login, você precisa acessar a seguinte URL:
- https://myaccount.google.com/signinoptions/two-step-verification
- Habilite a verificação em duas etapas nesta conta.
- Depois de habilitar a verificação de duas etapas, você precisa acessar a seguinte URL:
- https://security.google.com/settings/security/apppasswords
- Crie uma senha de aplicativo.
- Selecione o aplicativo gmail e o tipo de dispositivo: Outros.
![](https://github.com/cleitonleonel/support/blob/master/img/app_pass.png)

- Em nosso exemplo, nós nomeamos o dispositivo POWERSHELL.
- Clique no botão Gerar e tome nota da senha gerada aleatoriamente.
![](https://github.com/cleitonleonel/support/blob/master/img/make_pass.png)

- Em seguida, você precisa acessar a seguinte URL:
- https://accounts.google.com/DisplayUnlockCaptcha
- Clique no botão Continuar para ativar o acesso externo à sua conta do Google.
![](https://github.com/cleitonleonel/support/blob/master/img/access.png)

- Você terminou as etapas necessárias para a integração do Gmail.

**Instalando com pip:**

``
pip3 install git+https://github.com/cleitonleonel/support.git
``

## Uso:

``
python3 -m support
``

## Demonstração:

<img src="https://github.com/cleitonleonel/support/blob/master/img/support.gif?raw=true" alt="Your image title" width="700" height="400"/>


## Desenvolvido por:

Cleiton Leonel Creton ==> cleiton.leonel@gmail.com
