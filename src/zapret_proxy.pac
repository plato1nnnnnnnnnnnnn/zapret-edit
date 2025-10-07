
function FindProxyForURL(url, host) {
    if (shExpMatch(host, '*discord.com') ||
        shExpMatch(host, '*cdn.discordapp.com') ||
        shExpMatch(host, '*youtube.com') ||
        shExpMatch(host, '*youtu.be') ||
        shExpMatch(host, '*googlevideo.com') ||
        shExpMatch(host, '*soundcloud.com') ||
        shExpMatch(host, '*spotify.com') ||
        shExpMatch(host, '*audio-ak.spotify.com') ||
        shExpMatch(host, '*t.me') ||
        shExpMatch(host, '*telegram.org') ||
        shExpMatch(host, '*whatsapp.com') ||
        shExpMatch(host, '*instagram.com') ||
        shExpMatch(host, '*facebook.com') ||
        shExpMatch(host, '*twitter.com') ||
        shExpMatch(host, '*tiktok.com') ||
        shExpMatch(host, '*snapchat.com') ||
        shExpMatch(host, '*linkedin.com') ||
        shExpMatch(host, '*pinterest.com') ||
        shExpMatch(host, '*reddit.com') ||
        shExpMatch(host, '*vimeo.com') ||
        shExpMatch(host, '*tumblr.com')) {
        return 'PROXY 127.0.0.1:8080; DIRECT';
    }
    return 'DIRECT';
}
