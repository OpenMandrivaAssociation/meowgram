# Fix for broken debug
%define _empty_manifest_terminate_build 0

%define oname Meowgram
%define gitdate 20210618

Summary:  Telegram client written in GTK & Python
Name:     meowgram
Version:  0.1.0
Release:  0.%{gitdate}.0
License:  GPLv3.0
Group:    Networking/Instant messaging
Url:      https://github.com/ExposedCat/Meowgram
Source0:  https://github.com/ExposedCat/Meowgram/archive/refs/heads/main/%{oname}-main.tar.gz

BuildRequires:  appstream-util
BuildRequires:  meson
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libadwaita-1)

# For non GTK/GNOME deskops installation.
Requires: gtk+3.0
Requires: gtk+4.0
Requires: %{_lib}adwaita1_0

Requires: python3dist(bleach)
Requires: python3dist(telethon)

%description
Meowgram is a Telegram client written in GTK and Python.
Meowgram = Meow + Gram
Meow - Talking cats sound. It's a symbol of unique and user friendly UI of client, just like a cute kitten.
Gram - Part of platform name: Telegram. It says about which messanger is client made for.

%prep
%autosetup -n %{oname}-main -p1

%build
%meson

%meson_build

%install
%meson_install

%files
%{_bindir}/meowgram
%{_datadir}/applications/com.github.ExposedCat.Meowgram.desktop
%{_datadir}/appdata/com.github.ExposedCat.Meowgram.appdata.xml
%{_datadir}/glib-2.0/schemas/com.github.ExposedCat.Meowgram.gschema.xml
%{_datadir}/meowgram/meowgram*
%{_iconsdir}/hicolor/scalable/apps/com.github.ExposedCat.Meowgram.svg
%{_iconsdir}/hicolor/symbolic/apps/com.github.ExposedCat.Meowgram-symbolic.svg
