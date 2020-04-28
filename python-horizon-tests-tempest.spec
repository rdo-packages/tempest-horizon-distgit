%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service horizon
%global plugin tempest-horizon
%global module tempest_horizon

%global common_desc \
This package contains Tempest tests to cover the Horizon project. \
Additionally it provides a plugin to automatically load these tests \
into tempest.

Name:       python-%{service}-tests-tempest
Version:    XXX
Release:    XXX
Summary:    Tempest Integration of Horizon
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch
BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-pbr >= 2.0.0
Requires:   python3-oslo-config >= 2:4.6.0
Requires:   python3-tempest >= 1:18.0.0

%description -n python3-%{service}-tests-tempest
%{common_desc}

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{service}-tests-tempest
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info

%changelog
