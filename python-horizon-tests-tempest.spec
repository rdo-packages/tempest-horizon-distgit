# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service horizon
%global plugin tempest-horizon
%global module tempest_horizon

%global common_desc \
This package contains Tempest tests to cover the Horizon project. \
Additionally it provides a plugin to automatically load these tests \
into tempest.

Name:       python-%{service}-tests-tempest
Version:    0.2.0
Release:    1%{?dist}
Summary:    Tempest Integration of Horizon
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch
BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python%{pyver}-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python%{pyver}-%{service}-tests-tempest}
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools

Requires:   python%{pyver}-pbr >= 3.1.1
Requires:   python%{pyver}-babel >= 2.3.4
Requires:   python%{pyver}-oslo-config >= 2:5.2.0
Requires:   python%{pyver}-oslo-log >= 3.36.0
Requires:   python%{pyver}-six >= 1.10.0
Requires:   python%{pyver}-tempest >= 1:18.0.0

%description -n python%{pyver}-%{service}-tests-tempest
%{common_desc}

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup

%build
%{pyver_build}

%install
%{pyver_install}

%files -n python%{pyver}-%{service}-tests-tempest
%doc README.rst
%license LICENSE
%{pyver_sitelib}/%{module}
%{pyver_sitelib}/*.egg-info

%changelog
* Mon Sep 30 2019 RDO <dev@lists.rdoproject.org> 0.2.0-1
- Update to 0.2.0

