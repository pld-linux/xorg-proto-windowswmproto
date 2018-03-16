# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	WindowsWM extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia WindowsWM
Name:		xorg-proto-windowswmproto
Version:	1.0.4
Release:	2.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/windowswmproto-%{version}.tar.bz2
# Source0-md5:	e74b2ff3172a6117f2a62b655ef99064
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WindowsWM extension headers provide the definition of the WindowsWM
extension to the X11 protocol, used for coordination between an X11
server and the Microsoft Windows native window manager.

%description -l pl.UTF-8
Nagłówki rozszerzenia WindowsWM udostępniają definicję rozszerzenia
WindowsWM do protokołu X11, służącego do współpracy między serwerem
X11 a natywnym zarządcą okien Microsoft Windows.

%package devel
Summary:	WindowsWM extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia WindowsWM
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
WindowsWM extension headers provide the definition of the WindowsWM
extension to the X11 protocol, used for coordination between an X11
server and the Microsoft Windows native window manager.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia WindowsWM udostępniają definicję rozszerzenia
WindowsWM do protokołu X11, służącego do współpracy między serwerem
X11 a natywnym zarządcą okien Microsoft Windows.

%prep
%setup -q -n windowswmproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_includedir}/X11/extensions/windowswm*.h
%{_pkgconfigdir}/windowswmproto.pc
