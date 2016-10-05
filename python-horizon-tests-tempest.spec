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
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/tempest-horizon/commit/?id=b6f352de92a3f1a588e88afac936ec230592947f
