Name:		GNUnet
Release:	0.1
Summary:	An anonymous distributed secure network
Summary(pl):	Anonimowa, rozproszona, bezpieczna sieæ
License:	GPL
URL:		http://www.gnu.org/software/GNUnet/
Version:	0.5.4a
Source0:	http://www.ovmj.org/GNUnet/download/%{name}-%{version}.tar.gz
Source1:	gnunet.init
# Source0-md5:	0a22cadab0b33784d0d5344ce975a088
Group:		Applications/Network
######		Unknown group!
Requires:	gtk+ >= 1.2
Requires:	libextractor >= 0.2.3
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libextractor-devel >= 0.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
# Note that you can only build this RPM if the current GNUnet version
# is already installed in /usr. The reason is, that a GNUnet library
# (afsprotocol) is linked against another couple of libraries which
# are NOT found in BuildRoot in the "make install" stage when for some
# odd reason libtool decides to re-link the library :-(. I've spend 6h
# on this one, there does not seem to be a clean solution.  Note that
# without the RPM script foo around it, the build works just fine.

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

Note that this RPM does not build the database frontends for tdb and
mysql (only gdbm, bdb and plain directories are included).

%package mysql
Summary:	MySQL database support for GNUnet
Summary(pl):	Obs³uga bazy MySQL dla GNUnet
Group:		Applications/Network
Requires:	%{name} = %{version}
BuildRequires:	mysql-devel >= 3.23.56

%description mysql
This package contains MySQL database frontend for GNUnet.

#%package tdb
#Summary:	TDB database support for GNUnet
#Summary(pl):	Obs³uga bazy TDB dla GNUnet
#Group:		Applications/Network
#Requires:	%{name} = %{version}

#%description tdb
#This package contains TDB database frontend for GNUnet.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure --with-mysql=/usr --with-tdb=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

