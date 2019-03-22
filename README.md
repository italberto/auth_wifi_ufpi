# Autenticador de rede da UFPI

Este simples script tem o objetivo de criar um mecanismo para manter uma máquina sempre comectada na rede da UFPI, visto que as máquinas inativas são desligadas após un certo período de tempo.

Para usá-lo, basta adicionar uma entrada no arquivo crontab da seginte maneira:

  $ sudo echo '0 */1 * * *     [usuario_so]     /usr/bin/python2.7 [caminho_do_script]auth_wifi_ufpi.py [usuario_ufpi] [senha_ufpi] [driver_gecko_path] >/dev/null 2>&1' > /etc/crontab
 
A cada uma hora, o script será executado.
