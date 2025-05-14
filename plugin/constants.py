from __future__ import annotations

import re

import sublime

assert __package__

PACKAGE_NAME = __package__.partition(".")[0]

PLATFORM_ARCH = f"{sublime.platform()}_{sublime.arch()}"

SERVER_VERSION = ""
if m := re.match(r"^ty==(.+)", sublime.load_resource(f"Packages/{PACKAGE_NAME}/requirements.txt"), re.MULTILINE):
    SERVER_VERSION = m.group(1)

# map pypi version => github version
#     0.0.1a1      => 0.0.1-alpha.1
SERVER_VERSION = re.sub(r"(\d+\.\d+\.\d+)a(?=\d)", r"\1-alpha.", SERVER_VERSION)
SERVER_VERSION = re.sub(r"(\d+\.\d+\.\d+)b(?=\d)", r"\1-beta.", SERVER_VERSION)
SERVER_VERSION = re.sub(r"(\d+\.\d+\.\d+)rc(?=\d)", r"\1-rc.", SERVER_VERSION)

DOWNLOAD_TARBALL_NAMES = {
    "linux_arm64": "ty-aarch64-unknown-linux-gnu.tar.gz",
    "linux_x64": "ty-x86_64-unknown-linux-gnu.tar.gz",
    "osx_arm64": "ty-aarch64-apple-darwin.tar.gz",
    "osx_x64": "ty-x86_64-apple-darwin.tar.gz",
    "windows_x64": "ty-x86_64-pc-windows-msvc.zip",
    "windows_x86": "ty-i686-pc-windows-msvc.zip",
}
"""`platform_arch`-specific tarball names for the ty language server."""
DOWNLOAD_TARBALL_NAME = DOWNLOAD_TARBALL_NAMES[PLATFORM_ARCH]

DOWNLOAD_TARBALL_BIN_PATHS = {
    "linux_arm64": "ty-aarch64-unknown-linux-gnu/ty",
    "linux_x64": "ty-x86_64-unknown-linux-gnu/ty",
    "osx_arm64": "ty-aarch64-apple-darwin/ty",
    "osx_x64": "ty-x86_64-apple-darwin/ty",
    "windows_x64": "ty.exe",
    "windows_x86": "ty.exe",
}
"""`platform_arch`-specific server executable relative path in the tarball."""
DOWNLOAD_TARBALL_BIN_PATH = DOWNLOAD_TARBALL_BIN_PATHS[PLATFORM_ARCH]

DOWNLOAD_URL_TEMPLATE = "https://github.com/astral-sh/ty/releases/download/{version}/{tarball_name}"
SERVER_DOWNLOAD_URL = DOWNLOAD_URL_TEMPLATE.format(version=SERVER_VERSION, tarball_name=DOWNLOAD_TARBALL_NAME)
SERVER_DOWNLOAD_HASH_URL = f"{SERVER_DOWNLOAD_URL}.sha256"
