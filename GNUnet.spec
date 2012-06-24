#
# Conditional build:
%bcond_without	ipv6	# without IPv6 support
#
Summary:	An anonymous distributed secure network
Summary(pl.UTF-8):	Anonimowa, rozproszona, bezpieczna sieć
Name:		GNUnet
Version:	0.6.5
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ovmj.org/GNUnet/download/%{name}-%{version}.tar.bz2
# Source0-md5:	8bca32b55dccdb5bde7bd2b38df9df03
Source1:	gnunet.init
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-ipv6.patch
URL:		http://www.gnu.org/software/GNUnet/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel >= 4.0.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libextractor-devel >= 0.3.10
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	mysql-devel >= 3.23.56
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	tdb-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	gdbm
Requires:	gtk+ >= 1.2
Requires:	libextractor >= 0.3.10
Requires:	openssl >= 0.9.7d
Requires:	rc-scripts
Provides:	group(gnunet)
Provides:	user(gnunet)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gnunethomedir	/var/lib/GNUnet

%description
GNUnet is framework for secure peer-to-peer networking. The primary
application for GNUnet is anonymous file-sharing. GNUnet is part of
the GNU project <http://www.gnu.org/>.

While GNUnet file-sharing provides anonymity for its users, it also
provides accounting to perform better resource allocation.
Contributing users are rewarded with better service. Peers monitor the
behavior of other peers and allocate resources for peers that are
economically trusted. The content encoding makes it hard for peers to
circumvent the reward system.

GNUnet supports multiple transport protocols, currently UDP, TCP and
SMTP. The framework automatically chooses a cheap transport that is
currently available by both peers for any given link. It is possible
to run GNUnet peers behind NAT boxes and almost all firewall
configurations.

This is a beta version. The important features have been implemented
and tested. The security features are in place, but note that
anonymity may be limited due to the small number of active
participants.

For a more detailed description of GNUnet, see our webpages at:
<http://www.gnu.org/software/GNUnet/> and <http://www.ovmj.org/GNUnet/>

Note that this RPM contains only plain directories database frontend;
bdb, gdbm, mysql and tdb frontends are in separate subpackages.

