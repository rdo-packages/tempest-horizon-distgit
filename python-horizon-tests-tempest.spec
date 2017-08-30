%{!?upstream_version: %global upstream_version %{commit}}
%global commit 51995f7fd549b9316b6731fc6ecdd37f23ca7212
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%global service horizon
%global plugin tempest-horizon
%global module tempest_horizon

Name:       python-%{service}-tests-tempest
Version:    0.0.1
Release:    0.1%{?alphatag}%{?dist}
Summary:    Tempest Integration of Horizon
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://github.com/openstack/%{plugin}/archive/%{commit}.tar.gz#/%{plugin}-%{shortcommit}.tar.gz

BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git

Requires:   python-pbr >= 2.0.0
Requires:   python-babel >= 2.3.4
Requires:   python-oslo-config >= 2:4.0.0
Requires:   python-oslo-log >= 3.22.0
Requires:   python-six >= 1.9.0
Requires:   python-tempest >= 12.1.0

%description
This package contains Tempest tests to cover the Horizon project.
Additionally it provides a plugin to automatically load these tests
into tempest.

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%py2_build

%install
%py2_install

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{module}
%{python2_sitelib}/*.egg-info

%changelog
* Wed Aug 30 2017 Chandan Kumar <chkumar@redhat.com> 0.0.1-0.1.51995f7fgit
- Update to pre-release 0.0.1 (51995f7fd549b9316b6731fc6ecdd37f23ca7212)
