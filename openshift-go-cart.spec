%global cartridgedir %{_libexecdir}/openshift/cartridges/go

Name:          openshift-go-cart
Version:       1.4.1.3
Release:       1%{?dist}
Summary:       Golang cartridge
Group:         Development/Languages
License:       ASL 2.0
URL:           https://github.com/neverlock/openshift-go-cart
Source:	       openshift-go-cart-%{version}.tar.gz
Requires:      facter
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      golang >= 1.1
Requires:      httpd
Requires:      redhat-lsb-core
Requires:      symlinks
# These 2 requirements are for support of downloading additional
# go modules
Requires:      mercurial
Requires:      bzr
BuildArch:     noarch

%description
Go cartridge for OpenShift. (Cartridge Format V2)


%prep
%setup -q

%build

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%__mkdir -p %{buildroot}%{cartridgedir}/env

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/LICENSE

%post
%{_sbindir}/oo-admin-cartridge --action install --source %{cartridgedir}

%changelog
* Fri Mar 20 2015 Chanchai <neverlock@gmail.com> 1.4.1.3-1
- fix manifest.yml
* Fri Mar 20 2015 Chanchai <neverlock@gmail.com> 1.4.1.2-1
- new package built with tito
- add spec file for build rpm package
- for go 1.4.1
* Thu Oct 17 2013 K.C. Wong <kcwong@paypal.com>
- Genesis
