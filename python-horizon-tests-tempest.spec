%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service horizon
%global plugin tempest-horizon
%global module tempest_horizon

Name:       python-%{service}-tests-tempest
Version:    XXX
Release:    XXX
Summary:    Tempest Integration of Horizon
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git
BuildRequires:  openstack-macros

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
%py_req_cleanup

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
