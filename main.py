import webview
import psutil
import json


class Api:
    def get_system_info(self):
        cpu = psutil.cpu_percent(interval=0.5)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        return json.dumps({
            "cpu_percent": cpu,
            "ram_percent": ram.percent,
            "ram_used_gb": round(ram.used / (1024 ** 3), 1),
            "ram_total_gb": round(ram.total / (1024 ** 3), 1),
            "disk_percent": disk.percent,
            "disk_used_gb": round(disk.used / (1024 ** 3), 1),
            "disk_total_gb": round(disk.total / (1024 ** 3), 1),
        })

    def search_commands(self, query):
        query = query.lower().strip()
        results = [c for c in COMMANDS if query in c["komut"].lower() or query in c["aciklama"].lower()]
        return json.dumps(results[:8])


COMMANDS = [
    {"komut": "ls", "aciklama": "Bulunduğun klasördeki dosya ve klasörleri listeler.", "ornek": "ls -l (detaylı liste için)"},
    {"komut": "cd", "aciklama": "Başka bir klasöre geçiş yapar (change directory).", "ornek": "cd Belgeler"},
    {"komut": "pwd", "aciklama": "Şu an hangi klasörde olduğunu gösterir (print working directory).", "ornek": "pwd"},
    {"komut": "mkdir", "aciklama": "Yeni bir klasör oluşturur (make directory).", "ornek": "mkdir yeni_klasor"},
    {"komut": "rm", "aciklama": "Dosya veya klasör siler. DİKKAT: geri dönüşü yoktur!", "ornek": "rm dosya.txt"},
    {"komut": "cp", "aciklama": "Dosya veya klasörü kopyalar (copy).", "ornek": "cp dosya.txt yedek.txt"},
    {"komut": "mv", "aciklama": "Dosya/klasörü taşır veya yeniden adlandırır (move).", "ornek": "mv eski.txt yeni.txt"},
    {"komut": "sudo", "aciklama": "Bir komutu yönetici (admin) yetkisiyle çalıştırır. Dikkatli kullan.", "ornek": "sudo apt update"},
    {"komut": "apt", "aciklama": "Pardus'ta program kurmak, güncellemek veya kaldırmak için kullanılır.", "ornek": "sudo apt install firefox"},
    {"komut": "apt update", "aciklama": "Sistemdeki paket listesini günceller (yeni sürümleri kontrol eder).", "ornek": "sudo apt update"},
    {"komut": "apt upgrade", "aciklama": "Bilgisayarındaki programları en güncel sürümlerine yükseltir.", "ornek": "sudo apt upgrade"},
    {"komut": "df", "aciklama": "Disk alanının ne kadarının dolu/boş olduğunu gösterir.", "ornek": "df -h (okunabilir formatta)"},
    {"komut": "top", "aciklama": "Çalışan programları ve ne kadar kaynak kullandıklarını canlı gösterir.", "ornek": "top (çıkmak için q)"},
    {"komut": "clear", "aciklama": "Terminal ekranını temizler, yazılanları siler (dosyaları etkilemez).", "ornek": "clear"},
    {"komut": "man", "aciklama": "Bir komutun kullanım kılavuzunu (manual) gösterir.", "ornek": "man ls"},
    {"komut": "chmod", "aciklama": "Bir dosyanın kimlerin okuyabileceğini/çalıştırabileceğini ayarlar (izinler).", "ornek": "chmod +x script.sh"},
    {"komut": "history", "aciklama": "Daha önce yazdığın komutların listesini gösterir.", "ornek": "history"},
    {"komut": "echo", "aciklama": "Yazdığın metni ekrana yazdırır.", "ornek": "echo Merhaba"},
    {"komut": "cat", "aciklama": "Bir dosyanın içeriğini ekranda gösterir.", "ornek": "cat notlar.txt"},
    {"komut": "grep", "aciklama": "Dosya içinde belirli bir kelimeyi/metni arar.", "ornek": "grep hata log.txt"},
    {"komut": "less", "aciklama": "Uzun bir dosyayı sayfa sayfa okumanı sağlar.", "ornek": "less log.txt"},
    {"komut": "more", "aciklama": "less'e benzer, dosyayı parça parça gösterir.", "ornek": "more log.txt"},
    {"komut": "sort", "aciklama": "Bir dosyanın satırlarını alfabetik/sayısal sıralar.", "ornek": "sort isimler.txt"},
    {"komut": "uniq", "aciklama": "Tekrar eden satırları listeden kaldırır.", "ornek": "uniq liste.txt"},
    {"komut": "awk", "aciklama": "Metin dosyalarında sütun bazlı işlem yapan güçlü bir araç.", "ornek": "awk '{print $1}' dosya.txt"},
    {"komut": "sed", "aciklama": "Bir dosyada metin bulup değiştirir.", "ornek": "sed 's/eski/yeni/' dosya.txt"},
    {"komut": "cut", "aciklama": "Bir satırdan belirli bir sütunu/kısmı keser, alır.", "ornek": "cut -d',' -f1 dosya.csv"},
    {"komut": "tr", "aciklama": "Karakterleri başka karakterlerle değiştirir.", "ornek": "tr 'a-z' 'A-Z' < dosya.txt"},
    {"komut": "xargs", "aciklama": "Bir komutun çıktısını başka bir komuta girdi olarak aktarır.", "ornek": "find . -name '*.txt' | xargs rm"},
    {"komut": "tee", "aciklama": "Bir çıktıyı hem ekrana yazar hem dosyaya kaydeder.", "ornek": "ls | tee liste.txt"},
    {"komut": "mount", "aciklama": "Bir diski veya USB belleği sisteme bağlar.", "ornek": "sudo mount /dev/sdb1 /media/usb"},
    {"komut": "umount", "aciklama": "Bağlı bir diski güvenle çıkarır.", "ornek": "sudo umount /media/usb"},
    {"komut": "lsblk", "aciklama": "Bilgisayardaki tüm diskleri ve bölümleri listeler.", "ornek": "lsblk"},
    {"komut": "fdisk", "aciklama": "Disk bölümlerini (partition) yönetmeye yarar.", "ornek": "sudo fdisk -l"},
    {"komut": "free", "aciklama": "Boş ve kullanılan RAM miktarını gösterir.", "ornek": "free -h"},
    {"komut": "uname", "aciklama": "İşletim sistemi ve çekirdek (kernel) bilgisini gösterir.", "ornek": "uname -a"},
    {"komut": "hostname", "aciklama": "Bilgisayarın ağdaki adını gösterir.", "ornek": "hostname"},
    {"komut": "hostnamectl", "aciklama": "Bilgisayarın adını ve sistem bilgilerini gösterir/değiştirir.", "ornek": "hostnamectl"},
    {"komut": "systemctl", "aciklama": "Sistem servislerini başlatır, durdurur, durumunu gösterir.", "ornek": "systemctl status bluetooth"},
    {"komut": "journalctl", "aciklama": "Sistem günlüklerini (logları) görüntüler.", "ornek": "journalctl -xe"},
    {"komut": "crontab", "aciklama": "Belirli zamanlarda otomatik çalışacak görevler ayarlar.", "ornek": "crontab -e"},
    {"komut": "killall", "aciklama": "Aynı isimdeki tüm çalışan programları kapatır.", "ornek": "killall firefox"},
    {"komut": "jobs", "aciklama": "Arka planda çalışan görevleri listeler.", "ornek": "jobs"},
    {"komut": "bg", "aciklama": "Durdurulmuş bir görevi arka planda devam ettirir.", "ornek": "bg"},
    {"komut": "fg", "aciklama": "Arka plandaki bir görevi ön plana getirir.", "ornek": "fg"},
    {"komut": "nohup", "aciklama": "Terminal kapansa bile bir programın çalışmaya devam etmesini sağlar.", "ornek": "nohup python script.py &"},
    {"komut": "screen", "aciklama": "Terminalde birden fazla oturumu yönetmeni sağlar.", "ornek": "screen"},
    {"komut": "tmux", "aciklama": "screen'e benzer, gelişmiş terminal oturum yöneticisi.", "ornek": "tmux"},
    {"komut": "ssh", "aciklama": "Başka bir bilgisayara uzaktan güvenli bağlantı kurar.", "ornek": "ssh kullanici@192.168.1.5"},
    {"komut": "scp", "aciklama": "İki bilgisayar arasında güvenli dosya kopyalar.", "ornek": "scp dosya.txt kullanici@sunucu:/klasor"},
    {"komut": "rsync", "aciklama": "Dosyaları verimli şekilde senkronize eder/yedekler.", "ornek": "rsync -av kaynak/ hedef/"},
    {"komut": "git", "aciklama": "Kod geçmişini takip eden versiyon kontrol aracı.", "ornek": "git status"},
    {"komut": "pip", "aciklama": "Python paketlerini kurar ve yönetir.", "ornek": "pip install requests"},
    {"komut": "python3", "aciklama": "Python programlarını çalıştırır.", "ornek": "python3 script.py"},
    {"komut": "dpkg", "aciklama": "Debian tabanlı sistemlerde (.deb) paket kurar/kaldırır.", "ornek": "sudo dpkg -i paket.deb"},
    {"komut": "snap", "aciklama": "Snap paketlerini kurar ve yönetir.", "ornek": "sudo snap install spotify"},
    {"komut": "flatpak", "aciklama": "Flatpak paketlerini kurar ve yönetir.", "ornek": "flatpak install discord"},
    {"komut": "lsusb", "aciklama": "Bağlı USB cihazlarını listeler.", "ornek": "lsusb"},
    {"komut": "lspci", "aciklama": "Bilgisayardaki donanım (kart) bilgilerini listeler.", "ornek": "lspci"},
    {"komut": "dmesg", "aciklama": "Sistem/donanım ile ilgili çekirdek mesajlarını gösterir.", "ornek": "dmesg | less"},
    {"komut": "htop", "aciklama": "top'un renkli ve daha kolay kullanılan hali.", "ornek": "htop"},
    {"komut": "id", "aciklama": "Kullanıcının ID'sini ve grup bilgilerini gösterir.", "ornek": "id"},
    {"komut": "groups", "aciklama": "Bir kullanıcının üye olduğu grupları gösterir.", "ornek": "groups"},
    {"komut": "usermod", "aciklama": "Bir kullanıcının ayarlarını değiştirir (örn. gruba ekleme).", "ornek": "sudo usermod -aG sudo ahmet"},
    {"komut": "deluser", "aciklama": "Sistemden bir kullanıcıyı siler.", "ornek": "sudo deluser ahmet"},
    {"komut": "groupadd", "aciklama": "Yeni bir kullanıcı grubu oluşturur.", "ornek": "sudo groupadd geliştiriciler"},
    {"komut": "env", "aciklama": "Sistemdeki ortam değişkenlerini listeler.", "ornek": "env"},
    {"komut": "export", "aciklama": "Yeni bir ortam değişkeni tanımlar.", "ornek": "export PATH=$PATH:/yeni/yol"},
    {"komut": "type", "aciklama": "Bir komutun ne tür bir şey olduğunu (program/alias) gösterir.", "ornek": "type ls"},
    {"komut": "file", "aciklama": "Bir dosyanın ne tür bir dosya olduğunu söyler.", "ornek": "file resim.png"},
    {"komut": "stat", "aciklama": "Bir dosya hakkında detaylı bilgi (boyut, tarih vs.) gösterir.", "ornek": "stat dosya.txt"},
    {"komut": "tree", "aciklama": "Klasör yapısını ağaç şeklinde görselleştirir.", "ornek": "tree"},
    {"komut": "gzip", "aciklama": "Bir dosyayı sıkıştırır.", "ornek": "gzip dosya.txt"},
    {"komut": "zip", "aciklama": "Dosyaları .zip formatında sıkıştırır.", "ornek": "zip arsiv.zip dosya1.txt dosya2.txt"},
    {"komut": "md5sum", "aciklama": "Bir dosyanın benzersiz doğrulama kodunu (hash) üretir.", "ornek": "md5sum dosya.txt"},
    {"komut": "touch", "aciklama": "Boş, yeni bir dosya oluşturur.", "ornek": "touch notlar.txt"},
    {"komut": "nano", "aciklama": "Basit, kolay kullanılan bir metin düzenleyici açar.", "ornek": "nano notlar.txt"},
    {"komut": "whoami", "aciklama": "Şu an hangi kullanıcı olarak giriş yaptığını gösterir.", "ornek": "whoami"},
    {"komut": "passwd", "aciklama": "Kullanıcı şifresini değiştirmeni sağlar.", "ornek": "passwt"},
    {"komut": "ping", "aciklama": "Bir internet adresine bağlantı olup olmadığını test eder.", "ornek": "ping google.com"},
    {"komut": "ifconfig", "aciklama": "Bilgisayarının ağ (internet) bağlantı bilgilerini gösterir.", "ornek": "ifconfig"},
    {"komut": "ip a", "aciklama": "Ağ arayüzlerini ve IP adresini gösterir (ifconfig'in yeni hali).", "ornek": "ip a"},
    {"komut": "kill", "aciklama": "Çalışan bir programı numarasıyla (PID) zorla kapatır.", "ornek": "kill 1234"},
    {"komut": "ps", "aciklama": "Şu an çalışan programların listesini gösterir.", "ornek": "ps aux"},
    {"komut": "du", "aciklama": "Bir klasörün ne kadar disk alanı kapladığını gösterir.", "ornek": "du -sh klasor_adi"},
    {"komut": "tar", "aciklama": "Dosyaları sıkıştırıp arşivler veya arşivi açar.", "ornek": "tar -xzf dosya.tar.gz"},
    {"komut": "unzip", "aciklama": "Bir .zip dosyasını açar.", "ornek": "unzip dosya.zip"},
    {"komut": "wget", "aciklama": "İnternetten bir dosyayı doğrudan terminalden indirir.", "ornek": "wget https://ornek.com/dosya.zip"},
    {"komut": "curl", "aciklama": "Bir web adresinden veri çeker veya isteği test eder.", "ornek": "curl https://ornek.com"},
    {"komut": "which", "aciklama": "Bir komutun bilgisayarında nerede kurulu olduğunu gösterir.", "ornek": "which python"},
    {"komut": "alias", "aciklama": "Uzun bir komuta kısa bir takma ad verir.", "ornek": "alias gg='git status'"},
    {"komut": "exit", "aciklama": "Terminal oturumunu veya bağlantıyı kapatır.", "ornek": "exit"},
    {"komut": "reboot", "aciklama": "Bilgisayarı yeniden başlatır.", "ornek": "sudo reboot"},
    {"komut": "shutdown", "aciklama": "Bilgisayarı kapatır.", "ornek": "sudo shutdown now"},
    {"komut": "adduser", "aciklama": "Sisteme yeni bir kullanıcı ekler.", "ornek": "sudo adduser ahmet"},
    {"komut": "su", "aciklama": "Başka bir kullanıcıya (genelde root'a) geçiş yapar.", "ornek": "su root"},
    {"komut": "find", "aciklama": "Belirttiğin isimde bir dosyayı sistemde arar.", "ornek": "find / -name notlar.txt"},
    {"komut": "locate", "aciklama": "Dosya adına göre hızlı arama yapar (find'dan hızlı).", "ornek": "locate notlar.txt"},
    {"komut": "ln", "aciklama": "Bir dosyaya kısayol (link) oluşturur.", "ornek": "ln -s hedef.txt kisayol.txt"},
    {"komut": "diff", "aciklama": "İki dosya arasındaki farkları gösterir.", "ornek": "diff dosya1.txt dosya2.txt"},
    {"komut": "head", "aciklama": "Bir dosyanın ilk birkaç satırını gösterir.", "ornek": "head notlar.txt"},
    {"komut": "tail", "aciklama": "Bir dosyanın son birkaç satırını gösterir.", "ornek": "tail notlar.txt"},
    {"komut": "wc", "aciklama": "Bir dosyadaki satır, kelime veya karakter sayısını sayar.", "ornek": "wc -l notlar.txt"},
    {"komut": "date", "aciklama": "Sistemin tarih ve saatini gösterir.", "ornek": "date"},
    {"komut": "uptime", "aciklama": "Bilgisayarın ne kadar süredir açık olduğunu gösterir.", "ornek": "uptime"},
]


