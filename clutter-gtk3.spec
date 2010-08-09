%define oname clutter-gtk
%define version 0.90.2
%define git 0
%if ! %git
%define release %mkrel 1
%else
%define release %mkrel 0.%git.1
%endif

%define api 1.0
%define major 0
%define libname %mklibname %name %api %major
%define libnamedevel %mklibname -d %name %api

Summary:       GTK+3 Support for Clutter
Name:          %{oname}3
Version:       %{version}
Release:       %{release}
%if %git
Source0:       %{oname}-%{git}.tar.bz2
%else
Source0:       http://www.clutter-project.org/sources/clutter-gtk/%api/%{oname}-%{version}.tar.bz2
%endif
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel >= 1.3.8
BuildRequires: gtk+3-devel
BuildRequires: gtk-doc
BuildRequires: docbook-dtd412-xml
BuildRequires: gobject-introspection-devel >= 0.6.14

%description
A library providing facilities to integrate Clutter into GTK+ 3
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.

%package -n %libname
Summary:       GTK+3 Support for Clutter
Group:         Graphics

%description -n %libname
A library providing facilities to integrate Clutter into GTK+ 3
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.


%package -n %libnamedevel
Summary:       Development headers/libraries for %name
Group:         Development/X11
Provides:      %name-devel = %version-%release
Requires:      %libname = %version-%release

%description -n %libnamedevel
Development headers/libraries for %name (see %libname package)

#----------------------------------------------------------------------------

%prep

%if %git
%setup -q -n %oname
./autogen.sh -V
%else
%setup -q -n %oname-%version
%endif
%apply_patches

%build
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf %buildroot

%makeinstall

%clean
rm -rf %buildroot

%files -n %libname
%defattr(-,root,root)
%_libdir/lib%{oname}-%{api}.so.%{major}*
%_libdir/girepository-1.0/GtkClutter-%api.typelib

%files -n %libnamedevel
%_libdir/pkgconfig/%{oname}-%{api}.pc
%_libdir/lib%{oname}-%{api}.la
%_libdir/lib%{oname}-%{api}.so
%_includedir/clutter-gtk-%{api}/
%_datadir/gir-1.0/GtkClutter-%api.gir
%dir %_datadir/gtk-doc/html/%oname
%doc %_datadir/gtk-doc/html/%oname/*