%description -l pl.UTF-8
GNUnet stanowi szkielet bezpiecznej sieci typu peer-to-peer.
Podstawową aplikacją GNUnet jest anonimowe współdzielenie plików.
GNUnet stanowi część projektu GNU (http://www.gnu.org/).

Podczas gdy współdzielenie plików za pomocą GNUnet zapewnia
użytkownikom anonimowość, umożliwia ono również ewidencjonowanie dla
zapewnienia lepszego gospodarowania zasobami. Użytkownicy wnoszący coś
są nagradzani lepszą jakością usługi. Każdy z równorzędnych
użytkowników monitoruje zachowanie pozostałych i przydziela zasoby
użytkownikom, którzy są ekonomicznie wiarygodni. Kodowanie treści
czyni system nagród trudnym do przechytrzenia.

GNUnet wspiera wiele protokołów transportowych, aktualnie: UDP, TCP i
SMTP. Szkielet automatycznie wybiera tanią metodę transportu dostępną
w danej chwili dla obu użytkowników przy dowolnym połączeniu. GNUnet
może działać pomiędzy dwiema maszynami znajdującymi się za NAT i z
prawie wszystkimi konfiguracjami firewalli.

Jest to wersja beta. Najważniejsze funkcje zostały zaimplementowane i
przetestowane. Funkcje zapewniające bezpieczeństwo są na swoim
miejscu, lecz należy zauważyć, że anonimowość może być ograniczona ze
względu na małą liczbę aktywnych uczestników.

Bardziej szczegółowy opis GNUnet można znaleźć na stronie:
<http://www.gnu.org/software/GNUnet/> i <http://www.ovmj.org/GNUnet/>

Należy też zauważyć, że ten pakiet zawiera tylko interfejs bazodanowy
dla zwykłych katalogów; wtyczki obsługujące bazy bdb, gdbm, mysql i
tdb znajdują się w osobnych podpakietach.

%package bdb
Summary:	BerkeleyDB database support for GNUnet
Summary(pl.UTF-8):	Obsługa bazy BerkeleyDB dla GNUnet
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description bdb
This package contains BerkeleyDB database frontend for GNUnet.

%description bdb -l pl.UTF-8
Pakiet ten zawiera interfejs bazy danych BerkeleyDB dla GNUnet.

%package gdbm
Summary:	GDBM database support for GNUnet
Summary(pl.UTF-8):	Obsługa bazy GDBM dla GNUnet
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description gdbm
This package contains GDBM database frontend for GNUnet.

%description gdbm -l pl.UTF-8
Pakiet ten zawiera interfejs bazy danych GDBM dla GNUnet.

%package mysql
Summary:	MySQL database support for GNUnet
Summary(pl.UTF-8):	Obsługa bazy MySQL dla GNUnet
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	mysql-libs >= 3.23.56

%description mysql
This package contains MySQL database frontend for GNUnet.

%description mysql -l pl.UTF-8
Pakiet ten zawiera interfejs bazy danych MySQL dla GNUnet.

%package tdb
Summary:	TDB database support for GNUnet
Summary(pl.UTF-8):	Obsługa bazy TDB dla GNUnet
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description tdb
This package contains TDB database frontend for GNUnet.

%description tdb -l pl.UTF-8
Pakiet ten zawiera interfejs bazy danych TDB dla GNUnet.

%prep
%setup -q
%patch0 -p1
%{?with_ipv6:%patch1 -p1}

%build
%{__gettextize}
%{__libtoolize} --ltdl
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--with-gdbm=/usr \
	--with-mysql=/usr \
	--with-tdb=/usr \
	--with-crypto=/usr \
	%{?with_ipv6:--enable-ipv6}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{skel/.gnunet,/rc.d/init.d} \
	$RPM_BUILD_ROOT%{_gnunethomedir}/{state.sdb,data/{afs,credit,hosts}}

install contrib/gnunet.root $RPM_BUILD_ROOT%{_sysconfdir}/gnunet.conf
install contrib/gnunet.user $RPM_BUILD_ROOT%{_sysconfdir}/skel/.gnunet/gnunet.conf
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gnunet

# these are normal, dynamically linked libraries - there is no -devel, so *.la not needed
rm -f $RPM_BUILD_ROOT%{_libdir}/{libgnunetutil,libgnunet_afs_esed2,libgnunetdht_api}.la \
	$RPM_BUILD_ROOT%{_libdir}/{libgnunetdht_datastore_memory,libgnunetrpc_util}.la \
	$RPM_BUILD_ROOT%{_includedir}/*.h

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 115 gnunet
%useradd -o -u 115 -d /var/lib/GNUnet -s /bin/sh -g gnunet -c "GNUnet daemon" gnunet

%post
/sbin/ldconfig
/sbin/chkconfig --add gnunet
%service gnunet restart "GNUnet"

%preun
if [ "$1" = 0 ]; then
	%service gnunet stop
	/sbin/chkconfig --del gnunet
fi

%postun
/sbin/ldconfig
if [ "$1" = "0" ]; then
	%userremove gnunet
	%groupremove gnunet
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS PLATFORMS README UPDATING
%attr(755,root,root) %{_bindir}/gnunet-chat
%attr(755,root,root) %{_bindir}/gnunet-check
%attr(755,root,root) %{_bindir}/gnunet-convert
%attr(755,root,root) %{_bindir}/gnunet-delete
%attr(755,root,root) %{_bindir}/gnunet-dht-join
%attr(755,root,root) %{_bindir}/gnunet-dht-query
%attr(755,root,root) %{_bindir}/gnunet-directory
%attr(755,root,root) %{_bindir}/gnunet-download
#%attr(755,root,root) %{_bindir}/gnunet-download-manager.scm
%attr(755,root,root) %{_bindir}/gnunet-gtk
%attr(755,root,root) %{_bindir}/gnunet-insert
%attr(755,root,root) %{_bindir}/gnunet-peer-info
%attr(755,root,root) %{_bindir}/gnunet-pseudonym
%attr(755,root,root) %{_bindir}/gnunet-search
%attr(755,root,root) %{_bindir}/gnunet-setup
%attr(755,root,root) %{_bindir}/gnunet-stats
%attr(755,root,root) %{_bindir}/gnunet-tbench
%attr(755,root,root) %{_bindir}/gnunet-testbed
%attr(755,root,root) %{_bindir}/gnunet-tracekit
%attr(755,root,root) %{_bindir}/gnunet-transport-check
%attr(755,root,root) %{_bindir}/gnunet-update
%attr(755,root,root) %{_bindir}/gnunetd

# normal, dynamically linked libraries
%attr(755,root,root) %{_libdir}/libgnunet_afs_esed2.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetdht_api.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetdht_datastore_memory.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetrpc_util.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetutil.so.0.0.0

# ltdlopened plugins - these must have *.la
%attr(755,root,root) %{_libdir}/libgnunetafs_database_directory.so
%{_libdir}/libgnunetafs_database_directory.la
%attr(755,root,root) %{_libdir}/libgnunetafs_protocol.so
%{_libdir}/libgnunetafs_protocol.la
%attr(755,root,root) %{_libdir}/libgnunetchat_protocol.so
%{_libdir}/libgnunetchat_protocol.la
%attr(755,root,root) %{_libdir}/libgnunetdht_protocol.so
%{_libdir}/libgnunetdht_protocol.la
%attr(755,root,root) %{_libdir}/libgnunetrpc_protocol.so
%{_libdir}/libgnunetrpc_protocol.la
%attr(755,root,root) %{_libdir}/libgnunettbench_protocol.so
%{_libdir}/libgnunettbench_protocol.la
%attr(755,root,root) %{_libdir}/libgnunettestbed_protocol.so
%{_libdir}/libgnunettestbed_protocol.la
%attr(755,root,root) %{_libdir}/libgnunettracekit_protocol.so
%{_libdir}/libgnunettracekit_protocol.la
%attr(755,root,root) %{_libdir}/libgnunettransport_http.so
%{_libdir}/libgnunettransport_http.la
%attr(755,root,root) %{_libdir}/libgnunettransport_nat.so
%{_libdir}/libgnunettransport_nat.la
%attr(755,root,root) %{_libdir}/libgnunettransport_smtp.so
%{_libdir}/libgnunettransport_smtp.la
%attr(755,root,root) %{_libdir}/libgnunettransport_tcp.so
%{_libdir}/libgnunettransport_tcp.la
%attr(755,root,root) %{_libdir}/libgnunettransport_udp.so
%{_libdir}/libgnunettransport_udp.la
%if %{with ipv6}
%attr(755,root,root) %{_libdir}/libgnunettransport_tcp6.so
%{_libdir}/libgnunettransport_tcp6.la
%attr(755,root,root) %{_libdir}/libgnunettransport_udp6.so
%{_libdir}/libgnunettransport_udp6.la
%endif

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gnunet.conf
/etc/skel/.gnunet
%attr(754,root,root) /etc/rc.d/init.d/gnunet
%{_mandir}/man1/gnunet-chat.1*
%{_mandir}/man1/gnunet-check.1*
%{_mandir}/man1/gnunet-convert.1*
%{_mandir}/man1/gnunet-delete.1*
%{_mandir}/man1/gnunet-directory.1*
%{_mandir}/man1/gnunet-download-manager.1*
%{_mandir}/man1/gnunet-download.1*
%{_mandir}/man1/gnunet-gtk.1*
%{_mandir}/man1/gnunet-insert.1*
%{_mandir}/man1/gnunet-peer-info.1*
%{_mandir}/man1/gnunet-pseudonym.1*
%{_mandir}/man1/gnunet-search.1*
%{_mandir}/man1/gnunet-stats.1*
%{_mandir}/man1/gnunet-tbench.1*
%{_mandir}/man1/gnunet-testbed.1*
%{_mandir}/man1/gnunet-tracekit.1*
%{_mandir}/man1/gnunet-transport-check.1*
%{_mandir}/man1/gnunet-update.1*
%{_mandir}/man1/gnunetd.1*
%{_mandir}/man5/gnunet.conf.5*
%attr(2770,gnunet,gnunet) %dir %{_gnunethomedir}
%attr(2770,gnunet,gnunet) %dir %{_gnunethomedir}/data
%attr(2770,gnunet,gnunet) %dir %{_gnunethomedir}/data/afs
%attr(2770,gnunet,gnunet) %dir %{_gnunethomedir}/data/credit
%attr(2770,gnunet,gnunet) %dir %{_gnunethomedir}/data/hosts
%attr(2770,gnunet,gnunet) %dir %{_gnunethomedir}/state.sdb

# these (and *.so for them) should be in -devel or /dev/null
#%{_libdir}/libgnunetutil.la
#%{_libdir}/libgnunet_afs_esed2.la
#%{_libdir}/libgnunetdht_api.la
#%{_libdir}/libgnunetdht_datastore_memory.la
#%{_libdir}/libgnunetrpc_util.la

%files bdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnunetafs_database_bdb.so
%{_libdir}/libgnunetafs_database_bdb.la

%files gdbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnunetafs_database_gdbm.so
%{_libdir}/libgnunetafs_database_gdbm.la

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnunetafs_database_mysql.so
%{_libdir}/libgnunetafs_database_mysql.la

%files tdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnunetafs_database_tdb.so
%{_libdir}/libgnunetafs_database_tdb.la
