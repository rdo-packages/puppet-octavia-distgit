%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%define upstream_name openstack-octavia

Name:                   puppet-octavia
Version:                15.5.0
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
* Wed Jun 16 2021 RDO <dev@lists.rdoproject.org> 15.5.0-1
- Update to 15.5.0

* Fri Oct 04 2019 RDO <dev@lists.rdoproject.org> 15.4.0-1
- Update to 15.4.0

# REMOVEME: error caused by commit https://opendev.org/openstack/puppet-octavia/commit/db40598a78a4ff4e7293e9084c13719f89c22f0c
