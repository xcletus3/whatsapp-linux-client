# WhatsApp Linux Client 🐧

A lightweight, open-source **WhatsApp Web desktop client for Linux**, built using **PyQt6**.  
No Electron, no browser tab — just a native Linux application.

> ⚠️ **Disclaimer**  
> This is **not an official WhatsApp application**.  
> It is a desktop wrapper around **WhatsApp Web** and is not affiliated with, endorsed by, or supported by Meta (WhatsApp).

---

## ✨ Features

- 🔐 **Persistent login**  
  Scan the QR code once — your session is stored locally, so you don’t need to rescan every time.

- 🌐 **External links open in your default browser**  
  Clean separation between chats and web content.

- 📥 **Automatic media downloads**  
  All downloaded files are saved to: `~/Downloads/WhatsApp/`


- 🔔 **Native system notifications**  
- Sender name as notification title  
- Message content as body  
- Custom application icon  

- 🐧 **Linux-native & lightweight**  
Built with PyQt6 — **no Electron**, lower memory usage.

- 🎨 **Desktop integration**
- Application menu entry
- Custom app icon
- Proper window behavior
- System notification support

---

## 🧩 Installation

### 📦 Option 1: Install via .deb (recommended for Linux users)
Download the latest .deb from the Releases page and install:

    sudo apt install ./whatsapp-linux-client_1.0.0_all.deb

This method provides full desktop integration (icon, menu entry, notifications).

### 🐍 Option 2: Install from wheel (manual / advanced)

    python3 -m pip install --break-system-packages whatsapp_linux_client-1.0.0-py3-none-any.whl

⚠️ Note: This method may not provide full desktop integration (menu entry, icons, notifications). Recommended mainly for testing or manual setups.


### 🛠 Option 3: Install from source (development)

    git clone https://github.com/xcletus3/whatsapp-linux-client.git
    cd whatsapp-linux-client
    python3 -m venv venv
    source venv/bin/activate
    pip install -e .

🚀 Running the application
After installation, launch the app from:
your application menu, or the terminal:

    whatsapp-linux-client

## 🐧 Platform Note
This application is designed primarily for Linux.
While the wheel package may install on other platforms, full functionality and system integration are only guaranteed on Linux.

### 🖥️ System Requirements

    Linux (tested on Debian / XFCE)

    Python ≥ 3.9

    PyQt6

    PyQt6-WebEngine

    A desktop notification service (e.g. xfce4-notifyd, notify-osd)

### ⚠️ Known Limitations

    This application depends entirely on WhatsApp Web

    If WhatsApp Web changes or becomes unavailable, the app may stop working

    Voice and video calls are not supported (WhatsApp Web limitation)

### 🔐 Privacy & Security

    All data is stored locally on your machine

    No analytics, telemetry, or tracking

    No credentials are collected or transmitted by this application

    Authentication happens directly through WhatsApp Web

### 📜 License

    This project is licensed under the MIT License.
    See the LICENSE file for details.

### 👤 Author

    Cletus Xavier
    Open-source Linux enthusiast

### ⭐ Support & Contributions

    If you find this project useful:

        ⭐ Star the repository

        🐛 Report bugs or issues

        💡 Suggest features or improvements

### Contributions are welcome.
