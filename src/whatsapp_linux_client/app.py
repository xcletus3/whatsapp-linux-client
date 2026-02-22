import os

APP_NAME = "whatsapp-linux-client"
WHATSAPP_URL = "https://web.whatsapp.com"

home = os.path.expanduser("~")
profile_root = os.path.join(home, ".local", "share", APP_NAME)
cache_root   = os.path.join(home, ".cache", APP_NAME)

os.makedirs(profile_root, exist_ok=True)
os.makedirs(cache_root, exist_ok=True)


import sys, subprocess
from PyQt6.QtCore import QUrl, Qt, QTimer
from PyQt6.QtGui import QIcon, QDesktopServices
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineCore import (
    QWebEngineProfile,
    QWebEnginePage,
    QWebEngineDownloadRequest,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView


class WhatsAppPage(QWebEnginePage):
    def __init__(self, profile, parent=None):
        super().__init__(profile, parent)
        self.featurePermissionRequested.connect(self.on_feature_permission)

    def on_feature_permission(self, url, feature):
        if url.host().endswith("whatsapp.com"):
            self.setFeaturePermission(url, feature,
                QWebEnginePage.PermissionPolicy.PermissionGrantedByUser)
        else:
            self.setFeaturePermission(url, feature,
                QWebEnginePage.PermissionPolicy.PermissionDeniedByUser)

    def acceptNavigationRequest(self, url, nav_type, isMainFrame):
        if nav_type == QWebEnginePage.NavigationType.NavigationTypeLinkClicked:
            if not url.host().endswith("whatsapp.com"):
                QDesktopServices.openUrl(url)
                return False
        return super().acceptNavigationRequest(url, nav_type, isMainFrame)

    def createWindow(self, _type):
        page = QWebEnginePage(self.profile(), self)

        def handle_url(url):
            if url.isEmpty():
                return
            if not url.host().endswith("whatsapp.com"):
                QDesktopServices.openUrl(url)
            page.deleteLater()

        page.urlChanged.connect(handle_url)
        return page


def make_profile():
    data_dir = os.path.join(profile_root, "profile")
    cache_dir = cache_root

    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)

    profile = QWebEngineProfile("WhatsAppProfile")
    profile.setPersistentStoragePath(data_dir)
    profile.setCachePath(cache_dir)
    profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.DiskHttpCache)
    profile.setPersistentCookiesPolicy(
        QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
    )
    

    # 💬 System notifications for WhatsApp
    def present_notification(notification):
        app_name = "WhatsApp Linux Client"
        sender = (notification.title() or "WhatsApp").strip()
        message = (notification.message() or "").strip()

        # Try system locations (works for pip + deb installs)
        icon_candidates = [
            "/usr/share/icons/hicolor/256x256/apps/whatsapp-linux-client.png",
            "/usr/local/share/icons/hicolor/256x256/apps/whatsapp-linux-client.png",
            os.path.join(os.path.dirname(__file__), "icons", "whatsapp-linux-client.png"),
            ]


        icon_path = next((p for p in icon_candidates if os.path.exists(p)), None)

        cmd = [
            "notify-send",
            "-a", app_name,
        ]

        if icon_path:
            cmd.extend(["-i", icon_path])

        cmd.extend([
            sender,
            message,
        ])

        subprocess.run(cmd, check=False)



    try:
        profile.setNotificationPresenter(present_notification)
    except Exception as e:
        pass

    chrome_ua = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    )
    profile.setHttpUserAgent(chrome_ua)

    return profile


def setup_downloads(profile, window):
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads", "WhatsApp")
    os.makedirs(downloads_dir, exist_ok=True)

    def on_download(item: QWebEngineDownloadRequest):
        fname = item.suggestedFileName() or "download.bin"
        item.setDownloadDirectory(downloads_dir)
        item.setDownloadFileName(fname)

        def update_title():
            rec = item.receivedBytes()
            tot = item.totalBytes()
            if tot > 0:
                pct = int(rec * 100 / tot)
                window.setWindowTitle(f"WhatsApp – downloading {fname} ({pct}%)")
            else:
                window.setWindowTitle(f"WhatsApp – downloading {fname}…")

        item.receivedBytesChanged.connect(update_title)
        item.totalBytesChanged.connect(update_title)

        def on_state_changed(state):
            if state == QWebEngineDownloadRequest.DownloadState.DownloadCompleted:
                QTimer.singleShot(600, lambda: window.setWindowTitle("WhatsApp"))
            elif state == QWebEngineDownloadRequest.DownloadState.DownloadInterrupted:
                pass

        item.stateChanged.connect(on_state_changed)
        item.accept()

    profile.downloadRequested.connect(on_download)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("WhatsApp Linux Client")

    profile = make_profile()

    view = QWebEngineView()
    page = WhatsAppPage(profile, view)
    view.setPage(page)
    view.setWindowTitle("WhatsApp")

    try:
        here = os.path.dirname(__file__)
        icon_path = os.path.join(here, "icons", "whatsapp-linux-client.png")
        if os.path.exists(icon_path):
            view.setWindowIcon(QIcon(icon_path))
    except Exception:
        pass

    view.resize(1100, 800)
    view.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)

    setup_downloads(profile, view)
    view.load(QUrl(WHATSAPP_URL))
    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
