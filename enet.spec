#
# TODO: pl summary and desc
#
Summary:	Portable UDP networking library
Name:		enet
Version:	1.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://enet.bespin.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	e0d9f468d8c6f6bfd07083b3b40f5e69
URL:		http://enet.bespin.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ENet's purpose is to provide a relatively thin, simple and robust
network communication layer on top of UDP (User Datagram Protocol).
The primary feature it provides is optional reliable, in-order
delivery of packets.

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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

# generate shared library by hand (not implemented in Makefile)
%{__cxx} %{rpmldflags} %{rpmcflags} -shared host.o list.o callbacks.o packet.o peer.o protocol.o unix.o win32.o -o libenet.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install libenet.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog docs *.txt
%attr(755,root,root) %{_libdir}/libenet.so

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/enet/
%{_includedir}/enet/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
