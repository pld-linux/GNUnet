Summary:	An anonymous distributed secure network
Summary(pl):	Anonimowa, rozproszona, bezpieczna sieæ
Name:		GNUnet
Version:	0.5.4a
Release:	0.1
Group:		Applications/Networking
License:	GPL
Source0:	http://www.ovmj.org/GNUnet/download/%{name}-%{version}.tar.gz
# Source0-md5:	0a22cadab0b33784d0d5344ce975a088
Source1:	gnunet.init
Patch0:		%{name}-nolibs.patch
URL:		http://www.gnu.org/software/GNUnet/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	gdbm-devel
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libextractor-devel >= 0.2.3
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	mysql-devel >= 3.23.56
BuildRequires:	openssl-devel >= 0.9.5
BuildRequires:	tdb-devel
PreReq:		rc-scripts
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Requires(post,preun):	/sbin/chkconfig
Requires(post,postun):	/sbin/ldconfig
Requires:	gdbm
Requires:	gtk+ >= 1.2
Requires:	libextractor >= 0.2.3
Requires:	openssl >= 0.9.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_gnunethomedir	/var/lib/GNUnet

%description
GNUnet is framework for secure peer-to-peer networking. The primary
application for GNUnet is anonymous file-sharing. GNUnet is part of
the GNU project (http://www.gnu.org/).

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

http://www.gnu.org/software/GNUnet/ and http://www.ovmj.org/GNUnet/

Note that this RPM contains only plain directories database frontend;
bdb, gdbm, mysql and tdb frontends are in separate subpackages.

%description -l pl
GNUnet stanowi szkielet bezpiecznej sieci typu peer-to-peer.
Podstawow± aplikacj± GNUnet jest anonimowe wspó³dzielenie plików.
GNUnet stanowi czê¶æ projektu GNU (http://www.gnu.org/).

Podczas gdy wspó³dzielenie plików za pomoc± GNUnet zapewnia
u¿ytkownikom anonimowo¶æ, umo¿liwia ono równie¿ ewidencjonowanie dla
zapewnienia lepszego gospodarowania zasobami. U¿ytkownicy wnosz±cy
co¶ s± nagradzani lepsz± jako¶ci± us³ugi. Ka¿dy z równorzêdnych
u¿ytkowników monitoruje zachowanie pozosta³ych i przydziela zasoby
u¿ytkownikom, którzy s± ekonomicznie wiarygodni. Kodowanie tre¶ci
czyni system nagród trudnym do przechytrzenia.

GNUnet wspiera wiele protoko³ów transportowych, aktualnie: UDP, TCP i
SMTP. Szkielet automatycznie wybiera tani± metodê transportu dostêpn±
w danej chwili dla obu u¿ytkowników przy dowolnym po³±czeniu. GNUnet
mo¿e dzia³aæ pomiêdzy dwoma maszynami znajduj±cymi siê za NAT i z
prawie wszystkimi konfiguracjami firewalli.

Jest to wersja beta. Najwa¿niejsze funkcje zosta³y zaimplementowane i
przetestowane. Funkcje zapewniaj±ce bezpieczeñstwo s± na swoim
miejscu, lecz nale¿y zauwa¿yæ, ¿e anonimowo¶æ mo¿e byæ ograniczona ze
wzglêdu na ma³± liczbê aktywnych uczestników.

Bardziej szczegó³owy opis GNUnet mo¿na znale¼æ na stronie:

http://www.gnu.org/software/GNUnet/ and http://www.ovmj.org/GNUnet/

Nale¿y te¿ zauwa¿yæ, ¿e ten pakiet zawiera tylko interfejs bazodanowy
dla zwyk³ych katalogów; wtyczki obs³uguj±ce bazy bdb, gdbm, mysql i
tdb znajduj± siê w osobnych podpakietach.

%package bdb
Summary:	BerkeleyDB database support for GNUnet
Summary(pl):	Obs³uga bazy BerkeleyDB dla GNUnet
Group:		Applications/Network
Requires:	%{name} = %{version}

%description bdb
This package contains BerkeleyDB database frontend for GNUnet.

%description bdb -l pl
Pakiet ten zawiera interfejs bazy danych BerkeleyDB dla GNUnet.

%package gdbm
Summary:	GDBM database support for GNUnet
Summary(pl):	Obs³uga bazy GDBM dla GNUnet
Group:		Applications/Network
Requires:	%{name} = %{version}

%description gdbm
This package contains GDBM database frontend for GNUnet.

%description gdbm -l pl
Pakiet ten zawiera interfejs bazy danych GDBM dla GNUnet.

%package mysql
Summary:	MySQL database support for GNUnet
Summary(pl):	Obs³uga bazy MySQL dla GNUnet
Group:		Applications/Network
Requires:	%{name} = %{version}
Requires:	mysql-libs >= 3.23.56

%description mysql
This package contains MySQL database frontend for GNUnet.

%description mysql -l pl
Pakiet ten zawiera interfejs bazy danych MySQL dla GNUnet.

%package tdb
Summary:	TDB database support for GNUnet
Summary(pl):	Obs³uga bazy TDB dla GNUnet
Group:		Applications/Network
Requires:	%{name} = %{version}

%description tdb
This package contains TDB database frontend for GNUnet.

%description tdb -l pl
Pakiet ten zawiera interfejs bazy danych TDB dla GNUnet.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--with-gdbm=/usr \
	--with-mysql=/usr \
	--with-tdb=/usr \
	--with-crypto=/usr
# no --enable-ipv6  -- some files missing

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D contrib/gnunet.conf.root $RPM_BUILD_ROOT%{_sysconfdir}/gnunet.conf
install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel/.gnunet
install contrib/gnunet.conf $RPM_BUILD_ROOT%{_sysconfdir}/skel/.gnunet
install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gnunet
install -d $RPM_BUILD_ROOT%{_gnunethomedir}/data/hosts
install -d $RPM_BUILD_ROOT%{_gnunethomedir}/afs

# these are normal, dynamically linked libraries - there is no -devel, so *.la not needed
rm -f $RPM_BUILD_ROOT%{_libdir}/libgnunetafs_{blocks,database,decoding,delete,encoding,policy,search,util}.la \
	$RPM_BUILD_ROOT%{_libdir}/libgnunet{common,util}.la

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid gnunet`" ]; then
	if [ "`getgid gnunet`" != "115" ]; then
		echo "Error: group gnunet doesn't have gid=115. Correct this before installing GNUnet." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 115 -r -f gnunet
fi
if [ -n "`id -u gnunet 2>/dev/null`" ]; then
	if [ "`id -u gnunet`" != "115" ]; then
		echo "Error: user gnunet doesn't have uid=115. Correct this before installing GNUnet." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -o -r -u 115 \
		-d /var/lib/GNUnet -s /bin/sh -g gnunet \
		-c "GNUnet daemon" gnunet 1>&2
fi

%post
/sbin/ldconfig
/sbin/chkconfig --add gnunet
if [ -f /var/lock/subsys/gnunet ]; then
	 /etc/rc.d/init.d/gnunet restart >&2
else
	echo "Run \"/etc/rc.d/init.d/gnunet start\" to start GNUnet." >&2
fi


%preun
if [ -f /var/lock/subsys/gnunet ]; then
	/etc/rc.d/init.d/gnunet stop
fi
/sbin/chkconfig --del gnunet

%postun
/sbin/ldconfig
if [ "$1" = "0" ]; then
	/usr/sbin/userdel gnunet 2>/dev/null
	/usr/sbin/groupdel gnunet 2>/dev/null
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnunetd
%attr(755,root,root) %{_bindir}/gnunet-insert
%attr(755,root,root) %{_bindir}/gnunet-search
%attr(755,root,root) %{_bindir}/gnunet-download
%attr(755,root,root) %{_bindir}/gnunet-insert-multi
%attr(755,root,root) %{_bindir}/gnunet-gtk
%attr(755,root,root) %{_bindir}/gnunet-chat
%attr(755,root,root) %{_bindir}/gnunet-delete
%attr(755,root,root) %{_bindir}/gnunet-stats
%attr(755,root,root) %{_bindir}/gnunet-check
%attr(755,root,root) %{_bindir}/gnunet-convert
%attr(755,root,root) %{_bindir}/gnunet-transport-check
%attr(755,root,root) %{_bindir}/gnunet-tbench
%attr(755,root,root) %{_bindir}/gnunet-peer-info
%attr(755,root,root) %{_bindir}/gnunet-tracekit

# normal, dynamically linked libraries
%attr(755,root,root) %{_libdir}/libgnunetafs_blocks.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetafs_database.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetafs_decoding.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetafs_delete.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetafs_encoding.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetafs_policy.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetafs_search.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetafs_util.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetcommon.so.0.0.0
%attr(755,root,root) %{_libdir}/libgnunetutil.so.0.0.0

# ltdlopened plugins - these must have *.la
%attr(755,root,root) %{_libdir}/libextractor_lower.so.0.0.0
%{_libdir}/libextractor_lower.la
%attr(755,root,root) %{_libdir}/libgnunetafs_database_directory.so.0.0.0
%{_libdir}/libgnunetafs_database_directory.la
%attr(755,root,root) %{_libdir}/libgnunetafs_protocol.so.0.0.0
%{_libdir}/libgnunetafs_protocol.la
%attr(755,root,root) %{_libdir}/libgnunetchat_protocol.so.0.0.0
%{_libdir}/libgnunetchat_protocol.la
%attr(755,root,root) %{_libdir}/libgnunettbench_protocol.so.0.0.0
%{_libdir}/libgnunettbench_protocol.la
%attr(755,root,root) %{_libdir}/libgnunettracekit_protocol.so.0.0.0
%{_libdir}/libgnunettracekit_protocol.la
%attr(755,root,root) %{_libdir}/libgnunettransport_smtp.so.0.0.0
%{_libdir}/libgnunettransport_smtp.la
%attr(755,root,root) %{_libdir}/libgnunettransport_http.so.0.0.0
%{_libdir}/libgnunettransport_http.la
%attr(755,root,root) %{_libdir}/libgnunettransport_tcp.so.0.0.0
%{_libdir}/libgnunettransport_tcp.la
#%attr(755,root,root) %{_libdir}/libgnunettransport_tcp6.so.0.0.0
#%{_libdir}/libgnunettransport_tcp6.la
%attr(755,root,root) %{_libdir}/libgnunettransport_udp.so.0.0.0
%{_libdir}/libgnunettransport_udp.la
#%attr(755,root,root) %{_libdir}/libgnunettransport_udp6.so.0.0.0
#%{_libdir}/libgnunettransport_udp6.la

%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/gnunet.conf
%{_sysconfdir}/skel/.gnunet
%attr(754,root,root) /etc/rc.d/init.d/gnunet
%{_mandir}/man1/gnunetd.1*
%{_mandir}/man1/gnunet-convert.1*
%{_mandir}/man1/gnunet-gtk.1*
%{_mandir}/man1/gnunet-insert-multi.1*
%{_mandir}/man1/gnunet-download.1*
%{_mandir}/man1/gnunet-delete.1*
%{_mandir}/man1/gnunet-insert.1*
%{_mandir}/man1/gnunet-search.1*
%{_mandir}/man1/gnunet-check.1*
%{_mandir}/man1/gnunet-transport-check.1*
%{_mandir}/man1/gnunet-chat.1*
%{_mandir}/man5/gnunet.conf.5*
%{_mandir}/man1/gnunet-tbench.1*
%{_mandir}/man1/gnunet-tracekit.1*
%{_mandir}/man1/gnunet-stats.1*
%{_mandir}/man1/gnunet-peer-info.1*
%attr(2770,gnunet,gnunet) %dir %{_gnunethomedir}
%attr(2770,gnunet,gnunet) %dir %{_gnunethomedir}/afs
%attr(2770,gnunet,gnunet) %dir %{_gnunethomedir}/data
%attr(2770,gnunet,gnunet) %dir %{_gnunethomedir}/data/hosts

# these (and *.so for them) should be in -devel or /dev/null
#%{_libdir}/libgnunetafs_blocks.la
#%{_libdir}/libgnunetafs_database.la
#%{_libdir}/libgnunetafs_decoding.la
#%{_libdir}/libgnunetafs_delete.la
#%{_libdir}/libgnunetafs_encoding.la
#%{_libdir}/libgnunetafs_policy.la
#%{_libdir}/libgnunetafs_search.la
#%{_libdir}/libgnunetafs_util.la
#%{_libdir}/libgnunetcommon.la
#%{_libdir}/libgnunetutil.la

%files bdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnunetafs_database_bdb.so.0.0.0
%{_libdir}/libgnunetafs_database_bdb.la

%files gdbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnunetafs_database_gdbm.so.0.0.0
%{_libdir}/libgnunetafs_database_gdbm.la

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnunetafs_database_mysql.so.0.0.0
%{_libdir}/libgnunetafs_database_mysql.la

%files tdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnunetafs_database_tdb.so.0.0.0
%{_libdir}/libgnunetafs_database_tdb.la