html = """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<style>
    * { box-sizing: border-box; }
    body {
        font-family: 'Segoe UI', sans-serif;
        background: #1e1e2e;
        color: #ffffff;
        margin: 0;
        padding: 0;
    }
    .tabs {
        display: flex;
        background: #181825;
        padding: 0 20px;
    }
    .tab {
        padding: 15px 25px;
        cursor: pointer;
        color: #a6adc8;
        border-bottom: 3px solid transparent;
    }
    .tab.active {
        color: #89b4fa;
        border-bottom: 3px solid #89b4fa;
    }
    .content { padding: 30px; }
    .page { display: none; }
    .page.active { display: block; }

    h1 { color: #89b4fa; margin-bottom: 30px; font-size: 22px; }
    .grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }
    .card {
        background: #313244;
        border-radius: 12px;
        padding: 20px;
    }
    .card h3 {
        margin-top: 0;
        color: #cdd6f4;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .value { font-size: 32px; font-weight: bold; color: #89b4fa; }
    .sub { color: #a6adc8; font-size: 13px; margin-top: 5px; }
    .bar-bg { background: #45475a; border-radius: 8px; height: 8px; margin-top: 10px; overflow: hidden; }
    .bar-fill { background: #89b4fa; height: 100%; transition: width 0.3s ease; }

    #search-box {
        width: 100%;
        padding: 14px 18px;
        border-radius: 10px;
        border: none;
        background: #313244;
        color: white;
        font-size: 16px;
        margin-bottom: 20px;
    }
    #search-box:focus { outline: 2px solid #89b4fa; }
    .cmd-card {
        background: #313244;
        border-radius: 10px;
        padding: 16px 20px;
        margin-bottom: 12px;
    }
    .cmd-name {
        font-family: 'Consolas', monospace;
        background: #45475a;
        color: #a6e3a1;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 15px;
    }
    .cmd-aciklama { margin-top: 10px; color: #cdd6f4; line-height: 1.5; }
    .cmd-ornek { margin-top: 8px; color: #a6adc8; font-size: 13px; font-family: 'Consolas', monospace; }
    .empty-msg { color: #a6adc8; text-align: center; margin-top: 40px; }
</style>
</head>
<body>
    <div class="tabs">
        <div class="tab active" onclick="showPage('sistem')">Sistem Paneli</div>
        <div class="tab" onclick="showPage('terminal')">Terminal Rehberi</div>
    </div>

    <div class="content">
        <div id="page-sistem" class="page active">
            <h1>Sistem Paneli</h1>
            <div class="grid">
                <div class="card">
                    <h3>İşlemci (CPU)</h3>
                    <div class="value" id="cpu-val">--%</div>
                    <div class="bar-bg"><div class="bar-fill" id="cpu-bar" style="width:0%"></div></div>
                </div>
                <div class="card">
                    <h3>Bellek (RAM)</h3>
                    <div class="value" id="ram-val">--%</div>
                    <div class="sub" id="ram-sub"></div>
                    <div class="bar-bg"><div class="bar-fill" id="ram-bar" style="width:0%"></div></div>
                </div>
                <div class="card">
                    <h3>Disk</h3>
                    <div class="value" id="disk-val">--%</div>
                    <div class="sub" id="disk-sub"></div>
                    <div class="bar-bg"><div class="bar-fill" id="disk-bar" style="width:0%"></div></div>
                </div>
            </div>
        </div>

        <div id="page-terminal" class="page">
            <h1>Öğretici Terminal Rehberi</h1>
            <input type="text" id="search-box" placeholder="Bir komut yaz (örn: ls, sudo)" oninput="searchCmd()">
            <div id="results"></div>
        </div>
    </div>

<script>
function showPage(name) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.getElementById('page-' + name).classList.add('active');
    event.target.classList.add('active');
}

async function updateStats() {
    const result = await window.pywebview.api.get_system_info();
    const data = JSON.parse(result);
    document.getElementById('cpu-val').innerText = data.cpu_percent + '%';
    document.getElementById('cpu-bar').style.width = data.cpu_percent + '%';
    document.getElementById('ram-val').innerText = data.ram_percent + '%';
    document.getElementById('ram-sub').innerText = data.ram_used_gb + ' / ' + data.ram_total_gb + ' GB';
    document.getElementById('ram-bar').style.width = data.ram_percent + '%';
    document.getElementById('disk-val').innerText = data.disk_percent + '%';
    document.getElementById('disk-sub').innerText = data.disk_used_gb + ' / ' + data.disk_total_gb + ' GB';
    document.getElementById('disk-bar').style.width = data.disk_percent + '%';
}

async function searchCmd() {
    const query = document.getElementById('search-box').value;
    const resultsDiv = document.getElementById('results');
    if (!query.trim()) { resultsDiv.innerHTML = ''; return; }

    const result = await window.pywebview.api.search_commands(query);
    const data = JSON.parse(result);

    if (data.length === 0) {
        resultsDiv.innerHTML = '<div class="empty-msg">Sonuç bulunamadı.</div>';
        return;
    }

    resultsDiv.innerHTML = data.map(c => `
        <div class="cmd-card">
            <span class="cmd-name">${c.komut}</span>
            <div class="cmd-aciklama">${c.aciklama}</div>
            <div class="cmd-ornek">Örnek: ${c.ornek}</div>
        </div>
    `).join('');
}

setInterval(updateStats, 1500);
window.addEventListener('pywebviewready', updateStats);
</script>
</body>
</html>
"""

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('PMCC - Pardus Management Control Center', html=html, js_api=api, width=1000, height=650)
    webview.start()