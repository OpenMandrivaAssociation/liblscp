%define	major	5
%define	libname	%mklibname %oname %major
%define old_libname %mklibname %name %major
%define oname lscp

Name:          liblscp
Summary:       LinuxSampler Control Protocol (LSCP) wrapper library
Version:       0.5.5
Release:       %mkrel 2
License:       GPL
Group:	       System/Libraries 
Source0:       %{name}-%{version}.tar.gz
URL: 	       http://www.linuxsampler.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LinuxSampler Control Protocol (LSCP) wrapper library

#--------------------------------------------------------------------

%package -n	%libname
Group: 		System/Libraries
Summary: 	Libraries for %name
Provides: 	%name = %version-%release
Obsoletes:      %old_libname

%description -n %libname 
LinuxSampler Control Protocol (LSCP) wrapper library

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%_libdir/liblscp.so.5
%_libdir/liblscp.so.5.0.0

#--------------------------------------------------------------------

%package -n	%libname-devel
Group: 		Development/Other
Summary: 	Libraries for %name
Requires:	%libname = %version-%release
Provides: 	%{name}-devel = %{version}-%{release}
Obsoletes:      %old_libname-devel

%description -n	%libname-devel
Development libraries from %oname

%files -n %libname-devel
%defattr (-,root,root)
%dir %_includedir/lscp
%_includedir/lscp/*.h
%_libdir/liblscp.a
%_libdir/liblscp.la
%_libdir/liblscp.so
%_libdir/pkgconfig/lscp.pc

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%configure
make

%install
make DESTDIR=%buildroot  install

%clean

