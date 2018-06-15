#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : portaudio
Version  : 190600.20161030
Release  : 6
URL      : http://www.portaudio.com/archives/pa_stable_v190600_20161030.tgz
Source0  : http://www.portaudio.com/archives/pa_stable_v190600_20161030.tgz
Summary  : Portable audio I/O
Group    : Development/Tools
License  : MIT
Requires: portaudio-lib
BuildRequires : alsa-lib-dev
BuildRequires : cmake

BuildRequires : scons

%description


%package dev
Summary: dev components for the portaudio package.
Group: Development
Requires: portaudio-lib
Provides: portaudio-devel

%description dev
dev components for the portaudio package.


%package lib
Summary: lib components for the portaudio package.
Group: Libraries

%description lib
lib components for the portaudio package.


%prep
%setup -q -n portaudio

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1508790599
%reconfigure --disable-static --without-jack \
--without-oss
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1508790599
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libportaudio.so
/usr/lib64/pkgconfig/portaudio-2.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libportaudio.so.2
/usr/lib64/libportaudio.so.2.0.0
