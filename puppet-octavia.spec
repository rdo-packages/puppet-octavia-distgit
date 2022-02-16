%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x01527a34f0d0080f8a5db8d6eb6c5df21b4b6363
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%define upstream_name openstack-octavia

Name:                   puppet-octavia
Version:                18.4.1
Release:                1%{?dist}
Summary:                Puppet module for Octavia
License:                ASL 2.0

URL:                    https://launchpad.net/%{name}

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:              noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

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
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Wed Feb 16 2022 RDO <dev@lists.rdoproject.org> 18.4.1-1
- Update to 18.4.1

* Fri Apr 02 2021 RDO <dev@lists.rdoproject.org> 18.4.0-1
- Update to 18.4.0


