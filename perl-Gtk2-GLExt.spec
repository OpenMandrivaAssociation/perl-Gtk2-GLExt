%define module Gtk2-GLExt

Summary:	Perl module for the GtkGLExt library
Name:		perl-%{module}
Version:	0.90
Release:	%{mkrel 7}
License:	GPLv2+
Group:		Development/GNOME and GTK+
Source0:	http://downloads.sourceforge.net/sourceforge/gtk2-perl/%{module}-%{version}.tar.bz2
Patch0:		perl-Gtk2-GLExt-0.90-build.patch
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtkglext-devel >= 1
BuildRequires:	perl-devel 
BuildRequires:	perl-ExtUtils-Depends 
BuildRequires:	perl-Gtk2
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	glitz-devel
Requires:	perl-Gtk2 
Conflicts:	drakxtools < 9.1-15mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package adds perl support for GtkGLExt, an OpenGL extension to
GTK+ 2.0 or later.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0 -b .build
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="%{optflags}"
export GTK2_PERL_CFLAGS="%{optflags}"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="%{optflags}"
#%make test || :

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*

