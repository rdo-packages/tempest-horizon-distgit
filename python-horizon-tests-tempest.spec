%{!?upstream_version: %global upstream_version %{commit}}
%global commit 5378f71008513cbf1431512930154b209f418dc5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%global service horizon
%global plugin tempest-horizon
%global module tempest_horizon

Name:       python-%{service}-tests-tempest
Version:    0.0.1
Release:    0%{?alphatag}%{?dist}
Summary:    Tempest Integration of Horizon
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://github.com/openstack/%{plugin}/archive/%{commit}.tar.gz#/%{plugin}-%{shortcommit}.tar.gz

BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git

Requires:   python-pbr
Requires:   python-babel
Requires:   python-oslo-config
Requires:   python-oslo-log
Requires:   python-six
Requires:   python-tempest >= 10.0.0

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
* Thu Sep 22 2016 Alan Pevec <apevec AT redhat.com> 0.0.1-0.5378f71
- Update to pre-release 0.0.1 (5378f71008513cbf1431512930154b209f418dc5)
