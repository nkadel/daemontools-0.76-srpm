Summary:	Dan Bernstiens Daemon manager
Name:		daemontools
Version:	0.76
Release:	0.2%{?dist}
License:	Public Domain
Group:		Applications/System
URL:		http://cr.yp.to/daemontools.html
Source0:	daemontools-%{version}.tar.gz
Source1:	svscanboot.conf
Patch1:		daemontools-ECSC1.diff
Patch2:		daemontools-0.76.errno.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-root
# Needed for initctl
Requires:	initscripts >= 8.76

%description
Daemontools allows you to easily manage system services.
It runs your services on boot, passes them the correct
environment variables, backgrounds them, respawns them.
It also allows you to easily start, stop, restart, and
check the status of your services.

Use initctl to load and load the master service.

%prep
# Tarball has weird naming convention
%setup -q -n admin/%{name}-%{version}
%patch1 -p2
%patch2 -p1

%build
./package/compile

%install
# daemontools hs no built-in install procedure
rm -rf		$RPM_BUILD_ROOT
mkdir -p	$RPM_BUILD_ROOT/service
mkdir -p 	$RPM_BUILD_ROOT%{_bindir}
install -m 755 ./command/*	$RPM_BUILD_ROOT%{_bindir}
# Sensitive to initctl configuration
install -d	$RPM_BUILD_ROOT%{_sysconfdir}/init/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/init/svscanboot.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(750,root,root) %dir /service
%config %{_sysconfdir}/init/svscanboot.conf
%{_bindir}/*

%changelog
* Fri Feb 22 2013 Nico Kadel-Garcia <nkadel@gmail.com> 0.76-0.2
* Correct URL in .spec file

* Wed Jan 25 2012 Nico Kadel-Garcia <nkadel@gmail.com> 0.76-0.1
- Use bindir, not hardcoded /usr/local/bin
- Rollback version name to avoid repoforge or other conflicts

* Thu May 19 2005 Matthew Hall <matt@ecsc.co.uk> 0.76-1.fh2
- Rebuild for FireHat 2

* Mon May 20 2002 Gianni Tedesco <gianni@ecsc.co.uk>
- new version of daemontools (0.76)
- New spec for crazy djb shit
