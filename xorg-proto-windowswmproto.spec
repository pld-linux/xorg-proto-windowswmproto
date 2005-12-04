Summary:	WindowsWM extension headers
Summary(pl):	Nag��wki rozszerzenia WindowsWM
Name:		xorg-proto-windowswmproto
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/windowswmproto-%{version}.tar.bz2
# Source0-md5:	31a784e69f19a5a704b16c6b51ed0ee1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WindowsWM extension headers.

%description -l pl
Nag��wki rozszerzenia WindowsWM.

%package devel
Summary:	WindowsWM extension headers
Summary(pl):	Nag��wki rozszerzenia WindowsWM
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
WindowsWM extension headers.

%description devel -l pl
Nag��wki rozszerzenia WindowsWM.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/windowswmproto.pc
