Summary:	Portable UDP networking library
Summary(pl.UTF-8):	Przenośna biblioteka dla UDP
Name:		enet
Version:	1.3.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://enet.bespin.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	d31adbd50924fe39aab3c23308f58959
URL:		http://enet.bespin.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ENet's purpose is to provide a relatively thin, simple and robust
network communication layer on top of UDP (User Datagram Protocol).
The primary feature it provides is optional reliable, in-order
delivery of packets.

%description -l pl.UTF-8
Celem ENeta jest dostarczenie relatywnie lekkiej, prostej oraz
wydajnej sieciowej warstwy komunikacyjnej dla UDP (Datagramowego
Protokołu Użytkownika). Podstawową jego zaletą jest niezawodne
dostarczanie pakietów w odpowiedniej kolejności.

%package devel
Summary:	Header files for enet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki enet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for enet library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki enet.

%package static
Summary:	Static enet library
Summary(pl.UTF-8):	Statyczna biblioteka enet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static enet library.

%description static -l pl.UTF-8
Statyczna biblioteka enet.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog docs *.txt
%attr(755,root,root) %{_libdir}/libenet.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libenet.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libenet.so
%dir %{_includedir}/enet/
%{_includedir}/enet/*.h
%{_libdir}/libenet.la
%{_pkgconfigdir}/libenet.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
