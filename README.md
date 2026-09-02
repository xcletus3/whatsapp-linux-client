# WhatsApp Linux Client 🐧

A lightweight, open-source **WhatsApp Web desktop client for Linux**, built using **PyQt6**.
No Electron, no browser tab — just a native Linux application.

> ⚠️ **Disclaimer**
> This is **not an official WhatsApp application**.
> It is a desktop wrapper around **WhatsApp Web** and is not affiliated with, endorsed by, or supported by Meta (WhatsApp).

---

## ✨ Features

- 🔐 **Persistent login** — scan the QR code once, your session is stored locally so you don't need to rescan every time.
- 🌐 **External links open in your default browser** — clean separation between chats and web content.
- 📥 **Automatic media downloads** — saved to `~/Downloads/WhatsApp/`.
- 🔔 **Native system notifications** — sender name as title, message as body, custom app icon.
- 🐧 **Linux-native & lightweight** — built with PyQt6, no Electron, lower memory usage.
- 🎨 **Desktop integration** — application menu entry, custom app icon, proper window behavior.

---

## 🧩 Installation

### 📦 Option 1: Install via .deb (recommended)

Download the latest `.deb` from the [Releases](https://github.com/xcletus3/whatsapp-linux-client/releases) page and install it:

```
sudo apt install ./whatsapp-linux-client_<version>_all.deb
```

This installs the app, its PyQt6/WebEngine dependencies (via `apt`), the `whatsapp-linux-client` command, and full desktop integration (menu entry, icon, notifications) — nothing else to configure.

### 🛠 Option 2: Install from source (development)

```
git clone https://github.com/xcletus3/whatsapp-linux-client.git
cd whatsapp-linux-client
python3 -m venv venv
source venv/bin/activate
pip install -e .
whatsapp-linux-client
```

This gives you a working app inside the virtual environment, but **no menu entry/icon** — a venv install doesn't register anything in the system's application menu. To get that too, register a user-level desktop entry once (no root needed):

```
mkdir -p ~/.local/share/applications ~/.local/share/icons/hicolor/256x256/apps
cp src/whatsapp_linux_client/icons/whatsapp-linux-client.png ~/.local/share/icons/hicolor/256x256/apps/
sed "s|Exec=whatsapp-linux-client|Exec=$(realpath venv/bin/whatsapp-linux-client)|" \
    src/whatsapp_linux_client/data/whatsapp-linux-client.desktop \
    > ~/.local/share/applications/whatsapp-linux-client.desktop
update-desktop-database ~/.local/share/applications
```

### 🏗 Building the .deb yourself

Packaging lives in [`debian/`](debian/). With `debhelper`, `dh-python` and `pybuild-plugin-pyproject` installed:

```
sudo apt install debhelper dh-python pybuild-plugin-pyproject python3-all python3-setuptools python3-pip build-essential
dpkg-buildpackage -us -uc -b
```

The built `.deb` is written one directory above the source tree.

---

## 🖥️ System Requirements

- Linux (tested on Debian 13 / GNOME and XFCE)
- Python ≥ 3.9
- PyQt6 and PyQt6-WebEngine (installed automatically via `apt` with the `.deb`)
- A desktop notification service (e.g. `xfce4-notifyd`, GNOME's built-in notifications)

## ⚠️ Known Limitations

- This application depends entirely on WhatsApp Web — if WhatsApp Web changes or becomes unavailable, the app may stop working.

## 🔐 Privacy & Security

- All data is stored locally on your machine.
- No analytics, telemetry, or tracking.
- No credentials are collected or transmitted by this application.
- Authentication happens directly through WhatsApp Web.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

Cletus Xavier — Open-source Linux enthusiast

## ⭐ Support & Contributions

If you find this project useful, star the repository, report bugs/issues, or suggest features. Contributions are welcome.
