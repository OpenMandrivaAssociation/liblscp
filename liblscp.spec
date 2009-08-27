%define	major	6
%define	libname	%mklibname %oname %major
%define	develname %mklibname %oname -d
%define old_libname %mklibname %name %major
%define oname lscp

Name:          liblscp
Summary:       LinuxSampler Control Protocol (LSCP) wrapper library
Version:       0.5.6
Release:       %mkrel 1
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

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%_libdir/liblscp.so.%{major}*

#--------------------------------------------------------------------

%package -n	%develname
Group: 		Development/Other
Summary: 	Libraries for %name
Requires:	%libname = %version-%release
Provides: 	%{name}-devel = %{version}-%{release}
Obsoletes:      %old_libname-devel
Obsoletes:      %{_lib}%{name}5-devel

%description -n	%develname
Development libraries from %oname

%files -n %develname
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
%configure2_5x
make

%install
make DESTDIR=%buildroot  install

%clean

