%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%define upstream_name openstack-octavia

Name:                   puppet-octavia
Version:                10.3.1
Release:                1%{?dist}
Summary:                Puppet module for Octavia
License:                ASL 2.0

URL:                    https://launchpad.net/%{name}

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-keystone
Requires:               puppet-nova
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet-stdlib
Requires:               puppet >= 2.7.0

%description
Octavia puppet module

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/octavia/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/octavia/


%files
%{_datadir}/openstack-puppet/modules/octavia/


%changelog
* Thu Apr 27 2017 rdo-trunk <javier.pena@redhat.com> 10.3.1-1
- Update to 10.3.1

* Fri Feb 10 2017 Alfredo Moralejo <amoralej@redhat.com> 10.3.0-1
- Update to 10.3.0

