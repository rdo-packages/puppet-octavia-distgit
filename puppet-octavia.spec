%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-octavia
Version:                XXX
Release:                XXX
Summary:                Puppet module for Octavia
License:                Apache 2.0

URL:                    https://launchpad.net/%{name}

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet-stdlib
Requires:               puppet >= 2.7.0

%description
Octavia puppet module

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/octavia/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/octavia/


%files
%{_datadir}/openstack-puppet/modules/octavia/


%changelog
