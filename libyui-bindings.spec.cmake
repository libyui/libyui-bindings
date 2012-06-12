#
# spec file for package libyui-bindings
# generates:
#  libyui-ruby
#  libyui-python
#  perl-libyui (Perl naming convention)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# nodebuginfo

Name:           @PACKAGE@
Version:        @VERSION@
Release:        0
License:        GPL
Summary:        Bindings for libyui
Group:          Development/Sources
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake gcc-c++ ruby-devel perl python-devel swig
BuildRequires:  libyui-devel >= 2.21.5
Source:         %{name}-%{version}.tar.bz2
Prefix:         /usr

%description
-

%prep
%setup -q

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{prefix} \
      -DLIB=%{_lib} \
      -DPYTHON_SITEDIR=%{py_sitedir} \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
      -DBUILD_RUBY_GEM=no \
      ..
make %{?jobs:-j %jobs}

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf %{buildroot}

%package -n ruby-yui
Summary:        Ruby bindings for libyui
Group:          Development/Languages/Ruby

%description -n ruby-yui
-

%package -n python-yui
%py_requires
Summary:        Python bindings for libyui
Group:          Development/Languages/Python

%description -n python-yui
-

%package -n perl-yui
Requires:       perl = %{perl_version}
Summary:        Perl bindings for libyui
Group:          Development/Languages/Perl

%description -n perl-yui
-

%files -n ruby-yui
%defattr(-,root,root,-)
%doc swig/ruby/examples/*.rb
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/%{rb_arch}/yui.so

%files -n python-yui
%defattr(-,root,root,-)
%doc swig/python/examples/*.py
%{py_sitedir}/_yui.so
%{py_sitedir}/yui.py

%files -n perl-yui
%defattr(-,root,root,-)
%doc swig/perl/examples/*.pl
%{perl_vendorarch}/yui.so
%{perl_vendorlib}/yui.pm

%changelog
