#!/usr/bin/env bash
# Builds the .deb and the source .tar.gz (sdist), and drops both into
# releases/. dpkg-buildpackage always writes its output to the parent
# directory of the source tree (no flag controls this), so this script
# builds there as usual and then moves the results into releases/.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
parent_dir="$(dirname "$repo_root")"
releases_dir="$repo_root/releases"

cd "$repo_root"
mkdir -p "$releases_dir"

rm -rf build .pybuild dist src/whatsapp_linux_client.egg-info \
       debian/.debhelper debian/whatsapp-linux-client debian/files \
       debian/*.substvars debian/*.debhelper.log debian/*.debhelper \
       debian/debhelper-build-stamp

dpkg-buildpackage -us -uc -b

python3 -m build --sdist --outdir "$releases_dir"

mv -f "$parent_dir"/whatsapp-linux-client_*.deb \
      "$parent_dir"/whatsapp-linux-client_*.buildinfo \
      "$parent_dir"/whatsapp-linux-client_*.changes \
      "$releases_dir"/

rm -rf build .pybuild dist src/whatsapp_linux_client.egg-info \
       debian/.debhelper debian/whatsapp-linux-client debian/files \
       debian/*.substvars debian/*.debhelper.log debian/*.debhelper \
       debian/debhelper-build-stamp

echo "Release artifacts are in: $releases_dir"
ls -la "$releases_dir"
