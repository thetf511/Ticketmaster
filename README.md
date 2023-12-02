# Discord Bot für Support und Rollenverwaltung

Dieser Discord-Bot wurde mit Python und der Discord.py-Bibliothek erstellt. Der Bot bietet Funktionen für die Erstellung von Support-Channels und die Verwaltung von Rollen in einem Textkanal.

## Funktionen

### 1. Support-Channel erstellen

Verwende den Befehl `!support`, um einen Support-Channel zu erstellen. Ein eingebettetes Nachrichtenfenster wird angezeigt, und Benutzer können auf die 🆘-Reaktion klicken, um ihren eigenen Support-Channel zu erstellen.

### 2. Rollenverwaltung in einem Textkanal

Verwende den Befehl `!rollen <channel_id> <role1> <role2> ...`, um Rollenberechtigungen in einem bestimmten Textkanal zu verwalten.

### 3. Support-Channel schließen

Verwende den Befehl `!close`, um einen Support-Channel zu schließen und zu löschen.

## Konfiguration

1. Installiere die erforderlichen Abhängigkeiten mit `pip install discord.py`.

2. Füge deinen Bot-Token in die letzte Zeile des Codes ein:

```python
bot.run('DEIN_BOT_TOKEN')
