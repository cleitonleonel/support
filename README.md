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

O Gmail atualmente aplica diversas políticas para tentar evitar que um terceiro utilize a sua conta de email inclusive limitando o acesso de aplicativos diferentes do seu próprio webmail. Precisamos permitir o acesso de aplicativos de terceiros, denominado de “menos seguro” pelo Gmail, para poder conectar o nosso cliente de email ao smtp do Gmail.
- Abra o web browser e entre no endereço: https://myaccount.google.com/lesssecureapps
- Certifique-se de que está conectado com a conta do Gmail que irá utilizar para configurar o acesso. Caso esteja logado com uma conta diferente alterne para a conta a ser utilizada através do ícone correspondente à letra inicial da conta atual no canto superior direito.
- Mova o botão para o lado direito para ativar a opção **Permitir aplicativos menos seguros**. O botão ficará com a tonalidade azul.


**Instalando com pip:**

``
pip3 install git+https://github.com/cleitonleonel/support.git
``

## Uso:
- Suporte remoto simples com x11vnc + ngrok:

``
python3 -m support
``

## Desenvolvido por:

Cleiton Leonel Creton ==> cleiton.leonel@gmail.com