import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / 'config.json'
PAC_PATH = Path(__file__).parent / 'zapret_proxy.pac'

with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

enabled = config.get('enabled_services', [])

SERVICE_DOMAINS = {
    'discord': ['discord.com', 'cdn.discordapp.com'],
    'youtube': ['youtube.com', 'youtu.be', 'googlevideo.com'],
    'soundcloud': ['soundcloud.com'],
    'spotify': ['spotify.com', 'audio-ak.spotify.com'],
    'telegram': ['t.me', 'telegram.org'],
    'whatsapp': ['whatsapp.com'],
    'instagram': ['instagram.com'],
    'facebook': ['facebook.com'],
    'twitter': ['twitter.com'],
    'tiktok': ['tiktok.com'],
    'snapchat': ['snapchat.com'],
    'linkedin': ['linkedin.com'],
    'pinterest': ['pinterest.com'],
    'reddit': ['reddit.com'],
    'vimeo': ['vimeo.com'],
    'tumblr': ['tumblr.com']
}

def domains_for_enabled(enabled_services):
    doms = []
    for svc in enabled_services:
        doms += SERVICE_DOMAINS.get(svc, [])
    return doms

def generate_pac(domains, proxy_host='127.0.0.1', proxy_port=8080):
    proxy = f"PROXY {proxy_host}:{proxy_port}; DIRECT"
    domain_checks = []
    for d in domains:
        # ensure exact and subdomain matches
        domain_checks.append(f"shExpMatch(host, '*{d}')")

    rules = ' ||\n        '.join(domain_checks) if domain_checks else 'false'

    pac = f"""
function FindProxyForURL(url, host) {{
    if ({rules}) {{
        return '{proxy}';
    }}
    return 'DIRECT';
}}
"""
    return pac

if __name__ == '__main__':
    doms = domains_for_enabled(enabled)
    pac_text = generate_pac(doms)
    with open(PAC_PATH, 'w') as f:
        f.write(pac_text)
    print(f"Generated PAC at {PAC_PATH}")
