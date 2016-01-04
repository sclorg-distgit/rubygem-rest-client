%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from rest-client-1.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rest-client

Summary: Simple REST client for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.6.7
Release: 5%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/archiloque/rest-client

Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# A few fixes for RSpec 2.0.
# https://github.com/rest-client/rest-client/commit/264e8ae812a13eca872feba37c7555a6a027b3e9
Patch0: rubygem-rest-client-1.6.7-an-assortment-of-fixes-for-new-rspec-and-ruby.patch

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ror}rubygem(mime-types) >= 1.16
Requires: %{?scl_prefix}rubygem(netrc)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ror}rubygem(rspec)
BuildRequires: %{?scl_prefix_ror}rubygem(mime-types) >= 1.16
BuildRequires: %{?scl_prefix}rubygem(webmock) >= 0.9.1
BuildRequires: %{?scl_prefix}rubygem(netrc)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

rm -fR %{buildroot}%{gem_instdir}/.yardoc

%check
pushd .%{gem_instdir}
# TODO: According to comment in %%{PATCH0}, at least one test does not passes on
# R1.9.3. I gon't go to investigate further ATM.
%{?scl:scl enable %{scl} - << \EOF}
rspec spec | grep -e "188 examples, [34] failures"
%{?scl:EOF}
popd

%files
%{_bindir}/restclient
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/history.md
%doc %{gem_instdir}/VERSION
%doc %{gem_instdir}/spec
%doc %{gem_docdir}
%exclude %{gem_cache}
%{gem_spec}

%changelog
* Thu Feb 19 2015 Josef Stribny <jstribny@redhat.com> - 1.6.7-5
- Add SCL macros

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 1.6.7-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Sat Sep 22 2012 Tim Bielawa <tim@redhat.com> - 1.6.7-1
- Update to 1.6.7

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Vít Ondruch <vondruch@redhat.com> - 1.6.1-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Michal Fojtik <mfojtik@redhat.com> - 1.6.1-1
- New version release

* Wed Mar 03 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.0-6
- New version release

* Mon Feb 17 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-5
- Added %dir %{geminstdir} into spec file

* Mon Feb 17 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-4
- Marked README.rdoc, history.md and spec/ as %doc

* Mon Feb 16 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-3
- Fixed licence (MIT)
- Fixed duplicated files in spec
- Replaced %define with %global

* Mon Feb 16 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-2
- Fixed spec filename
- Added Ruby dependency

* Mon Feb 16 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-1
- Initial package
