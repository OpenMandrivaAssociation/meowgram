%define oname Meowgram

Summary:  Telegram client written in GTK & Python
Name:     meowgram
Version:  0.1.0
Release:  0
License:  GPLv3.0
Group:		Networking/Instant messaging
Url:      https://github.com/ExposedCat/Meowgram
Source0:  https://github.com/ExposedCat/Meowgram/archive/refs/heads/main/%{oname}-main.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(python)
#TBC

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
