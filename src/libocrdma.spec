Name: libocrdma
Version: 1.0.8
Release: 1%{?dist}
Summary: User-space Library for Emulex ROCE Device
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: https://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libibverbs-devel

%description
libocrdma provides a device-specific user-space driver for Emulex
One Command RoCE Adapters for use with the libibverbs library.

%package devel
Summary: Development files for the libocrdma driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Static version of libocrdma that may be linked directly to an
application, which may be useful for debugging.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/libocrdma.so

%post
/sbin/ldconfig
if [ -e %{_sysconfdir}/dat.conf ]; then
    sed -e '/ofa-v2-scm-roe-ocrdma.* u2/d' -i %{_sysconfdir}/dat.conf
    dapl_ver=`rpm -q dapl|cut -c6-8`
    echo ofa-v2-scm-roe-ocrdma0-1 u${dapl_ver} nonthreadsafe default libdaploscm.so.2 dapl.${dapl_ver} '"ocrdma0 1" ""' >> %{_sysconfdir}/dat.conf
    echo ofa-v2-scm-roe-ocrdma1-1 u${dapl_ver} nonthreadsafe default libdaploscm.so.2 dapl.${dapl_ver} '"ocrdma1 1" ""' >> %{_sysconfdir}/dat.conf
    echo ofa-v2-scm-roe-ocrdma2-1 u${dapl_ver} nonthreadsafe default libdaploscm.so.2 dapl.${dapl_ver} '"ocrdma2 1" ""' >> %{_sysconfdir}/dat.conf
    echo ofa-v2-scm-roe-ocrdma3-1 u${dapl_ver} nonthreadsafe default libdaploscm.so.2 dapl.${dapl_ver} '"ocrdma3 1" ""' >> %{_sysconfdir}/dat.conf
fi

%postun
/sbin/ldconfig
if [ -e %{_sysconfdir}/dat.conf ]; then
    sed -e '/ofa-v2-scm-roe-ocrdma.* u2/d' -i %{_sysconfdir}/dat.conf
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libocrdma-rdmav2.so
%doc AUTHORS README COPYING
%{_sysconfdir}/libibverbs.d/ocrdma.driver

%files devel
%defattr(-,root,root,-)
%{_libdir}/libocrdma*.a

%changelog