rm -f $RPM_BUILD_ROOT/usr/lib/*.a
#rm -f $RPM_BUILD_ROOT/usr/lib/*_tdb.*
rm -f $RPM_BUILD_ROOT/usr/lib/*.a
mkdir -p $RPM_BUILD_ROOT/etc
cp contrib/gnunet.conf.root $RPM_BUILD_ROOT/etc/gnunet.conf
mkdir -p $RPM_BUILD_ROOT/etc/skel/.gnunet/
cp contrib/gnunet.conf $RPM_BUILD_ROOT/etc/skel/.gnunet/
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gnunet
install -d $RPM_BUILD_ROOT%{_gnunethomedir}/data/hosts

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

if [ -n "`id -u gnunet 2>/dev/null`" ]; then
	if [ "`id -u gnunet`" != "89" ]; then
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
if [ -f /var/lock/subsys/gnunet ]; then
	 /etc/rc.d/init.d/gnunet restart >&2
else
	echo "Run \"/etc/rc.d/init.d/gnunet start\" to start GNUnet." >&2
fi

%preun
if [ -f /var/lock/subsys/gnunet ]; then
	/etc/rc.d/init.d/gnunet stop
fi

%postun
/sbin/ldconfig
/usr/sbin/userdel gnunet &> /dev/null
/usr/sbin/groupdel gnunet &> /dev/null

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
%{_libdir}/libgnunetafs_blocks.la
%{_libdir}/libgnunetafs_blocks.so
%{_libdir}/libgnunetafs_blocks.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_blocks.so.0.0.0
%{_libdir}/libgnunetafs_database.la
%{_libdir}/libgnunetafs_database.so
%{_libdir}/libgnunetafs_database.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_database.so.0.0.0
%{_libdir}/libgnunetafs_database_bdb.la
%{_libdir}/libgnunetafs_database_bdb.so
%{_libdir}/libgnunetafs_database_bdb.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_database_bdb.so.0.0.0
#%{_libdir}/libgnunetafs_database_gdbm.la
#%{_libdir}/libgnunetafs_database_gdbm.so
#%{_libdir}/libgnunetafs_database_gdbm.so.0
#%attr(755,root,root) %{_libdir}/libgnunetafs_database_gdbm.so.0.0.0
%{_libdir}/libgnunetafs_database_directory.la
%{_libdir}/libgnunetafs_database_directory.so
%{_libdir}/libgnunetafs_database_directory.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_database_directory.so.0.0.0
%{_libdir}/libgnunetafs_decoding.la
%{_libdir}/libgnunetafs_decoding.so
%{_libdir}/libgnunetafs_decoding.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_decoding.so.0.0.0
%{_libdir}/libgnunetafs_delete.la
%{_libdir}/libgnunetafs_delete.so
%{_libdir}/libgnunetafs_delete.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_delete.so.0.0.0
%{_libdir}/libgnunetafs_encoding.la
%{_libdir}/libgnunetafs_encoding.so
%{_libdir}/libgnunetafs_encoding.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_encoding.so.0.0.0
%{_libdir}/libgnunetafs_policy.la
%{_libdir}/libgnunetafs_policy.so
%{_libdir}/libgnunetafs_policy.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_policy.so.0.0.0
%{_libdir}/libgnunetafs_protocol.la
%{_libdir}/libgnunetafs_protocol.so
%{_libdir}/libgnunetafs_protocol.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_protocol.so.0.0.0
%{_libdir}/libgnunetafs_search.la
%{_libdir}/libgnunetafs_search.so
%{_libdir}/libgnunetafs_search.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_search.so.0.0.0
%{_libdir}/libgnunetafs_util.la
%{_libdir}/libgnunetafs_util.so
%{_libdir}/libgnunetafs_util.so.0
%attr(755,root,root) %{_libdir}/libgnunetafs_util.so.0.0.0
%{_libdir}/libgnunetchat_protocol.la
%{_libdir}/libgnunetchat_protocol.so
%{_libdir}/libgnunetchat_protocol.so.0
%attr(755,root,root) %{_libdir}/libgnunetchat_protocol.so.0.0.0
%{_libdir}/libgnunetcommon.la
%{_libdir}/libgnunetcommon.so
%{_libdir}/libgnunetcommon.so.0
%attr(755,root,root) %{_libdir}/libgnunetcommon.so.0.0.0
%{_libdir}/libgnunettbench_protocol.la
%{_libdir}/libgnunettbench_protocol.so
%{_libdir}/libgnunettbench_protocol.so.0
%attr(755,root,root) %{_libdir}/libgnunettbench_protocol.so.0.0.0
%{_libdir}/libgnunettracekit_protocol.la
%{_libdir}/libgnunettracekit_protocol.so
%{_libdir}/libgnunettracekit_protocol.so.0
%attr(755,root,root) %{_libdir}/libgnunettracekit_protocol.so.0.0.0
%{_libdir}/libgnunettransport_smtp.la
%{_libdir}/libgnunettransport_smtp.so
%{_libdir}/libgnunettransport_smtp.so.0
%attr(755,root,root) %{_libdir}/libgnunettransport_smtp.so.0.0.0
%{_libdir}/libgnunettransport_tcp.la
%{_libdir}/libgnunettransport_tcp.so
%{_libdir}/libgnunettransport_tcp.so.0
%attr(755,root,root) %{_libdir}/libgnunettransport_tcp.so.0.0.0
%{_libdir}/libgnunettransport_udp.la
%{_libdir}/libgnunettransport_udp.so
%{_libdir}/libgnunettransport_udp.so.0
%attr(755,root,root) %{_libdir}/libgnunettransport_udp.so.0.0.0
%{_libdir}/libgnunetutil.la
%{_libdir}/libgnunetutil.so
%{_libdir}/libgnunetutil.so.0
%attr(755,root,root) %{_libdir}/libgnunetutil.so.0.0.0
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/gnunet.conf
%{_sysconfdir}/skel/.gnunet
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/gnunetd
%doc %{_mandir}/man1/gnunetd.1.gz
%doc %{_mandir}/man1/gnunet-convert.1.gz
%doc %{_mandir}/man1/gnunet-gtk.1.gz
%doc %{_mandir}/man1/gnunet-insert-multi.1.gz
%doc %{_mandir}/man1/gnunet-download.1.gz
%doc %{_mandir}/man1/gnunet-delete.1.gz
%doc %{_mandir}/man1/gnunet-insert.1.gz
%doc %{_mandir}/man1/gnunet-search.1.gz
%doc %{_mandir}/man1/gnunet-check.1.gz
%doc %{_mandir}/man1/gnunet-transport-check.1.gz
%doc %{_mandir}/man1/gnunet-chat.1.gz
%doc %{_mandir}/man5/gnunet.conf.5.gz
%doc %{_mandir}/man1/gnunet-tbench.1.gz
%doc %{_mandir}/man1/gnunet-tracekit.1.gz
%doc %{_mandir}/man1/gnunet-stats.1.gz
%doc %{_mandir}/man1/gnunet-peer-info.1.gz
%attr(750,gnunet,gnunet) %dir %{_gnunethomedir}
%attr(750,gnunet,gnunet) %dir %{_gnunethomedir}/data/hosts

%files mysql
%defattr(644,root,root,755)
%{_libdir}/libgnunetafs_database_mysql.*

#%files tdb
#%defattr(644,root,root,755)
#%{_libdir}/libgnunetafs_database_tdb.*
