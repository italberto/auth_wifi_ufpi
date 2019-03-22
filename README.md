# Autenticador de rede da UFPI

Este simples script tem o objetivo de criar um mecanismo para manter uma máquina sempre comectada na rede da UFPI, visto que as máquinas inativas são desligadas após un certo período de tempo.

Para usá-lo, basta adicionar uma entrada no arquivo crontab da seginte maneira:

> $ sudo echo '0 */1 * * *     [usuario_so]     /usr/bin/python2.7 [caminho_do_script]auth_wifi_ufpi.py [usuario_ufpi] [senha_ufpi] [driver_gecko_path] >/dev/null 2>&1' > /etc/crontab
 
 Não esquecer de substituir os parâmetros no comando:
 * [usuario_so]
 * [caminho_do_script]
 * [usuario_ufpi]
 * [senha_ufpi]
 * [driver_gecko_path]
 
A cada uma hora, o script será executado.

Use o link a seguir para baixar a última versão: [latest](https://github.com/italberto/auth_wifi_ufpi/releases/download/0.1/auth_wifi_ufpi.bin).

**OBS:** Se for usar a distribuição em vez do código fonte, use o código a seguir para inserir a entrada no cron:

> $ sudo echo '0 */1 * * *     [usuario_so]     /usr/bin/python2.7 [caminho_do_script]auth_wifi_ufpi.bin [usuario_ufpi] [senha_ufpi] >/dev/null 2>&1' > /etc/crontab
