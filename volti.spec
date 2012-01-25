Name:		volti
Version:	0.2.3
Release:	3
Summary:	GTK+ app for controlling audio volume from system tray/notification area
License:	GPLv3
Group:		Sound
URL:		http://code.google.com/p/volti/
Source0:	http://code.google.com/p/volti/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	python-devel
BuildRequires:  desktop-file-utils

Requires:	pygtk2.0
Requires:	python-gobject
Requires:	python-alsaaudio
Requires:	python-dbus
Requires:	python-xlib

%description
GTK+ application for controlling audio volume from system tray/notification 
area

Features:
* no pulseaudio, gstreamer, phonon etc. only alsa is needed 
* uses external mixer that you can choose, it goes nicely with gnome-alsamixer 
* left click opens volume scale (slider) 
* scroll wheel on tray icon changes volume, increment in percents is 
configurable 
* you can configure middle click to toggle 'mute' or 'show mixer' 
* nice tooltip with card and volume info 
 
%prep
%setup -q 

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-Multimedia-Sound" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc README COPYING ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}-mixer
%{_bindir}/%{name}-remote
%{_datadir}/%{name}/preferences.glade
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/icons
%{_mandir}/man1/*.1*
%{py_sitedir}/*

