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


html = """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<style>
    body {
        font-family: 'Segoe UI', sans-serif;
        background: #1e1e2e;
        color: #ffffff;
        margin: 0;
        padding: 30px;
    }
    h1 {
        color: #89b4fa;
        margin-bottom: 30px;
    }
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
    .value {
        font-size: 32px;
        font-weight: bold;
        color: #89b4fa;
    }
    .sub {
        color: #a6adc8;
        font-size: 13px;
        margin-top: 5px;
    }
    .bar-bg {
        background: #45475a;
        border-radius: 8px;
        height: 8px;
        margin-top: 10px;
        overflow: hidden;
    }
    .bar-fill {
        background: #89b4fa;
        height: 100%;
        transition: width 0.3s ease;
    }
</style>
</head>
<body>
    <h1>PMCC - Sistem Paneli</h1>
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

<script>
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

setInterval(updateStats, 1500);
window.addEventListener('pywebviewready', updateStats);
</script>
</body>
</html>
"""

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('PMCC - Sistem Paneli', html=html, js_api=api, width=900, height=600)
    webview.start()